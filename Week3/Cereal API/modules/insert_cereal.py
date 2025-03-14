from modules.get_db_connection import get_db_connection
from flask import jsonify, make_response
import logging

def insert_cereal(columns, placeholders, values):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert the data into the table using parameterized query
        query = f"INSERT INTO cereal ({columns}) VALUES ({placeholders})"
        cursor.execute(query, values)

        # Commit the insertion and close connection
        conn.commit()
        conn.close()

        return jsonify({"message": "success"}), 201
    except Exception as e:
        logging.error(f"Error inserting cereal: {e}")
        return make_response(jsonify({"message": "error", "details": "Invalid or missing cereal parameters"}),400)