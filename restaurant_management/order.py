# Order class
# This handles customer orders

from datetime import datetime


class Order:
    def __init__(self, id, table_num):
        self.id = id
        self.table_num = table_num
        self.items = []  # list to store items
        self.time = datetime.now()
        self.status = 'new'

    # add item to the order
    def add_item(self, item, qty=1):
        # check if item is available
        if item.available == False:
            print("Sorry, " + item.name + " is not available right now")
            return

        # check if item already in order
        found = False
        for i in range(len(self.items)):
            if self.items[i][0].id == item.id:
                # update quantity
                old_qty = self.items[i][1]
                new_qty = old_qty + qty
                self.items[i] = (item, new_qty)
                print("Updated " + item.name + " to " + str(new_qty))
                found = True
                break

        # if not found, add new
        if found == False:
            self.items.append((item, qty))
            print("Added " + str(qty) + "x " + item.name)

    # remove item from order
    def remove_item(self, item_id):
        for i in range(len(self.items)):
            if self.items[i][0].id == item_id:
                removed_item = self.items[i][0].name
                self.items.pop(i)
                print("Removed " + removed_item)
                return
        print("Item not found in order")

    # calculate subtotal
    def get_subtotal(self):
        total = 0
        for item, qty in self.items:
            total = total + (item.price * qty)
        return total

    # calculate total with tax
    def get_total(self):
        subtotal = self.get_subtotal()
        tax = subtotal * 0.19  # 19% tax
        total = subtotal + tax
        return total

    # change order status
    def change_status(self, new_status):
        self.status = new_status
        print("Order #" + str(self.id) + " is now " + new_status)

    # print the order
    def print_order(self):
        print("\n==================================================")
        print("Order #" + str(self.id) + " - Table " + str(self.table_num))
        print("Time: " + self.time.strftime('%Y-%m-%d %H:%M'))
        print("Status: " + self.status)
        print("==================================================")

        if len(self.items) == 0:
            print("No items yet")
        else:
            print("\nItems:")
            for item, qty in self.items:
                item_total = item.price * qty
                print("  " + str(qty) + "x " + item.name + " - €" + str(item.price) + " = €" + str(item_total))

            subtotal = self.get_subtotal()
            total = self.get_total()
            tax = total - subtotal

            print("--------------------------------------------------")
            print("Subtotal: €" + str(round(subtotal, 2)))
            print("Tax (19%): €" + str(round(tax, 2)))
            print("==================================================")
            print("TOTAL: €" + str(round(total, 2)))
            print("==================================================")