import psycopg2
from psycopg2 import Error
from contextlib import contextmanager

class PostgreSQLDatabase:
    """
    A class to manage connections and operations for a PostgreSQL database.
    """

    def __init__(self, dbname, user, password, host='localhost', port='5432'):
        """
        Initializes the database connection parameters.

        Args:
            dbname (str): The name of the database.
            user (str): The username to connect with.
            password (str): The password for the user.
            host (str, optional): The database host. Defaults to 'localhost'.
            port (str, optional): The database port. Defaults to '5432'.
        """
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None  # Connection object
        self.cur = None   # Cursor object

    def _connect(self):
        """
        Establishes a connection to the PostgreSQL database.
        Internal method, use connect() context manager or check connection before operations.
        """
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.conn.autocommit = False  # Ensure transactions are managed explicitly
            self.cur = self.conn.cursor()
            print("Database connection established successfully.")
        except Error as e:
            print(f"Error connecting to PostgreSQL database: {e}")
            self.conn = None
            self.cur = None

    def close(self):
        """
        Closes the database connection and cursor.
        """
        if self.cur:
            self.cur.close()
            self.cur = None
        if self.conn:
            self.conn.close()
            self.conn = None
            print("Database connection closed.")

    @contextmanager
    def connect(self):
        """
        Context manager for database connection.
        Ensures connection is opened and closed properly.
        """
        self._connect()
        try:
            yield self.conn
        finally:
            self.close()

    def execute_query(self, query, params=None, fetch=False):
        """
        Executes a SQL query.

        Args:
            query (str): The SQL query string.
            params (tuple or list, optional): Parameters for the query. Defaults to None.
            fetch (bool, optional): If True, fetches results (for SELECT statements). Defaults to False.

        Returns:
            list or None: List of fetched rows if fetch is True, otherwise None.
        """
        if not self.conn or not self.cur:
            print("No active database connection. Please use the 'with db.connect():' block.")
            return None
        try:
            self.cur.execute(query, params)
            if fetch:
                return self.cur.fetchall()
            else:
                self.conn.commit()  # Commit changes for DML operations
                return self.cur.rowcount
        except Error as e:
            print(f"Error executing query: {e}")
            self.conn.rollback()  # Rollback in case of error
            return None



# --- Example Usage ---
if __name__ == "__main__":
    # IMPORTANT: Replace with your actual PostgreSQL credentials and database details
    DB_NAME = "your_database_name"
    DB_USER = "your_username"
    DB_PASSWORD = "your_password"
    DB_HOST = "localhost" # or your PostgreSQL host
    DB_PORT = "5432"

    db = PostgreSQLDatabase(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    # Example 1: Using the context manager for a robust connection
    with db.connect():
        # Create a table (if it doesn't exist)
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL
        );
        """
        print("\nCreating 'users' table...")
        db.execute_query(create_table_query)

        # Insert data
        print("\nInserting data...")
        user1 = {"name": "Alice", "email": "alice@example.com"}
        db.insert("users", user1)

        user2 = {"name": "Bob", "email": "bob@example.com"}
        db.insert("users", user2)

        # Select all users
        print("\nSelecting all users:")
        all_users = db.select("users")
        if all_users:
            for user in all_users:
                print(user)

        # Select a specific user by email
        print("\nSelecting user with email 'alice@example.com':")
        alice = db.select("users", where="email = %s", params=("alice@example.com",))
        if alice:
            print(alice[0])

        # Update a user's name
        print("\nUpdating Bob's name to 'Robert':")
        db.update("users", {"name": "Robert"}, "email = %s", ("bob@example.com",))

        print("\nSelecting all users after update:")
        all_users_after_update = db.select("users")
        if all_users_after_update:
            for user in all_users_after_update:
                print(user)

        # Delete a user
        print("\nDeleting user with email 'alice@example.com':")
        db.delete("users", "email = %s", ("alice@example.com",))

        print("\nSelecting all users after deletion:")
        all_users_after_delete = db.select("users")
        if all_users_after_delete:
            for user in all_users_after_delete:
                print(user)
        else:
            print("No users left in the table.")

    # You can also use the class without the context manager, but you'll need to manually close:
    print("\n--- Demonstrating without context manager (requires manual close) ---")
    db_manual = PostgreSQLDatabase(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
    db_manual._connect() # Manually connect

    if db_manual.conn: # Check if connection was successful
        # Insert a new user
        user3 = {"name": "Charlie", "email": "charlie@example.com"}
        db_manual.insert("users", user3)
        print("\nInserted Charlie (manual connection).")

        # Select to confirm
        print("\nUsers after manual insert:")
        manual_users = db_manual.select("users")
        if manual_users:
            for user in manual_users:
                print(user)
        db_manual.close() # Manually close the connection
    else:
        print("Could not connect manually.")