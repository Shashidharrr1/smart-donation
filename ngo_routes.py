from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from app import db
from app.models import User, Donation

ngo_bp = Blueprint('ngo', __name__)

# NGO Login
@ngo_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email'], role='ngo').first()
    if user and check_password_hash(user.password, data['password']):
        return jsonify({'message': 'NGO login successful', 'ngo_id': user.id}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

# View Pending Donations
@ngo_bp.route('/donations', methods=['GET'])
def view_donations():
    donations = Donation.query.filter_by(status='pending').all()
    return jsonify([{
        'id': d.id,
        'product_name': d.product_name,
        'category': d.category,
        'quantity': d.quantity,
        'location': d.location,
        'user_id': d.user_id
    } for d in donations])

# Update Donation Status
@ngo_bp.route('/donation/<int:donation_id>', methods=['PUT'])
def update_status(donation_id):
    data = request.get_json()
    donation = Donation.query.get_or_404(donation_id)
    donation.status = data['status']
    donation.ngo_id = data['ngo_id']
    db.session.commit()
    return jsonify({'message': 'Donation status updated'})
