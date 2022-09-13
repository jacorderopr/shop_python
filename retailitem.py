class RetailItem:
    inventory = []
    def __init__(self, desc, units, price):

        self.__desc = desc
        self.__units = units
        self.__price = price
        RetailItem.inventory.append(self)
    def get_desc(self):
        return self.__desc

    def get_units(self):
        return self.__units

    def get_price(self):
        return float(self.__price)

    def purchase_units(self, to_purchase):

        self.__units -= to_purchase

    def introduce(self):
        print(f"Description: {self.get_desc()}")
        print(f"units: {self.get_units()}")
        print(f"Price: ${self.get_price()}")
        return self.__desc
