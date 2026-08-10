#Base Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person): 
    def __init__(self, name, age, roll_number, marks):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.marks = marks

    def display_student_info(self):
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")

class Result(Student): 
    def __init__(self, name, age, roll_number, marks):
        super().__init__(name, age, roll_number, marks)

    def display_result(self):
        self.display_person_info()
        self.display_student_info()
        if self.marks >= 40:
            print("Status: Pass")
        else:
            print("Status: Fail")

obj_result = Result("Anu", 20, 101, 85)
obj_result.display_result()
