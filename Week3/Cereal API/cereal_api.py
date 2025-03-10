from flask import Flask, request, jsonify
import sqlite3
from modules.get_cereals import get_cereals


app = Flask(__name__)



@app.route('/cereal', methods = ['GET'])
def get_all_cereals():
    
    conditions = []

    # Iterate through request arguments to get the keys and add to conditions array
    for key, value in request.args.items():
        # Add the conditions to the condition array
        conditions.append(f"{key} = ?") # Using ? for placeholder to prevent SQL injection

    # Create tuple containing the values of the request arguments.
    values = tuple(request.args.values())

    return get_cereals(conditions, values)



if __name__ == "__main__":
    app.run(debug=True)
