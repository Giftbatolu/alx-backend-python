#!/usr/bin/python3

import seed

def stream_users_in_batches(batch_size):
    """
   Generator that yields user ages one by one from user_data table.
    """
    connection = seed.connect_to_prodev()
    if connection is None:
        print("Failed to connect to the database.")
        return

    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data;")
    
    for (age,) in cursor:
        if age is not None:
            yield int(age)

    cursor.close()
    connection.close()

def calculate_average_age():
    """Calculates and prints the average age using a generator."""
    total = 0
    count = 0
    for age in stream_user_ages():
        total += age
        count += 1

    if count == 0:
       return 0
    
    return average = total / count