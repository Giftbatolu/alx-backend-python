#!/usr/bin/python3

import seed

def stream_users_in_batches(batch_size):
    """
    Generator that fetches users in batches from MySQL.
    """
    connection = seed.connect_to_prodev()
    if connection is None:
        print("Failed to connect to the database.")
        return

    cursor = connection.cursor(dictionary=True)

    offset = 0
    while True:
        cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s;", (batch_size, offset))
        rows = cursor.fetchall()
        if not rows:
            break
        yield rows
        offset += batch_size

    cursor.close()
    connection.close()

def batch_processing(batch_size):
    """
    Processes user batches, yielding users over age 25.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user.get('age', 0) > 25:
                yield user