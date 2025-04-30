from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models import User, Donation

user_bp = Blueprint('user', __name__)

# Register
@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        return jsonify({'message': 'User already exists'}), 400

    hashed_password = generate_password_hash(data['password'], method='sha256')
    user = User(
        username=data['username'],
        email=data['email'],
        password=hashed_password,
        role='user',
        location=data.get('location', '')
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

# Login
@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email'], role='user').first()
    if user and check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Login successful', 'user_id': user.id}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

# Donate Item
@user_bp.route('/donate', methods=['POST'])
def donate():
    data = request.get_json()
    donation = Donation(
        product_name=data['product_name'],
        category=data['category'],
        quantity=data['quantity'],
        location=data.get('location'),
        user_id=data['user_id']
    )
    db.session.add(donation)
    db.session.commit()
    return jsonify({'message': 'Donation submitted'}), 201

# Track Donation Status
@user_bp.route('/donations/<int:user_id>', methods=['GET'])
def get_user_donations(user_id):
    donations = Donation.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'id': d.id,
        'product_name': d.product_name,
        'category': d.category,
        'status': d.status,
        'date': d.date
    } for d in donations])
