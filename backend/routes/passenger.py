from flask import Blueprint, request, jsonify
from models import Passenger, db

# Create a Blueprint for passenger routes
passenger_bp = Blueprint('passenger', __name__)

# Define a route to add a passenger to a ride
@passenger_bp.route('/', methods=['POST'])
def add_passenger():
    data = request.json
    new_passenger = Passenger(
        user_id=data['user_id'],
        ride_id=data['ride_id']
    )
    db.session.add(new_passenger)
    db.session.commit()
    return jsonify({'message': 'Passenger added successfully!', 'passenger': new_passenger.id}), 201

# Define a route to get all passengers
@passenger_bp.route('/', methods=['GET'])
def get_passengers():
    passengers = Passenger.query.all()
    return jsonify([
        {
            'id': passenger.id,
            'user_id': passenger.user_id,
            'ride_id': passenger.ride_id
        } for passenger in passengers
    ])

# Define a route to delete a passenger by ID
@passenger_bp.route('/<int:passenger_id>', methods=['DELETE'])
def delete_passenger(passenger_id):
    passenger = Passenger.query.get(passenger_id)
    if not passenger:
        return jsonify({'error': 'Passenger not found'}), 404

    db.session.delete(passenger)
    db.session.commit()
    return jsonify({'message': f'Passenger with ID {passenger_id} deleted successfully!'}), 200