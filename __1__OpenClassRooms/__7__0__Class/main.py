class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi {self.name}")

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major
    def greetings(self):
        print(f"Hi student {self.name} your class is {self.major}")

student = Student("Thomas", 30, "physics")
person = Person("BOUTIN", 25)

print(student.greetings())