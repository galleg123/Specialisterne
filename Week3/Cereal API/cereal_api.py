from flask import Flask, request, jsonify
import sqlite3
from modules.fetch_cereals import fetch_cereals
from modules.insert_cereal import insert_cereal
from modules.update_cereal import update_cereal
from modules.remove_cereal import remove_cereal
from modules.validate_login import validate_login


app = Flask(__name__)


# Get all cereals or filter by query parameters
@app.route('/cereal', methods = ['GET'])
def get_cereals():
    
    conditions = []

    # Iterate through request arguments to get the keys and add to conditions array
    for key, value in request.args.items():
        # Add the conditions to the condition array
        conditions.append(f"{key} = ?") # Using ? for placeholder to prevent SQL injection

    # Convert the values to a tuple to pass to the get_cereals function to prevent SQL injection
    values = tuple(request.args.values())

    # Call the get_cereals function from get_cereals.py
    return fetch_cereals(conditions, values)


# Get a cereal by id
@app.route('/cereal/<int:id>', methods = ['GET'])
def get_cereal_by_id(id):
    conditions = ['id = ?']
    values = (id,)
    return fetch_cereals(conditions, values)



# Post a cereal to the database if valid token is provided.
@app.route('/cereal', methods = ['POST'])
def post_cereal():
    # Get the data from the request
    data = request.json

    if not validate_login(request.headers['Authorization']):
        return jsonify({'message': 'Bearer token missing or invalid'}), 401 # Return 401 Unauthorized if token is missing or invalid

    # Exclude 'id' from columns and values
    columns = ', '.join([key for key in data.keys() if key != 'id'])
    placeholders = ', '.join(['?'] * len(data))
    values = tuple(value for key, value in data.items() if key != 'id')

    # Insert the data into the table
    return insert_cereal(columns, placeholders, values)




# Update a cereal in the database if it exists, and if a valid token is provided.
@app.route('/cereal/<int:id>', methods = ['PUT'])
def put_cereal(id):
    # Get the data from the request
    data = request.json

    # Validate bearer token
    if not validate_login(request.headers['Authorization']):
        return jsonify({'message': 'Bearer token missing or invalid'}), 401 # Return 401 Unauthorized if token is missing or invalid

    # Include 'id' in the columns and values
    columns = ', '.join([f"{key} = ?" for key in data.keys()])
    values = tuple(data.values())

    # Add the id to the values tuple
    values += (id,)

    # Update the data in the table
    return update_cereal(columns, values)


# Delete a cereal from the database if it exists, and if valid token is provided.
@app.route('/cereal/<int:id>', methods = ['DELETE'])
def delete_cereal(id):
    # Validate bearer token
    if not validate_login(request.headers['Authorization']):
        return jsonify({'message': 'Bearer token missing or invalid'}), 401 # Return 401 Unauthorized if token is missing or invalid
    
    return remove_cereal(id)



@app.route('/login', methods = ['POST'])
def login():
    # Get the data from the request
    data = request.json

    # Check if the username and password are correct
    if data['username'] == 'admin' and data['password'] == 'password':
        # Return a bearer token
        return jsonify({'message': 'Login successful',
                        'bearer_token': 'random_bearer_token'})
    else:
        return jsonify({'message': 'Login failed'})
    
if __name__ == "__main__":
    app.run(debug=True)
