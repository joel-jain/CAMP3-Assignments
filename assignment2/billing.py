class BillingSystem():
    def __init__(self,country_name,language,customer_id,billing_date,amount_outstanding):
        self.country_name=country_name
        self.language=language
        self.customer_id=customer_id
        self.billing_date=billing_date
        self.amount_outstanding=float(amount_outstanding)

    def display_details(self):
        print("--- Billing Details ---")
        print(f"Country: {self.country_name}")
        print(f"Language: {self.language}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Billing Date: {self.billing_date}")
        print("Amount Outstanding: ${self.amount_outstanding}")
        print("-----------------------")

objUSbill=BillingSystem("USA","English","C101","10-10-2026",500)
objJapanbill=BillingSystem("Japan","Japanese","C102","10-09-2026",500)

objUSbill.display_details()
objJapanbill.display_details()
