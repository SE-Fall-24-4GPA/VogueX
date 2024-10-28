import pickle
import os
import joblib
import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Define the FeatureExtractor class with simple embedding layers for each feature
@tf.keras.utils.register_keras_serializable()
class FeatureExtractor(tf.keras.Model):
    def __init__(self, feature_vocab_sizes, embedding_dim):
        super(FeatureExtractor, self).__init__()
        self.embeddings = {
            feature: tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim)
            for feature, vocab_size in feature_vocab_sizes.items()
        }

    def call(self, inputs):
        # Embed each feature and concatenate all embeddings
        embedded = [self.embeddings[feature](inputs[feature]) for feature in self.embeddings]
        concatenated = tf.concat(embedded, axis=1)
        return concatenated
    
    def get_config(self):
        return {
            'feature_vocab_sizes': self.feature_vocab_sizes,
            'embedding_dim': self.embedding_dim,
            **super(FeatureExtractor, self).get_config()  # Include base class config
        }
        
    @classmethod
    def from_config(cls, config):
        feature_vocab_sizes = config.pop('feature_vocab_sizes')
        embedding_dim = config.pop('embedding_dim')
        return cls(feature_vocab_sizes, embedding_dim, **config)

def get_recommendations():
    # Directory where model and encoders are saved
    model_save_dir = 'datasets/model_params/'

    # Load the pre-trained model and specify FeatureExtractor as a custom object
    with open(os.path.join(model_save_dir, 'text_feature_extractor.pkl'), 'rb') as model_file:
        loaded_model = pickle.load(model_file)
    # loaded_model = tf.keras.models.load_model(
    #     os.path.join(model_save_dir, 'text_feature_extractor.h5'),
    #     custom_objects={'FeatureExtractor': FeatureExtractor}
    # )

    # Load label encoders for each feature
    features_to_encode = ['gender', 'masterCategory', 'subCategory', 'articleType', 'baseColour', 'season', 'usage']
    label_encoders = {col: joblib.load(os.path.join(model_save_dir, f'{col}_label_encoder.pkl')) for col in features_to_encode}

    # Load dataset and add image filenames
    csv_path = "datasets/fashion-dataset/styles.csv"
    df = pd.read_csv(csv_path, on_bad_lines='skip')
    df['image'] = df['id'].astype(str) + ".jpg"

    # Prepare encoded features for each row in the dataset
    encoded_data = {col: label_encoders[col].transform(df[col].astype(str)) for col in features_to_encode}
    dataset_features = loaded_model({col: tf.constant(encoded_data[col]) for col in features_to_encode}).numpy()

    # Define a function to find top-N similar items
    def find_similar_items(input_values, model, encoders, dataset_features, top_n=10):
        # Encode the input query values
        encoded_input = {col: tf.constant([encoders[col].transform([input_values[col]])[0]]) for col in input_values}
        input_features = model(encoded_input).numpy()

        # Calculate cosine similarity between input and dataset features
        similarities = cosine_similarity(input_features, dataset_features)
        top_indices = np.argsort(similarities[0])[::-1][:top_n]
        return df.iloc[top_indices]

    # Define the input query to get recommendations
    input_values = {
        'gender': 'Men',
        'masterCategory': 'Apparel',
        'subCategory': 'Topwear',
        'articleType': 'Shirts',
        'baseColour': 'Navy Blue',
        'season': 'Fall',
        'usage': 'Casual'
    }

    # Retrieve and display the top 10 similar items
    similar_items = find_similar_items(input_values, loaded_model, label_encoders, dataset_features, top_n=10)
    print(similar_items[['productDisplayName', 'image']])

    return similar_items

# Run the function to test the model
_ = get_recommendations()