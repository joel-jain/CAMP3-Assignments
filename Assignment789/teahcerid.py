from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, person_id):
        self._id = person_id

    @abstractmethod
    def get_role_details(self):
        pass

    def display_id(self):
        print(f"Teacher ID: {self._id}")


class Teacher(Person):
    def __init__(self, person_id, subject, department):
        super().__init__(person_id)
        self.subject = subject
        self.department = department

    def get_role_details(self):
        print(f"Subject: {self.subject}")
        print(f"Department: {self.department}")


teacher = Teacher(101, "Mathematics", "Science")
teacher.display_id()
teacher.get_role_details()
