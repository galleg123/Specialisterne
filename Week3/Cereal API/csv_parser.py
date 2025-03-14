import sqlite3
import csv
from modules.get_db_connection import get_db_connection

def createTable():

    # Connect to the sql database (or create if it doesn't exist)
    conn = get_db_connection()

    # Cursor object for interacting with the sql connection
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cereal(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT, 
                   manufacturer TEXT, 
                   type TEXT, 
                   calories INTEGER, 
                   protein INTEGER, 
                   fat INTEGER, 
                   sodium INTEGER, 
                   fiber REAL, 
                   carbo REAL, 
                   sugars INTEGER, 
                   potassium INTEGER, 
                   vitamins INTEGER, 
                   shelf INTEGER, 
                   weight REAL, 
                   cups REAL, 
                   rating REAL)
    '''
    )

    # Save the changes
    conn.commit()

    # Close connection
    conn.close()

def createCSVDict(file_path):
    result = []

    with open(file_path, mode='r', newline='') as file:
        # Create a CSV reader
        csv_reader = csv.reader(file, delimiter=';')

        # Read all rows
        rows = list(csv_reader)

        # Extract keys
        keys = rows[0]

        for row in rows[2:]:
            row_dict = dict(zip(keys,row))
            result.append(row_dict)
        
        return result

def insertData(data):
    createTable()
    conn = sqlite3.connect('cereal.db')
    cursor = conn.cursor()
    for row in data:
        # Exclude 'id' from columns and values
        columns = ', '.join([key for key in row.keys() if key != 'id'])
        placeholders = ', '.join(['?'] * (len(row)))
        values = list(value for key, value in row.items() if key != 'id')
        
        # Remove the '.' from the rating value
        values[-1] = values[-1].replace('.','')
        print(values)
        
        # Convert values to a tuple
        values = tuple(values)

        # Insert the data into the table
        cursor.execute(f"INSERT INTO cereal ({columns}) VALUES ({placeholders})", values)
    
    # Commit the insertion and close connection
    conn.commit()
    conn.close()
        



if __name__ == "__main__":
    data = createCSVDict('Cereal.csv')
    insertData(data)