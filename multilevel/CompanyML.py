class Company:
    def __init__(self, company_name):
        self.company_name = company_name

    def display_company_info(self):
        print(f"Company Name: {self.company_name}")

class Employee(Company):
    def __init__(self, company_name, employee_id, employee_name):
        super().__init__(company_name)
        self.employee_id = employee_id
        self.employee_name = employee_name

    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Employee Name: {self.employee_name}")

class Salary(Employee):
    def __init__(self, company_name, employee_id, employee_name, basic_salary):
        super().__init__(company_name, employee_id, employee_name)
        self.basic_salary = basic_salary

    def calculate_salary(self):
        bonus = self.basic_salary * 0.10
        total_salary = self.basic_salary + bonus
        print(f"Basic Salary: {self.basic_salary}")
        print(f"Bonus: {bonus}")
        print(f"Total Salary: {total_salary}")

    def display_all_details(self):
        self.display_company_info()
        self.display_employee_info()
        self.calculate_salary()

obj_salary = Salary("TechCorp", "E101", "Ravi", 50000)
obj_salary.display_all_details()
