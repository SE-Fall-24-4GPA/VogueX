# VogueX
# Copyright (c) 2024 Group 84: Gokul Prakash Ramesh, Haricharan Bharathi, Raghunandan Ganesh Mante
# This project is licensed under the MIT License.
# #
# Governance Model:
# This project follows an open governance model, which includes a leadership team,
# contribution guidelines, a code of conduct, and a clear decision-making process.
# Contributions are welcome, and please see CONTRIBUTING.md for details.

import os
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Define the path to save the label encoders
model_save_dir = 'website/datasets/new_model_params/'
os.makedirs(model_save_dir, exist_ok=True)

# Load the dataset
data = pd.read_csv("website/datasets/fashion-dataset/agg_styles.csv", on_bad_lines='skip')

# Specify the features to be encoded
features_to_encode = ['gender', 'masterCategory', 'subCategory', 'articleType', 'baseColour', 'season', 'usage']

# Fit and save label encoders for each feature
for feature in features_to_encode:
    print(f"Fitting LabelEncoder for '{feature}'")
    encoder = LabelEncoder()
    
    # Fill missing values and fit encoder
    data[feature] = data[feature].fillna("Other")
    encoder.fit(data[feature])
    
    # Save the fitted encoder
    encoder_file_path = os.path.join(model_save_dir, f"{feature}_agg_label_encoder.pkl")
    joblib.dump(encoder, encoder_file_path)
    print(f"Saved LabelEncoder for '{feature}' to {encoder_file_path}")

print("All label encoders have been fitted and saved.")
