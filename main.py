print("----------------------------E-Commerce Store ----------------------")
print("----------------------------Menu ---------------------")
class Product():
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock

class Inventory():

    def __init__(self):
        self.products = {
            
    }

    def add_product (self,Product):
        self.products[Product.name] = Product

    def show_product(self):
        print("------------This is the inventory----------------")
        for key,value in self.products.items():
            print(value.name,value.price,value.stock)

    def remove_product(self,product_name):
            if product_name in self.products:
                del self.products[product_name]

class Card():
    def __init__(self,inventory):
        self.inventory = inventory
        self.products = {

        }

    def add_product(self,Product,quantity):
        try:
            if Product.name in self.inventory.products and Product.name not in self.products:
                if quantity <= self.inventory.products[Product.name].stock and quantity > 0:
                    self.products[Product.name] = [Product.price,quantity]
                    self.inventory.products[Product.name].stock -= quantity
                else:
                    print("Sorry sir, at this moment we don't have the enough stock we you want.")
            elif Product.name in self.inventory.products and Product.name in self.products:
                if quantity <= self.inventory.products[Product.name].stock and quantity > 0:
                    self.products[Product.name][1] += quantity
                    self.inventory.products[Product.name].stock -= quantity
                else:
                    print("Sorry sir, at this moment we don't have the enough stock we you want.")
            else:
                print("Sorry, this product is not available in inventory.")
        except AttributeError:
            print("Sorry, this product is not available in inventory.")
            
                
    def remove_product(self,Product_name):
        if Product_name in self.products:
            self.inventory.products[Product_name].stock += self.products[Product_name][1]
            del self.products[Product_name]

    def show_card(self):
        print("---------------------This is the Card----------------------")
        for key,value in self.products.items():
            print(key,value[0],value[1])

    def calculate_total(self):
        print("--------------The is total ----------------")
        total = 0
        for key,value in self.products.items():
            total = (value[0] * value[1]) + total
        print(f"The final cost after total is {total}")



def main():
    while True:
        user_input = input("1: browser product \n2: add product to card \n3: remove product from Card \n4: View Card \n5: Calculate total \n6: Exit \nSelect an option :")
        if user_input == "1":
            inventory.show_product()
        elif user_input == "2":
            product_name = input("Enter the Product name:")
            if product_name in inventory.products:
                selected_product = inventory.products[product_name]
                while True:
                    try:
                        quantity = int(input("Enter the quantity:"))
                        if quantity > 0:
                            break
                        else:
                            print("Quantity must be greater then 0")
                    except ValueError:
                        print("Invalid input try again ")
                mycard.add_product(selected_product,quantity)
            else:
                print("Product not have in inventory ")
        elif user_input == "3":
            product_name = input("Enter the product name:")
            mycard.remove_product(product_name)
        elif user_input == "4":
            mycard.show_card()
        elif user_input == "5":
            mycard.calculate_total()
        elif user_input == "6":
            print("The program is closed")
            break
        else:
            print("Invalid Input")



inventory = Inventory()
laptop = Product("laptop",50000,5)
mouse = Product("Mouse",2000,10)

inventory.add_product(laptop)
inventory.add_product(mouse)
mycard = Card(inventory)


main()

