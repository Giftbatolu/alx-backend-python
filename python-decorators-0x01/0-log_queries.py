import sqlite3
import functools
from datetime import datetime

def initialize_db():
    """Initialize user_data table in users.db database."""
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    # Create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT UNIQUE NOT NULL
        );
    """)
        
    # Sample data
    sample_users = [
        ("Alice Johnson", 28, "aliceohnson@gmail.com"),
        ("Bob Smith", 35, "bobsmith@gmail.com"),
        ("Carol White", 22, "carolwhite@gmail.com"),
        ("David Brown", 41, "davidbrown@gmail.com"),
        ("Eve Black", 30, "eveblack@gmail.com"),
        ("Frank Green", 27, "frankgrenn@gmail.com"),
        ("Grace Blue", 33, "graceblue@gmail.com"),
        ("Hank Yellow", 29, "hankyellow@gmail.com"),
        ("Ivy Orange", 26, "ivyorange@gmail.com"),
        ("Jack Purple", 38, "jackpurple@gmail.com")
    ]
    try:
        # Insert data
        cursor.executemany("INSERT INTO users (name, age, email) VALUES (?, ?, ?);", sample_users)
    except sqlite3.IntegrityError:
        pass # Ignore if data already exists

    # Commit and close
    connection.commit()
    connection.close()

# Run database setup
initialize_db()
print("Database initialized and sample data inserted.")

#### decorator to lof SQL queries
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Extract the SQL query from arguments (assuming first positional arg or 'query' kwarg)
        query = kwargs.get('query') if 'query' in kwargs else (args[0] if args else None)
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{time_stamp}] Executing query: {query}")
        try:
            results = func(*args, **kwargs)
            print(f"[{time_stamp}] Query executed successfully.")
            return results
        except Exception as e:
            print(f"[{time_stamp}] Error executing query: {e}")
            raise
    return wrapper

#### function to fetch all users from the database
@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
print(users)