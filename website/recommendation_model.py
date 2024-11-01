import os
import joblib
import tensorflow as tf
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np


def get_recommendations(user_input):
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
                feature: tf.keras.layers.Embedding(
                    input_dim=size, output_dim=embedding_dim
                )
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
        encoded_dataset[feature] = encoder.fit_transform(
            data[feature].fillna("Unknown")
        )
        vocab_sizes[feature] = len(encoder.classes_)

    # Initialize model and process dataset
    feature_extractor = FeatureExtractor(vocab_sizes, embedding_dim=8)
    # Assume encoded_dataset is a dictionary of integer-encoded feature columns
    encoded_features = feature_extractor(encoded_dataset).numpy()

    # Define the input query to get recommendations
    # user_input = {
    #     'gender': 'Men',
    #     'masterCategory': 'Apparel',
    #     'subCategory': 'Topwear',
    #     'articleType': 'Shirts',
    #     'baseColour': 'Navy Blue',
    #     'season': 'Fall',
    #     'usage': 'Casual'
    # }

    encoded_user_input = {
        feature: label_encoders[feature].fit_transform([value])[0]
        for feature, value in user_input.items()
    }

    user_input_tensors = {
        feature: tf.constant([value]) for feature, value in encoded_user_input.items()
    }

    user_features = feature_extractor(user_input_tensors).numpy()

    # Compute cosine similarity
    similarity_scores = cosine_similarity(user_features, encoded_features)
    top_10_indices = np.argsort(similarity_scores[0])[::-1][:10]

    # Retrieve top 10 similar items
    similar_items = data.iloc[top_10_indices]

    return similar_items["image"]


# # Run the function to test the model
# similar_items = get_recommendations()
# print(similar_items)
