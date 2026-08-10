class Product:
    product_name = ""
    price = 0.0
    stock = 0
    def add_stock(self, quantity):
        if quantity > 0:
            self.stock = self.stock+quantity
            print("Stock added successfully")
        else:
            print("Invalid quantity")

    def sell(self, quantity):
        if quantity <= self.stock:
            self.stock = self.stock-quantity
            print("Product sold")
            print("Stock left:", self.stock)
        else:
            print("No stock left")


    def display(self):
        print("Product Name :",self.product_name)
        print("Price :",self.price)
        print("Stock :",self.stock)


# Create Object
objp1 = Product()
objp2= Product()
objp3= Product()

objp1.product_name = "Laptop"
objp1.price = 55000
objp1.stock = 20

objp2.product_name = "keyboard"
objp2.price = 5000
objp2.stock = 20

objp3.product_name = "Mouse"
objp3.price = 2000
objp3.stock = 20

print("-----------------------------------")
# Display Details
objp1.display()
objp2.display()
objp3.display()
print("-----------------------------------")

# Sell Product
objp1.sell(20)
objp2.sell(20)
objp3.sell(20)
print("-----------------------------------")

# Add Stock
objp1.add_stock(0)
objp2.add_stock(1)
objp3.add_stock(1)
print("-----------------------------------")


print(" AFTER SELL AND RESTOCK: \n")
# Display Again
objp1.display()
objp2.display()
objp3.display()