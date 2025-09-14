import sqlite3

def create_database():
    """
    Create a SQLite database and a sample table with some data.
    """
    connection = sqlite3.connect("context_async.db")
    cursor = connection.cursor()

    # Create the users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')

    sample_data = [
        ('Alice Smith', 30, 'alicesmith@gmail.com'),
        ('Bob Johnson', 24, 'bobjohnson@gmail.com'),
        ('Charlie Lee', 29, 'charlielee@gmail.com'),
        ('Diana King', 35, 'dianaking@gmail.com'),
        ('Ethan Brown', 28, 'ethanbrown@gmail.com'),
        ('Fiona White', 32, 'fionawhite@gmail.com'),
        ('George Black', 27, 'georgeblack@gmail.com'),
        ('Hannah Green', 26, 'hannahgreen@gmail.com'),
        ('Ian Gray', 31, 'iangray@gmail.com'),
        ('Jane Doe', 22, 'janedoe@gmail.com')
    ]

    # Insert some sample data
    cursor.executemany('INSERT INTO users (name, age, email) VALUES (?, ?, ?)', sample_data)

    connection.commit()
    connection.close()

create_database()
print("Database created and initialized.")