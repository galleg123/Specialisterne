from modules.get_db_connection import get_db_connection
from flask import jsonify, make_response
import logging

def update_cereal(columns, values):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Update the data in the table using parameterized query
        query = f"UPDATE cereal SET {columns} WHERE id = ?"

        cursor.execute(query, values)

        # Commit the update and close connection
        conn.commit()
        conn.close()

        return jsonify({"message": "success"})
    except Exception as e:
        logging.error(f"Error updating cereal: {e}")
        return make_response(jsonify({"message": "error", "details": "Invalid parameter given"}), 400)