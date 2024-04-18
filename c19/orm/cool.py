import MySQLdb

connection = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="password", db="cool_db", charset="utf8")
cursor = connection.cursor()

create_table = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INT
    )
"""

insert_data = """
INSERT INTO users (username, email, age) VALUES
('john', 'john@doe.com', 20),
('jane', 'jane@doe.com', 38),
('jack', 'jack@jack.com', 67)
"""

cursor.execute(create_table)
cursor.execute(insert_data)

connection.commit()

select_data = "SELECT * FROM users"

cursor.execute(select_data)

users = cursor.fetchall()

for user in users:
    print(user)

cursor.close()
connection.close()
