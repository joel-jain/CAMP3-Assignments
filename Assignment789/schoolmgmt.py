# from abc import ABC, abstractmethod
# class Person(ABC):
#     def __init__(self, T_id):
#         self._id=T_id
#     @abstractmethod
#     def get_role_details(self):
#         pass
#     def display_id(self):
#         print(f"T_id: {self._id}")
# class Teacher(Person):
#     def __init__(self, T_id,subject,department):
#         super().__init__(T_id)
#         self.subject=subject
#         self.department=department
#     def get_role_details(self):
#         print(f"Subject:{self.subject}")
#         print(f"Department:{self.department}")
# teacher = Teacher(101,"eng","language")
# teacher.display_id
# teacher.get_role_details

 class Teacher(Person):
    pass

teacher = Teacher(101,"eng","language")
