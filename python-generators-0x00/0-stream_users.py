#!/usr/bin/python3

import seed

def stream_users():
    """
    Generator that yields rows one by one from the user_data table.
    """
    connection = seed.connect_to_prodev()
    if connection is None:
        print("Failed to connect to the database.")
        return

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data;")

    for row in cursor:
        yield row
 
    cursor.close()
    connection.close()