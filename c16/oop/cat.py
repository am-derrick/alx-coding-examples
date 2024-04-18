class Cat:
    species = "Felidae"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"My cat is {self.name} and is {self.age} years."

    def sound(self):
        print(f"{self.name} says moew.")

    def spin(self, num):
        print(f"{self.name} spins {num} times.")


myCat = Cat("Dexter", 7)
myCat.sound()
myCat.spin(10)
print(myCat)
