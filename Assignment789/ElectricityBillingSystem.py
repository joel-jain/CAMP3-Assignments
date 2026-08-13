class ElectricityBill:
    def calculate_bill(self, units):
        return units*5

class DomesticBill(ElectricityBill):
    def calculate_bill(self, units):
        if units<=100:
             print("bill_amount= ")
        else:
            cost=500+(units-100)*3 
            print("cost=",cost)

class CommercialBill(ElectricityBill):
    def calculatebill(self,units):
        cost=(units*8)
        fcost=cost*(cost*0.1)
        print("cost=",fcost)

objbill=ElectricityBill()
objdombill=DomesticBill()
objcombill=CommercialBill()

print("electricity bill:",objbill.calculatebill(150))
print("domestic bill:",objdombill.calculatebill(150))
print("commercial bill:",objcombill.calculatebill(150))