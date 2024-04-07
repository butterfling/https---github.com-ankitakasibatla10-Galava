import pymysql

# Database connection parameters
host = 'galava.cpic2wqcks8b.us-east-1.rds.amazonaws.com'
user = 'admin'
password = 'ankita2003'

# Connect without specifying a database
connection = pymysql.connect(host=host, user=user, passwd=password)

try:
    cursor = connection.cursor()
    # Create database if it does not exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS database")
    connection.select_db('database')

    # SQL statement to create a table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Institutions (
        InstitutionID VARCHAR(50) PRIMARY KEY,
        InstitutionName VARCHAR(255) NOT NULL,
        Location VARCHAR(255) NOT NULL,
        AccreditationStatus VARCHAR(50),
        EstablishmentYear INT,
        InstitutionType VARCHAR(50)
    );
    """

    print("Connected to the database.")

    # Execute the SQL statement to create the table
    cursor.execute(create_table_query)
    print("Table created successfully.")

    # Commit the changes
    connection.commit()

except pymysql.MySQLError as e:
    print(f"Error: {e}")

finally:
    # Close the database connection
    if connection:
        connection.close()
        print("Database connection closed.")
