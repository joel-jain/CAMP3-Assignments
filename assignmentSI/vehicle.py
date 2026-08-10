class vehicle:
    def start(self):
        print("Vehicle Started")

class Car(vehicle):
    def drive(self):
        print("Car is Driving")

car1=Car()

car1.start()
car1.drive()