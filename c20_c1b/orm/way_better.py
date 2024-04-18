from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "password", "way_better_db"), pool_pre_ping=True)
Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(70), nullable=False)
    age = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

employees_data = [
        {'name' : 'Bob', 'email': 'Bob@Bob.com', 'age': 23},
        {'name' : 'Aisha', 'email': 'Aisha@Bob.com', 'age': 27},
        {'name' : 'Becca', 'email': 'Becca@Bob.com', 'age': 23},
        {'name' : 'Susan', 'email': 'Susan@Bob.com', 'age': 21}
]

for employee_data in employees_data:
    new_employee = Employee(name=employee_data['name'], email=employee_data['email'], age=employee_data['age'])
    session.add(new_employee)

session.commit()

employees= session.query(Employee).all()
for employee in employees:
    print(employee.id, employee.name, employee.email, employee.age)

session.close()
