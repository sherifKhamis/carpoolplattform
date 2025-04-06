# Carpool Platform Backend

This backend provides the core features of a carpool platform using **Flask** and **SQLAlchemy**.

---

## Key Features

1. **Users**  
   - Create new users.  
   - Retrieve all users.  
   - Delete users by ID.  

2. **Rides**  
   - Create rides tied to a user (driver).  
   - Retrieve all rides.  
   - Delete rides by ID.  

3. **Vehicles**  
   - Create vehicles owned by drivers.  
   - Retrieve all vehicles.  
   - Delete vehicles by ID.  

4. **Passengers**  
   - Add passengers to rides.  
   - Retrieve all passengers.  
   - Delete passengers by ID.  

---

## Models

1. **User**  
   - Attributes: id, name, email, driver, rides (relationship).

2. **Ride**  
   - Attributes: id, origin, destination, date, user_id (driver), relationship to User.  

3. **Vehicle**  
   - Attributes: id, make, model, year, license_plate, user_id (driver).  

4. **Passenger**  
   - Attributes: id, user_id, ride_id.  

---

## API Endpoints

Below are the primary routes (registered as Blueprints in app.py):

- **User**  
  - POST /users  
  - GET /users  
  - DELETE /users/<user_id>  

- **Ride**  
  - POST /rides  
  - GET /rides  
  - DELETE /rides/<ride_id>  

- **Vehicle**  
  - POST /vehicles  
  - GET /vehicles  
  - DELETE /vehicles/<vehicle_id>  

- **Passenger**  
  - POST /passengers  
  - GET /passengers  
  - DELETE /passengers/<passenger_id>  

---

## Getting Started

1. **Install Dependencies**  
   Install the required Python packages:  
   ```bash
   pip install -r requirements.txt

2. **Initialize the Database**   
   ```bash
   python db_init.py

3. **Run the App**   
   ```bash
   python app.py