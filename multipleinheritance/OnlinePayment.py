
class OnlinePayment:
    def __init__(self, card_number):
        self.card_number = card_number

    def pay_online(self, amount):
        print(f"Paid {amount} online using card {self.card_number}")


class CashPayment:
    def __init__(self, cashier_name):
        self.cashier_name = cashier_name

    def pay_cash(self, amount):
        print(f"Paid {amount} in cash, collected by {self.cashier_name}")

class BillingModule(OnlinePayment, CashPayment):
    def __init__(self, card_number, cashier_name):
        OnlinePayment.__init__(self, card_number)
        CashPayment.__init__(self, cashier_name)

obj_billing = BillingModule("1234-5678-9999", "Ravi")

obj_billing.pay_online(1500)
obj_billing.pay_cash(500)
