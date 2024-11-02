import os
import joblib
import pandas as pd
import pytest
from sklearn.preprocessing import LabelEncoder
import sys

# Add the 'websites' folder to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))  # Going up two levels

from label_enc import model_save_dir, features_to_encode  # Adjusted import for label_enc.py

@pytest.fixture(scope='module')
def setup_label_encoders():
    os.makedirs(model_save_dir, exist_ok=True)
    
    # Load the dataset (mocked for the test)
    data = pd.read_csv("website/datasets/fashion-dataset/agg_styles.csv", on_bad_lines='skip')
    
    encoders = {}
    for feature in features_to_encode:
        encoder = LabelEncoder()
        data[feature] = data[feature].fillna("Other")
        encoder.fit(data[feature])
        
        encoder_file_path = os.path.join(model_save_dir, f"{feature}_agg_label_encoder.pkl")
        joblib.dump(encoder, encoder_file_path)
        encoders[feature] = (encoder, encoder_file_path)
    
    return encoders

def test_label_encoders_fitted_and_saved(setup_label_encoders):
    for feature, (encoder, encoder_file_path) in setup_label_encoders.items():
        assert os.path.exists(encoder_file_path), f"Encoder file for '{feature}' not found."

def test_loading_label_encoders(setup_label_encoders):
    for feature, (_, encoder_file_path) in setup_label_encoders.items():
        loaded_encoder = joblib.load(encoder_file_path)
        assert isinstance(loaded_encoder, LabelEncoder), f"Loaded encoder for '{feature}' is not a LabelEncoder."

def test_encoder_functionality(setup_label_encoders):
    for feature, (encoder, encoder_file_path) in setup_label_encoders.items():
        loaded_encoder = joblib.load(encoder_file_path)
        sample_input = ["Other", "Female", "Male"]  # Modify as needed
        encoded_output = loaded_encoder.transform(sample_input)
        assert isinstance(encoded_output, (pd.Series, list)), f"Encoder output for '{feature}' is not an array."
        assert len(encoded_output) == len(sample_input), f"Encoded output length mismatch for '{feature}'."

def test_encoder_unique_classes(setup_label_encoders):
    for feature, (encoder, encoder_file_path) in setup_label_encoders.items():
        unique_classes = encoder.classes_
        assert unique_classes is not None, f"No classes found for encoder of feature '{feature}'."
        assert len(unique_classes) > 0, f"Encoder for '{feature}' has no unique classes."

# To run the test, use the command: pytest -q --tb=short test_labelenc.py
