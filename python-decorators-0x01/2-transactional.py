import sqlite3
import functools
from datetime import datetime

# Decorator to manage database connection
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

# Decorator to wrap function in a transaction
def transactional(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            print(f"[{time_stamp}] Transaction committed successfully.")
            return result
        except Exception as e:
            conn.rollback()
            print(f"[{time_stamp}] Transaction rolled back due to error: {e}")
            raise
    return wrapper


@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
    #### Update user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')