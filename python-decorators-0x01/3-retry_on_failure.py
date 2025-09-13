import sqlite3
import functools
from datetime import datetime
import time

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

# Decorator to retry a function on failure
def retry_on_failure(retries=3, delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, retries + 1):
                try:
                    print(f"[INFO] Attempt {attempt}...")
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"[{time_stamp}] Attempt {attempt} failed {e}")
                    if attempt < retries:
                        print(f"[{time_stamp}] Retrying in {delay} seconds...")
                        time.sleep(delay)
            print(f"[{time_stamp}] All retry attempts failed.")
            raise last_exception
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)

def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)