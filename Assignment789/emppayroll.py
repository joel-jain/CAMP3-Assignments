from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, basic_salary):
        self._basic_salary = basic_salary
    @abstractmethod
    def calculate_salary(self):
        pass
    def display_basic_salary(self):
        print(f"Basic Salary: {self._basic_salary}")
class FullTimeEmployee(Employee):
    def __init__(self, basic_salary):
        super().__init__(basic_salary)
    def calculate_salary(self):
        hra=0.20*self._basic_salary
        da=0.10*self._basic_salary
        total_salary=self._basic_salary+hra+da
        return total_salary
employee = FullTimeEmployee(50000)
employee.display_basic_salary()
print(f"Total Salary: {employee.calculate_salary()}")
