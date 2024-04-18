import MySQLdb

# Establish a connection to the MySQL database
connection = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="password", db="my_db", charset="utf8")

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Define SQL queries to create a table and insert data
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INT
)
"""

insert_data_query = """
INSERT INTO users (username, email, age) VALUES 
('john_doe', 'john@example.com', 30),
('jane_doe', 'jane@example.com', 25),
('alice_smith', 'alice@example.com', 35)
"""

# Execute the SQL queries to create the table and insert data
cursor.execute(create_table_query)
cursor.execute(insert_data_query)

# Commit the changes to the database
connection.commit()

# Define a SQL query to fetch all users from the table
select_query = "SELECT * FROM users"

# Execute the SQL query to fetch all users
cursor.execute(select_query)

# Fetch all rows from the result set
users = cursor.fetchall()

# Print the fetched users
for user in users:
    print(user)

# Close the cursor and connection
cursor.close()
connection.close()

