class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def printname(self):
        print(self.first_name, self.last_name)

class Student(Person):
    def __init__(self, first_name, last_name, email, grad_year):
        super().__init__(first_name, last_name)
        self.email = email
        self.grad_year = grad_year

    def details(self):
        print("Welcome ", self.first_name, self.last_name, " with email: ", self.email, " to the class of ", self.grad_year) 


x = Student("Jack", "Richards", "student@email.com", 2024)
x.printname()
x.details()
