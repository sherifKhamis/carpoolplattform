from flask import Blueprint, request, jsonify
from models import User, db

# Create a Blueprint for user routes
user_bp = Blueprint('user', __name__)

# Define a route to create a user
@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(name=data['name'], email=data['email'], driver=data.get('driver', False))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully!', 'user': new_user.id}), 201

# Define a route to get all users
@user_bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'name': user.name, 'email': user.email, 'driver': user.driver} for user in users])

# Define a route to delete a user by ID
@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': f'User with ID {user_id} deleted successfully!'}), 200