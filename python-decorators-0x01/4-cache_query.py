import sqlite3
import functools
from datetime import datetime

query_cache = {}

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

# Decorator to cache query results
def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        # Get the query string: assume it's passed as a keyword argument or the first positional arg
        query = kwargs.get('query') if 'query' in kwargs else (args[0] if args else None)
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if query in query_cache:
            print(f"[{time_stamp}] [CACHE HIT] Returning cached result for query: {query}")
            return query_cache[query]
        else:
            result = func(conn, *args, **kwargs)
            query_cache[query] = result
            print(f"[{time_stamp}] [CACHE MISS] Caching result for query: {query}")
            return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")