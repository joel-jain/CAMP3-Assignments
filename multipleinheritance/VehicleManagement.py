class EngineDetails:
    def __init__(self, engine_type, horsepower):
        self.engine_type = engine_type
        self.horsepower = horsepower

    def display_engine_info(self):
        print(f"Engine: {self.engine_type}, HP: {self.horsepower}")


class SafetyFeatures:
    def __init__(self, airbags, abs_system):
        self.airbags = airbags
        self.abs_system = abs_system

    def display_safety_info(self):
        print(f"Airbags: {self.airbags}, ABS: {self.abs_system}")

class Car(EngineDetails, SafetyFeatures):
    def __init__(self, engine_type, horsepower, airbags, abs_system):
        EngineDetails.__init__(self, engine_type, horsepower)
        SafetyFeatures.__init__(self, airbags, abs_system)

#Creating object of Car
obj_car = Car("V6 Petrol", 250, 6, "Yes")

obj_car.display_engine_info()
obj_car.display_safety_info()
