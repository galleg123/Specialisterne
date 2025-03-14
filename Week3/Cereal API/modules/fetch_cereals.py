from flask import jsonify
from modules.get_db_connection import get_db_connection


def fetch_cereals(conditions, values):
    # The initial query, that will be sent if no additinol conditions are passed
    query = "SELECT * FROM cereal"
    
    # Add any conditions that are passed to the query. conditions being of the format (key = ?) where ? is the placeholder variable replaced by value during execute.
    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    # Initiate sql connection.
    conn = get_db_connection()
    cursor = conn.cursor()

    # Try except to prevent api arguments that are not a column in the table.
    try:
        cursor.execute(query, values)
    except:
        return jsonify({"Error": "Invalid argument"}), 400

    # Fetch matching rows 
    rows = cursor.fetchall()

    # Convert rows to a list of dictionaries
    result = [dict(row) for row in rows]

    # Close database connection
    conn.close()

    return jsonify(result), 200
