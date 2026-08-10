class Employee:
    def __init__(self,employee_id,employee_name):
        self.employee_id=employee_id
        self.employee_name=employee_name

    def display_employee(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Employee Name: {self.employee_name}")

class Manager(Employee):
    def __init__(self, employee_id, employee_name,department):
        super().__init__(employee_id, employee_name)
        self.department=department

    def display_manager(self):
        super().display_employee()
        print(f"Department:{self.department}")

manager1=Manager("E101", "Joel", 'HR')
manager1.display_manager()