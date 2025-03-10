from flask import Flask, request, jsonify
import sqlite3
from modules.fetch_cereals import fetch_cereals
from modules.insert_cereal import insert_cereal
from modules.update_cereal import update_cereal
from modules.remove_cereal import remove_cereal


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



@app.route('/cereal', methods = ['POST'])
def post_cereal():
    # Get the data from the request
    data = request.json

    # Exclude 'id' from columns and values
    columns = ', '.join([key for key in data.keys() if key != 'id'])
    placeholders = ', '.join(['?'] * len(data))
    values = tuple(value for key, value in data.items() if key != 'id')

    # Insert the data into the table
    return insert_cereal(columns, placeholders, values)



@app.route('/cereal/<int:id>', methods = ['PUT'])
def put_cereal(id):
    # Get the data from the request
    data = request.json

    # Include 'id' in the columns and values
    columns = ', '.join([f"{key} = ?" for key in data.keys()])
    values = tuple(data.values())


    # Add the id to the values tuple
    values += (id,)

    # Update the data in the table
    return update_cereal(columns, values)

@app.route('/cereal/<int:id>', methods = ['DELETE'])
def delete_cereal(id):
    return remove_cereal(id)

if __name__ == "__main__":
    app.run(debug=True)
