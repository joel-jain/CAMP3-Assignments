class Employee:
    name = ""
    base_salary = 0
    years_of_service = 0

    def calculate_bonus(self):
       bonus=self.base_salary * 0.05 * self.years_of_service
       return bonus

    def total_salary(self):
        bonus = self.calculate_bonus()
        total = self.base_salary + bonus
        return total
    
    def display(self):
        print("Employee Name :", self.name)
        print("Base Salary:", self.base_salary)
        print("Years of Service :", self.years_of_service)
        print("Bonus:", self.calculate_bonus())
        print("Total Salary :", self.total_salary())

# Create Object
objE1 = Employee()

# Assign values manually
objE1.name = "AD"
objE1.base_salary = 55000
objE1.years_of_service = 2

print("-----------------------------------")
# Display Details
objE1.display()

objE1.calculate_bonus()

print("-----------------------------------")

objE1.total_salary()

print(" after bonus: \n")
# Display Again
objE1.display()