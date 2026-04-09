# Menu Item class
# This is for the items in my ramen shop

class MenuItem:
    def __init__(self, id, name, category, price):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.available = True

    # show the item info
    def show_info(self):
        if self.available:
            status = "Available"
        else:
            status = "Not Available"

        info = "[" + str(self.id) + "] " + self.name + " - €" + str(self.price)
        info = info + " (" + self.category + ") - " + status
        return info

    # change the price
    def change_price(self, new_price):
        self.price = new_price
        print("Price updated to €" + str(self.price))

    # make available or not available
    def toggle_available(self):
        if self.available == True:
            self.available = False
            print(self.name + " is now unavailable")
        else:
            self.available = True
            print(self.name + " is now available")

    # calculate total for multiple items
    def get_total(self, qty):
        total = self.price * qty
        return total