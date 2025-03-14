from modules.get_db_connection import get_db_connection
from flask import jsonify, make_response
import logging
import os


def send_image(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Get the image from the database
        cursor.execute(f"SELECT name FROM cereal WHERE id = {id}")
        
        file_name = cursor.fetchone()[0]
        full_path = os.path.join("CerealPictures",f'{file_name}.jpg')
        print(full_path)
        # Create a response with the image
        with open(full_path, 'rb') as image_file:
            image = image_file.read()
        response = make_response(image)
        response.headers.set('Content-Type', 'image/jpeg')

        return response
    except Exception as e:
        logging.error(f"Error getting image: {e}")
        return make_response(jsonify({"Error" : "Image not found"}), 404)