import os
import pickle
import tensorflow as tf
from tensorflow.keras.applications import DenseNet121
from tensorflow.keras.models import load_model
import pandas as pd

# Define file paths
MODEL_H5_PATH = "VogueX/datasets/densenet_model.h5densenet_model.h5"
MODEL_PKL_PATH = "VogueX/datasets/densenet_model.pkl"
CSV_FILE_PATH = "VogueX/datasets/batch_embeddings.csv"


# Test if model file is saved as .h5 format
def test_model_h5_exists():
    assert os.path.exists(MODEL_H5_PATH), "Model .h5 file not found."


# Test if model file is saved as .pkl format
def test_model_pkl_exists():
    assert os.path.exists(MODEL_PKL_PATH), "Model .pkl file not found."


# Test if the model architecture is DenseNet121
def test_model_is_densenet():
    model = load_model(MODEL_H5_PATH)
    assert isinstance(
        model.layers[0], DenseNet121
    ), "The base model is not DenseNet121."


# Test if model files can be loaded properly
def test_load_model_files():
    with open(MODEL_PKL_PATH, "rb") as f:
        model = pickle.load(f)
    assert model is not None, "Failed to load model from .pkl file."

    h5_model = load_model(MODEL_H5_PATH)
    assert h5_model is not None, "Failed to load model from .h5 file."


# Test if CSV file with embeddings exists and loads correctly
def test_embeddings_csv_exists():
    assert os.path.exists(CSV_FILE_PATH), "Embeddings CSV file not found."


def test_embeddings_csv_load():
    df = pd.read_csv(CSV_FILE_PATH)
    assert not df.empty, "Embeddings CSV file is empty."


# Test if embedding array shape is as expected
def test_embedding_shape():
    df = pd.read_csv(CSV_FILE_PATH)
    sample_embedding = df.iloc[0].values
    assert (
        sample_embedding.shape[0] > 0
    ), "Embedding array is empty or incorrectly formatted."
