# Import the database object and models
from app import db  # Import the database object (initialized in app.py)
from models import User, Ride  # Import the models (tables) defined in models.py

# Create all tables in the database
# This will create the tables defined in models.py if they don't already exist
db.create_all()

# Print a message to indicate that the database has been initialized
print("Database initialized!")