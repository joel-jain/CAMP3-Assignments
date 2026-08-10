class Calling:
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def make_call(self, to_number):
        print(f"Calling {to_number} from {self.phone_number}")

class Camera:
    def __init__(self, megapixels):
        self.megapixels = megapixels

    def take_photo(self):
        print(f"Photo taken with {self.megapixels}MP camera")

class SmartPhone(Calling, Camera):
    def __init__(self, phone_number, megapixels):
        Calling.__init__(self, phone_number)
        Camera.__init__(self, megapixels)

#Creating object
obj_phone = SmartPhone("9876543210", 108)

obj_phone.make_call("9123456789")
obj_phone.take_photo()
