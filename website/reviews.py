from flask import Blueprint, request, jsonify
from .models import Review  # Ensure you have a Review model defined in models.py
from . import db  # Import the database instance

reviews_bp = Blueprint('reviews', __name__)

@reviews_bp.route('/reviews/', methods=['POST'])
def submit_review():
    data = request.get_json()
    favourite_url = data.get('favourite_url')
    rating = data.get('rating')

    if not favourite_url or rating not in [1, 2, 3, 4, 5]:
        return jsonify({'error': 'Invalid input'}), 400

    new_review = Review(favourite_url=favourite_url, rating=rating)
    db.session.add(new_review)
    db.session.commit()

    return jsonify({'message': 'Review submitted successfully!'}), 201
