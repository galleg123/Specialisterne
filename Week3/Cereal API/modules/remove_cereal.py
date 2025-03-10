from modules.get_db_connection import get_db_connection
from flask import jsonify, make_response

def remove_cereal(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Delete the cereal with the given id
    cursor.execute("DELETE FROM cereal WHERE id = ?", (id,))
    conn.commit()

    # Check if any rows were affected
    if cursor.rowcount == 0:
        conn.close()
        return make_response(jsonify({"message": "Cereal not found"}), 404)

    conn.close()
    return jsonify({"message": "Cereal deleted successfully"})
