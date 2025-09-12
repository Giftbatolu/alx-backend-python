#!/usr/bin/python3

import seed

def paginate_users(page_size, offset):
    """
    Fetch a page of users from the database.
    """
    connection = seed.connect_to_prodev()
    if connection is None:
        print("Failed to connect to the database.")
        return 

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s;", (page_size, offset))
    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return rows

def lazy_paginate(page_size):
    """
    Generator that yields users page by page.
    """
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size