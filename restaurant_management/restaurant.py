# Restaurant class
# Main class that controls everything

import csv
import os
from menu_item import MenuItem
from order import Order
from table import Table


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = {}  # dictionary for menu items
        self.tables = {}  # dictionary for tables
        self.orders = {}  # dictionary for orders
        self.order_counter = 1  # to generate order IDs

        # create data folder if it doesn't exist
        if not os.path.exists('data'):
            os.makedirs('data')

    # add menu item
    def add_menu_item(self, item):
        self.menu[item.id] = item
        print("Added " + item.name)

    # add table
    def add_table(self, table):
        self.tables[table.number] = table
        print("Added Table " + str(table.number))

    # create new order
    def create_order(self, table_num):
        # check if table exists
        if table_num not in self.tables:
            print("Table doesn't exist")
            return None

        table = self.tables[table_num]

        # check if table is free
        if table.is_free() == False:
            print("Table " + str(table_num) + " is not free")
            return None

        # create order
        order = Order(self.order_counter, table_num)
        self.orders[self.order_counter] = order
        table.make_busy(self.order_counter)

        print("Created Order #" + str(self.order_counter))
        self.order_counter = self.order_counter + 1
        return order

    # get menu item by id
    def get_item(self, item_id):
        if item_id in self.menu:
            return self.menu[item_id]
        else:
            print("Item not found")
            return None

    # show the menu
    def show_menu(self):
        print("\n============================================================")
        print(self.name.upper() + " - MENU")
        print("============================================================")

        if len(self.menu) == 0:
            print("No items in menu")
            return

        # organize by category
        categories = {}
        for item in self.menu.values():
            if item.category not in categories:
                categories[item.category] = []
            categories[item.category].append(item)

        # print each category
        for cat in sorted(categories.keys()):
            print("\n" + cat.upper())
            print("------------------------------------------------------------")
            items = categories[cat]
            items.sort(key=lambda x: x.id)
            for item in items:
                print("  " + item.show_info())

        print("============================================================")

    # show all tables
    def show_tables(self):
        print("\n============================================================")
        print("TABLES")
        print("============================================================")

        if len(self.tables) == 0:
            print("No tables")
            return

        for num in sorted(self.tables.keys()):
            print("  " + self.tables[num].show_status())

        print("============================================================")

    # close order
    def close_order(self, order_id):
        if order_id not in self.orders:
            print("Order not found")
            return

        order = self.orders[order_id]
        order.change_status('paid')

        # free the table
        if order.table_num in self.tables:
            self.tables[order.table_num].make_free()

        print("Order #" + str(order_id) + " closed")

    # save menu to csv file
    def save_menu(self, filename='menu.csv'):
        filepath = os.path.join('data', filename)

        file = open(filepath, 'w', newline='', encoding='utf-8')
        writer = csv.writer(file)

        # write header
        writer.writerow(['id', 'name', 'category', 'price', 'available'])

        # write items
        for item in self.menu.values():
            writer.writerow([item.id, item.name, item.category, item.price, item.available])

        file.close()
        print("Menu saved to " + filepath)

    # load menu from csv file
    def load_menu(self, filename='menu.csv'):
        filepath = os.path.join('data', filename)

        if not os.path.exists(filepath):
            print("File not found")
            return 0

        file = open(filepath, 'r', encoding='utf-8')
        reader = csv.DictReader(file)

        count = 0
        for row in reader:
            item = MenuItem(
                int(row['id']),
                row['name'],
                row['category'],
                float(row['price'])
            )
            if row['available'] == 'True':
                item.available = True
            else:
                item.available = False

            self.menu[item.id] = item
            count = count + 1

        file.close()
        print("Loaded " + str(count) + " items")
        return count