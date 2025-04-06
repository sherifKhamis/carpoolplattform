# Import the database object from SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Create a database object (this will be initialized in app.py)
db = SQLAlchemy()

# Define the User model (represents a table in the database)
class User(db.Model):
    # Define the table name (optional, defaults to the class name in lowercase)
    __tablename__ = 'users'

    # Define the columns of the table
    id = db.Column(db.Integer, primary_key=True)  # Primary key column (unique identifier)
    name = db.Column(db.String(80), nullable=False)  # Name column (required, max 80 characters)
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email column (unique and required)
    driver = db.Column(db.Boolean, default=False)  # Indicates if the user is a driver
    rides = db.relationship('Ride', backref='user', lazy=True)  # Relationship to rides

    # Define a string representation of the object (useful for debugging)
    def __repr__(self):
        return f'<User {self.name}>'

# Define the Ride model (represents another table in the database)
class Ride(db.Model):
    # Define the table name (optional)
    __tablename__ = 'rides'

    # Define the columns of the table
    id = db.Column(db.Integer, primary_key=True)  # Primary key column
    origin = db.Column(db.String(120), nullable=False)  # Origin column (required)
    destination = db.Column(db.String(120), nullable=False)  # Destination column (required)
    date = db.Column(db.DateTime, nullable=False)  # Date column (required)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key to the User table

    # Define a string representation of the object
    def __repr__(self):
        return f'<Ride {self.origin} to {self.destination}>'

# Define the Vehicle model (represents another table in the database)
class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(80), nullable=False)  # Vehicle make (e.g., Toyota)
    model = db.Column(db.String(80), nullable=False)  # Vehicle model (e.g., Corolla)
    year = db.Column(db.Integer, nullable=False)  # Year of manufacture
    license_plate = db.Column(db.String(20), unique=True, nullable=False)  # License plate number
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Driver's ID

# Define the Passenger model (represents another table in the database)
class Passenger(db.Model):
    __tablename__ = 'passengers'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Passenger's ID
    ride_id = db.Column(db.Integer, db.ForeignKey('rides.id'), nullable=False)  # Ride ID