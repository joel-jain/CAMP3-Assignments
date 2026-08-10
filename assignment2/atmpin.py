class Verify:
    # Class variable
    y= 1234      

    def __init__(self):
        print("Welcome to XYZ company")
        pin= int(input("Enter your PIN: "))

        if pin==Verify.y:
            print("Access granted")
        else:
            print("Access denied")
objpin = Verify()