from flask import Blueprint, request, jsonify
from models import Ride, db

# Create a Blueprint for ride routes
ride_bp = Blueprint('ride', __name__)

# Define a route to create a ride
@ride_bp.route('/', methods=['POST'])
def create_ride():
    data = request.json
    new_ride = Ride(
        origin=data['origin'],
        destination=data['destination'],
        date=data['date'],
        user_id=data['user_id']
    )
    db.session.add(new_ride)
    db.session.commit()
    return jsonify({'message': 'Ride created successfully!', 'ride': new_ride.id}), 201

# Define a route to get all rides
@ride_bp.route('/', methods=['GET'])
def get_rides():
    rides = Ride.query.all()
    return jsonify([
        {
            'id': ride.id,
            'origin': ride.origin,
            'destination': ride.destination,
            'date': ride.date,
            'user_id': ride.user_id
        } for ride in rides
    ])

# Define a route to delete a ride by ID
@ride_bp.route('/<int:ride_id>', methods=['DELETE'])
def delete_ride(ride_id):
    ride = Ride.query.get(ride_id)
    if not ride:
        return jsonify({'error': 'Ride not found'}), 404

    db.session.delete(ride)
    db.session.commit()
    return jsonify({'message': f'Ride with ID {ride_id} deleted successfully!'}), 200