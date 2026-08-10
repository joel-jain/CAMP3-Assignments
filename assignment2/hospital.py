class Patient():
    #class variable
    hospital_name="CityCare hospital"

    def __init__(self,patient_id,name,age,admitted_days,daily_charge):
        self.patient_id=patient_id
        self.name=name
        self.age=age
        self.admitted_days=admitted_days
        self.daily_charge=daily_charge
    def display_details(self):
        print("\nPatient Details")
        print("Hospital:", Patient.hospital_name)
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Admitted Days:", self.admitted_days)
        print("Daily Charge:", self.daily_charge)

    def calculate_bill(self):
        return self.admitted_days*self.daily_charge
    
    @classmethod
    def change_hospital_name(cls, new_name):
        cls.hospital_name=new_name

    @staticmethod
    def is_senior(age):
        return age >= 60

def __str__(self):
    return (
        f"Hospital: {Patient.hospital_name}\n"
        f"Patient ID: {self.patient_id}\n"
        f"Name: {self.name}\n"
        f"Age: {self.age}\n"
        f"Admitted Days: {self.admitted_days}\n"
        f"Daily Charge: {self.daily_charge}"
    )    
patient1 = Patient("P101","Alice",29,4,200)
patient2 = Patient("P102","Bob",45,6,200)

patient1.display_details()
patient2.display_details() 