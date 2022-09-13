class Shop:

    def __init__(self, items= None): # the items should be retailItems objects
        if items is None:
            self.__shopitems = []
        else:
            self.__shopitems = items

    def add_to_shop(self, item):

        self.__shopitems.append(item)

    # the remove_item function will remove an item from the STORE INVENTORY NOT from the user's cart!
    def remove_item(self, item): # only call this function if you are sure that it is inside the list
    # RetailItem objects will be inside the list!!! NO STRINGS ARE CONTAINED IN LISTS

        self.__shopitems.pop(self.__shopitems.index(item))

    def show_inventory(self):
        print("Items in the Shop Invetory: ")
        count = 1
        for item in self.__shopitems: # item will be an object of the RetailItems class
            print("-"*20+f"Inventory item #{count}"+"-"*20)
            item.introduce()
            count += 1


    def get_items(self):
        return self.__shopitems
