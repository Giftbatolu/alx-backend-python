import mysql.connector as connector
from mysql.connector import Error
from mysql.connector import errorcode
import csv
import uuid

# Set up the MySQL database, ALX_prodev with the table user_data with the following fields:
# user_id(Primary Key, UUID, Indexed)
# name (VARCHAR, NOT NULL)
# email (VARCHAR, NOT NULL)
# age (DECIMAL,NOT NULL)
# Populate the database with the sample data from this user_data.csv
# Prototypes:
# def connect_db() :- connects to the mysql database server
# def create_database(connection):- creates the database ALX_prodev if it does not exist
# def connect_to_prodev() connects the the ALX_prodev database in MYSQL
# def create_table(connection):- creates a table user_data if it does not exists with the required fields
# def insert_data(connection, data):- inserts data in the database if it does not exist

def connect_db():
    """ Connect to MySQL database """
    try:
        connection = connector.connect(
            host='localhost',
            user='gifty',
            password='Str0ngP@ssword123'
        )
        
        return connection
    except Error as e:
        print(f"Error connecting to MYSQL database: {e}")
        return None

def create_database(connection):
    """ Create the ALX_prodev database if it does not exist """
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    except Error as e:
        print(f"Error creating database: {e}")
    finally:
        cursor.close()

def connect_to_prodev():
    """ Connect to the ALX_prodev database """
    try:
        connection = connector.connect(
            host='localhost',
            user='gifty',
            password='Str0ngP@ssword123',
            database='ALX_prodev'
        )
        return connection
    except Error as e:
        print(f"Error connecting to ALX_prodev database: {e}")
        return None

def create_table(connection):
    """ Create the user_data table if it does not exist """
    create_table_query = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id CHAR(36) PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL,
        age DECIMAL NOT NULL,
        INDEX (user_id)
    )
    """
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
    except Error as e:
        print(f"Error creating table: {e}")
    finally:
        cursor.close()

def insert_data(connection, data):
    """ Insert data into the user_data table if it does not exist """
    try:
        cursor = connection.cursor()
        with open(data, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                user_id = str(uuid.uuid4())
                name = row['name']
                email = row['email']
                age = row['age']
                
                # Check if the record already exists
                cursor.execute("SELECT * FROM user_data WHERE email = %s", (email,))
                result = cursor.fetchone()
                
                if not result:
                    cursor.execute(
                        "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                        (user_id, name, email, age)
                    )
        connection.commit()
    except Error as e:
        print(f"Error inserting data: {e}")
    finally:
        cursor.close()