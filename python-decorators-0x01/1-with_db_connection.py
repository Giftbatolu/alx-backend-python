import sqlite3
import functools
from datetime import datetime

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            results = func(conn, *args, **kwargs)
            print(f"[{time_stamp}] Function '{func.__name__}' executed successfully.")
            return results
        except Exception as e:
            conn.rollback()
            print(f"[{time_stamp}] Error in function '{func.__name__}': {e}")  
        finally:
            conn.close()
            print(f"[{time_stamp}] Database connection closed.") 
    return wrapper

@with_db_connection
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

# Fetch user by ID with automatic connection handling
user = get_user_by_id(user_id=1)
print(user)
