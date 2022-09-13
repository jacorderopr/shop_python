"""Create a shop class where you pass all of the available cart in the shop
at the beginning of the program (maybe later add the option for the user to create
objects and add them to the shop)

Display a Menu where you can view the cart you have in your cart (using CashRegister class)
and also the ability to checkout

At the end of the program, you should pickle the created instances of Retail cart
so that way the Shop keeps expanding retail cart each time you start the program.
"""

from retailitem import RetailItem
from shop import Shop
class CashRegister:

    def __init__(self, cart=None):
        if cart is None:
            self.__cart = {}
        else:
            self.__cart = cart

    def purchase_item(self, *objects):# you could in theory pass multiple objects
        for obj in objects:

            self.__cart[obj.get_desc().lower()] = obj

    def remove_item(self, *objects_descriptions):

        for string_description in objects_descriptions:
            if string_description in self.__cart:
                del self.__cart[string_description]

            else:
                print(f"ERROR THERE IS NO {string_description} in the cart!")
                print(f"the cart is: {self.__cart}")

    def get_total(self):
        total = 0
        for item, object in self.__cart.items():
            total += object.get_price()

        return total

    def show_cart(self):

        if not self.__cart: # if self.__cart is empty
            print("\n\nYour cart is currently empty!\n")

        else: # if self.__cart has contents

            count = 1
            for item in self.__cart.values(): # this is now a dictionary
                print("-"*20+f"item #{count}"+"-"*20)
                item.introduce()
                count += 1
                print("\n")

    def clear(self):

        self.__cart = {}

    def checkout(self):
        total = self.get_total()

        for item in self.__cart.values():
            item.purchase_units(1)

        print(f"Total is: ${cr.get_total()}")
        cr.clear()

    def get_cart(self):
        return self.__cart


if __name__ == "__main__":
    cr = CashRegister()



    jacket = RetailItem("Jacket", 12, 59.95)
    jeans = RetailItem("Designer Jeans", 40, 34.65)
    shirt = RetailItem("Shirt", 20, 24.95)

    myshop = Shop([jacket, jeans, shirt]) # initializes with a list of objects

    cr.purchase_item(jacket)

    cr.purchase_item(jeans)
    cr.purchase_item(shirt)
    cr.show_cart()

    cr.checkout()

    print("\n\nAfter purchasing: ")

    cr.show_cart() # quitar esto!!!!!!!!!!!!

    myshop.show_inventory()
