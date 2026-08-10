
class AcademicDetails:
    def __init__(self, course, grade):
        self.course = course
        self.grade = grade

    def display_academic_info(self):
        print(f"Course: {self.course}, Grade: {self.grade}")


class PersonalDetails:
    def __init__(self, student_name, dob):
        self.student_name = student_name
        self.dob = dob

    def display_personal_info(self):
        print(f"Name: {self.student_name}, DOB: {self.dob}")

class StudentProfile(AcademicDetails, PersonalDetails):
    def __init__(self, course, grade, student_name, dob):
        AcademicDetails.__init__(self, course, grade)
        PersonalDetails.__init__(self, student_name, dob)

    def display_full_profile(self):
        self.display_personal_info()
        self.display_academic_info()

obj_student = StudentProfile("Computer Science", "A", "Meena", "12-Jan-2003")
obj_student.display_full_profile()
