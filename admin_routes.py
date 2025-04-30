from flask import Blueprint, jsonify
from app.models import User, Donation

admin_bp = Blueprint('admin', __name__)

# View all users
@admin_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.filter_by(role='user').all()
    return jsonify([{
        'id': u.id,
        'username': u.username,
        'email': u.email,
        'location': u.location
    } for u in users])

# View all NGOs
@admin_bp.route('/ngos', methods=['GET'])
def get_ngos():
    ngos = User.query.filter_by(role='ngo').all()
    return jsonify([{
        'id': n.id,
        'username': n.username,
        'email': n.email,
        'location': n.location
    } for n in ngos])

# View all donations
@admin_bp.route('/donations', methods=['GET'])
def get_donations():
    donations = Donation.query.all()
    return jsonify([{
        'id': d.id,
        'product_name': d.product_name,
        'status': d.status,
        'user_id': d.user_id,
        'ngo_id': d.ngo_id,
        'date': d.date
    } for d in donations])
