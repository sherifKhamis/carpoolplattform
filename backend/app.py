# Import necessary libraries
from flask import Flask  # Flask is the core framework for building web applications
from flask_sqlalchemy import SQLAlchemy  # SQLAlchemy is used for database interactions
from flask_migrate import Migrate  # Migrate is used for managing database migrations
from models import db  # Import the database object (defined in models.py)

# Create an instance of the Flask application
app = Flask(__name__)

# Configure the database connection
# SQLALCHEMY_DATABASE_URI specifies the database type and location (SQLite in this case)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///carpool.db'

# Disable SQLALCHEMY_TRACK_MODIFICATIONS to avoid unnecessary overhead
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the Flask app
db = SQLAlchemy(app)

# Initialize Flask-Migrate for database migrations
migrate = Migrate(app, db)

# Define a route for the home page
@app.route('/')
def home():
    # This function is executed when the user visits the root URL ('/')
    return "Welcome to the Carpool Platform!"

# Run the application if this file is executed directly
if __name__ == '__main__':
    # Start the Flask development server with debugging enabled
    app.run(debug=True)