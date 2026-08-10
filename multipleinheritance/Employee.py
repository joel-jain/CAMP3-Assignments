
class PersonalInfo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_personal_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class JobInfo:
    def __init__(self, designation, salary):
        self.designation = designation
        self.salary = salary

    def display_job_info(self):
        print(f"Designation: {self.designation}, Salary: {self.salary}")

class Employee(PersonalInfo, JobInfo):
    def __init__(self, name, age, designation, salary):
        PersonalInfo.__init__(self, name, age)
        JobInfo.__init__(self, designation, salary)

    def display_employee_info(self):
        self.display_personal_info()
        self.display_job_info()

#Creating object
obj_employee = Employee("Anu", 28, "Software Engineer", 55000)

obj_employee.display_employee_info()
