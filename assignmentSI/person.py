# Problem 1: Person and Student
# Design a Python program to demonstrate single inheritance.
# Create a base class Person with attributes name and age, and methods
# to read and display these details.
# Derive a class Student from Person that adds attributes roll_number
# and marks.
# Implement methods to read and display complete student details.

class Person:
    def __init__(self,name,age): #parameterized constructor
        self.name=name
        self.age=age

    def display_person(self):
            print(f"Name: {self.name}")
            print(f"Age: {self.age}")

class Student(Person):
    def __init__(self,name, age, roll_number, marks):
        super().__init__(name, age)
        self.roll_number=roll_number
        self.marks=marks

    def display_student(self):
        super().display_person()
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")
student1 = Student("Joel",22,101,95)
student1.display_student()
