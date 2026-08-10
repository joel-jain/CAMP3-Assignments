class Account:
    def __init__(self, account_number,balance):
        self.account_number=account_number
        self.balance=balance

    def display_account(self):
        print(f"Account Number:{self.account_number}")
        print(f"Balance:{self.balance}")

    def deposit(amount):
        