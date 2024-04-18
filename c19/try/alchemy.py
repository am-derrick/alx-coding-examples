from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Configure the SQLAlchemy database URI using create_engine
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "password", "new_db"), pool_pre_ping=True)
Base = declarative_base()

# Define a SQLAlchemy model for the "employees" table
class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    age = Column(Integer)

# Create all tables based on the defined models
Base.metadata.create_all(engine)

# Create a sessionmaker to manage sessions with the database
Session = sessionmaker(bind=engine)
session = Session()

employees_data = [
    {'name': 'Brian Doe', 'email': 'brian@example.com', 'age': 30},
    {'name': 'Jane Doe', 'email': 'jane@example.com', 'age': 25},
    {'name': 'Alice Smith', 'email': 'alice@example.com', 'age': 35}
]

# Example usage: Inserting data into the "employees" table
for emp_data in employees_data:
    new_employee = Employee(name=emp_data['name'], email=emp_data['email'], age=emp_data['age'])
    session.add(new_employee)

session.commit()

# Querying data from the "employees" table
employees = session.query(Employee).all()
for employee in employees:
    print(employee.id, employee.name, employee.email, employee.age)

# Close the session
session.close()

