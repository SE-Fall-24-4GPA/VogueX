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
import tensorflow as tf
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Load dataset
data = pd.read_csv("datasets/fashion-dataset/styles.csv", on_bad_lines="skip")
data["image"] = data["id"].astype(str) + ".jpg"

# Specify the features to be encoded
features_to_encode = [
    "gender",
    "masterCategory",
    "subCategory",
    "articleType",
    "baseColour",
    "season",
    "usage",
]

# Dictionary to store label encoders for each feature
# label_encoders = {feature: LabelEncoder() for feature in features_to_encode}
model_save_dir = "datasets/model_params/"
label_encoders = {
    col: joblib.load(os.path.join(model_save_dir, f"{col}_label_encoder.pkl"))
    for col in features_to_encode
}

# Apply label encoding to each specified feature
for feature in features_to_encode:
    # Fit the LabelEncoder on the column and transform the data
    data[feature] = label_encoders[feature].fit_transform(
        data[feature].fillna("Unknown")
    )

# Convert the encoded DataFrame into a dictionary of integer arrays for each feature
encoded_dataset = {feature: data[feature].values for feature in features_to_encode}


class FeatureExtractor(tf.keras.Model):
    def __init__(self, vocab_sizes, embedding_dim=8):
        super(FeatureExtractor, self).__init__()
        self.embeddings = {
            feature: tf.keras.layers.Embedding(input_dim=size, output_dim=embedding_dim)
            for feature, size in vocab_sizes.items()
        }

    def call(self, inputs):
        embedded_features = [
            self.embeddings[feature](inputs[feature]) for feature in inputs
        ]
        concatenated = tf.concat(embedded_features, axis=-1)
        return concatenated


# Vocabulary sizes for each feature
vocab_sizes = {}

for feature in features_to_encode:
    encoder = label_encoders[feature]
    encoded_dataset[feature] = encoder.fit_transform(data[feature].fillna("Unknown"))
    vocab_sizes[feature] = len(encoder.classes_)

# Initialize model and process dataset
feature_extractor = FeatureExtractor(vocab_sizes, embedding_dim=8)
# Assume encoded_dataset is a dictionary of integer-encoded feature columns
encoded_features = feature_extractor(encoded_dataset).numpy()

# Custom input example
custom_input = {  # Encode custom input in the same way as dataset features
    "gender": 1,
    "masterCategory": 2,
    "subCategory": 0,
    "articleType": 4,
    "baseColour": 3,
    "season": 2,
    "usage": 1,
}
custom_input_tensors = {
    feature: tf.constant([value]) for feature, value in custom_input.items()
}

custom_features = feature_extractor(custom_input_tensors).numpy()

# Compute cosine similarity
similarity_scores = cosine_similarity(custom_features, encoded_features)
top_10_indices = np.argsort(similarity_scores[0])[::-1][:10]

# Retrieve top 10 similar items
similar_items = data.iloc[top_10_indices]

print(similar_items)
