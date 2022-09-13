"""work on the function remove_from_cart_portal

if length of cart is 1 (already coded)
the else statement is missing
must code parts show below:

'print("Enter 's' to remove a SINGLE item from your cart")
print("Enter 'm' to remove MULTIPLE items from your cart")
print("Enter 'c' to CLEAR your cart")'

try to make the program work even if they do not have a shopInventory.txt text file (write to the file in case it does not exist)"""

from retailitem import RetailItem
from Cashregister import CashRegister
from shop import Shop
import pickle

FILE = 'shopInventory.txt'
def display_portal_name(name):
    print("-"*20+name.upper()+"-"*20)

def display_main_menu():
    display_portal_name("Menu")
    print("Enter 'a' to add a new object to the store")
    print("Enter 'r' to remove item from the store")
    print("Enter 's' to shop at the store")
    print("Enter 'v' to view inventory of the store")


def display_shop_menu():
    display_portal_name("Shop")
    print("Enter 'd' to display inventory")
    print("Enter 'a' to add an item to your cart")
    print("Enter 'r' to remove an item from your cart")
    print("Enter 'c' to see your cart's contents")
    print("Enter 'b' to go Back to main menu")
# def __init__(self, desc, units, price):
def gather_obj_data():
    desc = input("Enter object's description: ")
    units = int(input(f"Enter the amount of units available of {desc}: "))
    price = float(input(f"Enter the price of a {desc}: $").replace("$", ""))

    obj = RetailItem(desc, units, price)
    return obj

def remove_from_shop(shop_obj):
    retail_object_list = shop_obj.get_items()

    available = [obj.get_desc().lower() for obj in retail_object_list]

    print(f"Available items are: {available}")
    to_remove = input("Enter the name of the item you would like to remove: ").lower()

    for obj in shop_obj.get_items():
        if obj.get_desc().lower() == to_remove:
            shop_obj.remove_item(obj)
            print(f"Just removed {obj.introduce()}")
            break
    else:
        print(f"{to_remove} was not found in the shop! Shop inventory remains unchanged...")

def display_remove_options():
    print("Enter 's' to remove a SINGLE item from your cart")
    print("Enter 'm' to remove MULTIPLE items from your cart")
    print("Enter 'c' to CLEAR your cart")


def remove_from_cart_portal(cash_register):
    cart = cash_register.get_cart()

    if len(cart) == 0:
        print("You cannot enter the Remove portal since your cart is empty!")
    else:
        available_objects = cash_register.get_cart() # will return a dictionary with the strings as keys and objects as values
        available = list(available_objects.keys())
        print(f"THE TEST DICTIONARY IS: {available_objects}")
        print(f"The available items in your cart are: {available}")

        if len(available) == 1: # if there is only one item, ask the user to confirm removal of this item
            print(f"\n\nThere is only 1 item in your cart. Would you like to remove it? (Item is: {available[0]})")
            option_remove = input("Enter 'y' to remove (anything else to cancel): ").lower().strip()

            if option_remove == "y":
                cash_register.remove_item(available[0]) # remove the only item
                print(f"\nThe item : '{available[0]}' has been removed from your cart!")
            else:
                print(f"No item will be removed from your cart.\nYour cart remains with: {available[0]}")
        else: # if there is more than one item then make the user pick which one to remove
            display_remove_options()
            # print("Enter 's' to remove a SINGLE item from your cart")
            # print("Enter 'm' to remove MULTIPLE items from your cart")
            # print("Enter 'c' to CLEAR your cart")
            option_remove = input("\nEnter your option > ")

            if option_remove == 's':
                pass
            elif option_remove == 'm':
                pass
            elif option_remove == 'c':
                pass # clear the cart
    # do not let the user enter if they have no items in their cart


# there is a main menu and a shop menu (shop menu is named shop_main)
def main_menu():
    # creating the main loop first
    try:
        infile = open(FILE, 'rb')
        ret = pickle.load(infile)
        print(f"Objects found on {FILE} proceeding to use them!")
        myShop = Shop(ret)
        infile.close()



    except EOFError:
        print(f"No objects were found on: {FILE}\nCreating own objects...")
        jacket = RetailItem("Jacket", 12, 59.95)
        jeans = RetailItem("Designer Jeans", 40, 34.65)
        shirt = RetailItem("Shirt", 20, 24.95)

        myShop = Shop([jacket, jeans, shirt])
    finally: # always create the same CashRegister object no matter what
        cr = CashRegister() # this will be the same cash register object that will be used accross the program
        # cr stores a dictionary!!! not a list:
        # dictionary format: {desc : object} or {"jacket": RetailItem object reference}



    while True:
        display_main_menu()
        option = input("Enter your option\n>")

        if option == 'a':
            new_obj = gather_obj_data() # this will return a RetailItem object

            myShop.add_to_shop(new_obj)
            print(f"Successfully added the following object to the Store!")
            new_obj.introduce()
            print("-"*35)
        elif option == 'v':
            myShop.show_inventory() # iterates over list of objects and it calls the introduce() method of the object

        elif option == 'r':
            remove_from_shop(myShop) # the parameter must be a Shop object

        elif option == 's':
            print("Transporting to Shop Portal...")
            val = shop_main(myShop, cr) # return -1 if you want to break out of the loop from the shop portal
            if val == -1:
                print(f"Val was {val} so we break out of the entire program")
                break
            elif val == "done":
                print("Returning to main menu...")

        print("\n\n\n"+ "-"*50)
        print("TESTING INVENTORY OF SHOP: ")
        myShop.show_inventory()
        print("-"*50)
        print("\n\n")


    outfile = open(FILE, 'wb') # need to open in binary write mode
    pickle.dump(myShop.get_items(), outfile) # dumping the list of objects using Data Serialization and Pickle library
    # this way, if you create new objects you will be able to pick up where you left off last time
    outfile.close()

# You access the shop_main function when you enter 's' in the main_menu()
def shop_main(shop_obj, cash_register):

    while True:
        display_shop_menu()
        option = input("\nEnter your option: ")
        if option == 'd': # display the inventory of the store
            shop_obj.show_inventory()
        elif option == 'a':
            available = {obj.get_desc().lower():obj for obj in shop_obj.get_items()} # this line access the list of retail OBJECTS stored inside the shop instance
            # and says that: "for every object, get their object name in lower case letter and make that a key whose value is the object it references"
            print(f"Available items in shop are: {available}\n\n{list(available.keys())}")

            to_add = input("Enter the item you wish to add to your cart: ").lower()
            if to_add in available:
                cash_register.purchase_item(available[to_add])
                print("Your cart now is: ")
                cash_register.show_cart()
                print("-"*50)
            else:
                print(f"{to_add} is not available in the shop!")

        elif option == 'r':
            remove_from_cart_portal(cash_register)
        elif option == 'c':
            cash_register.show_cart()

        elif option == 'b':
            return 'done'
        elif option == 'exit' or option == 'x':
            return -1



if __name__ == "__main__":
    main_menu()
