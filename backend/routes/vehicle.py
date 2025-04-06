from flask import Blueprint, request, jsonify
from models import Vehicle, db

# Create a Blueprint for vehicle routes
vehicle_bp = Blueprint('vehicle', __name__)

# Define a route to create a vehicle
@vehicle_bp.route('/', methods=['POST'])
def create_vehicle():
    data = request.json
    new_vehicle = Vehicle(
        make=data['make'],
        model=data['model'],
        year=data['year'],
        license_plate=data['license_plate'],
        user_id=data['user_id']
    )
    db.session.add(new_vehicle)
    db.session.commit()
    return jsonify({'message': 'Vehicle created successfully!', 'vehicle': new_vehicle.id}), 201

# Define a route to get all vehicles
@vehicle_bp.route('/', methods=['GET'])
def get_vehicles():
    vehicles = Vehicle.query.all()
    return jsonify([
        {
            'id': vehicle.id,
            'make': vehicle.make,
            'model': vehicle.model,
            'year': vehicle.year,
            'license_plate': vehicle.license_plate,
            'user_id': vehicle.user_id
        } for vehicle in vehicles
    ])

# Define a route to delete a vehicle by ID
@vehicle_bp.route('/<int:vehicle_id>', methods=['DELETE'])
def delete_vehicle(vehicle_id):
    vehicle = Vehicle.query.get(vehicle_id)
    if not vehicle:
        return jsonify({'error': 'Vehicle not found'}), 404

    db.session.delete(vehicle)
    db.session.commit()
    return jsonify({'message': f'Vehicle with ID {vehicle_id} deleted successfully!'}), 200