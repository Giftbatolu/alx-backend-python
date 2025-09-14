import sqlite3

class ExecuteQuery:
    def __init__(self, db_name, query, params=()):
        """
        A context manager to execute a SQL query and fetch results.
        """
        self.db_name = db_name
        self.query = query
        self.params = params
        self.connection = None
        self.cursor = None
        self.results = None

    def __enter__(self):
        # Validate query is a non-empty string
        if not isinstance(self.query, str) or not self.query.strip():
            raise ValueError("Query must be a non-empty string.")

        # Validate that number of `?` placeholders matches number of parameters
        placeholder_count = self.query.count("?")
        if placeholder_count != len(self.params):
            raise ValueError(f"Query expects {placeholder_count} parameters, but got {len(self.params)}.")

        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, self.params)
        self.results = self.cursor.fetchall()
        return self.results

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            if exc_type is None:
                self.connection.commit()
            else:
                self.connection.rollback()
            self.connection.close()

if __name__ == "__main__":
    db_file = 'context_async.db'
    query = "SELECT * FROM users WHERE age > ?"
    params = (25,)

    # Run query using context manager
    with ExecuteQuery(db_file, query, params) as results:
        for row in results:
            print(row)