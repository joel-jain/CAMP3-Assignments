from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass
class CreditCardPayment(Payment):
    def make_payment(self, amount):
        print("Payment of", amount, "made using Credit Card")    
class UPIPayment(Payment):
    def make_payment(self, amount):
        print("Payment of", amount, "made using UPI")
class NetBankingPayment(Payment):
    def make_payment(self, amount):
        print("Payment of", amount, "made using Net Banking")
card=CreditCardPayment()
upi=UPIPayment()
net=NetBankingPayment()

card.make_payment(500)
upi.make_payment(1000)
net.make_payment(2000)