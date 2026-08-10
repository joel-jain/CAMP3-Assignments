class StudentResult:
    def __init__(self,student_name,roll_number,marks):
        self.student_name=student_name
        self.roll_number=roll_number
        self.marks=marks

    def calculate_result(self):
        return "Pass" if self.marks>=60 else "Fail"


    def calculate_grade(self):
        if self.marks >=90:
            return "A"
        elif self.marks >=75:
            return "B"
        elif self.marks >=60:
            return "C"
        else:
            return "D"

    def display(self):
        print(f"Student_Name:{self.student_name}")
        print(f"Roll no: {self.roll_number}")
        print(f"Marks:{self.marks}")
        print(f"Result:{self.calculate_result()}")
        print(f"Grade:{self.calculate_grade()}")

objStudentResult1=StudentResult("Joel",30,88)
objStudentResult1.display()