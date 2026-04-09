# Main program for ramen shop management system
# Student project for B100 course

from restaurant import Restaurant
from menu_item import MenuItem
from table import Table


# main menu
def show_main_menu():
    print("\n==================================================")
    print("RAMEN SHOP MANAGEMENT SYSTEM")
    print("==================================================")
    print("1. Menu")
    print("2. Tables")
    print("3. Orders")
    print("4. Status")
    print("5. Save/Load")
    print("6. Exit")
    print("==================================================")


# menu stuff
def menu_section(restaurant):
    while True:
        print("\n--- MENU MANAGEMENT ---")
        print("1. View Menu")
        print("2. Add Item")
        print("3. Change Price")
        print("4. Toggle Available")
        print("5. Back")

        choice = input("Choose: ")

        if choice == '1':
            restaurant.show_menu()

        elif choice == '2':
            # add new item
            try:
                id = int(input("ID: "))
                name = input("Name: ")
                category = input("Category: ")
                price = float(input("Price: "))
                item = MenuItem(id, name, category, price)
                restaurant.add_menu_item(item)
            except ValueError:
                print("Error! Please enter valid numbers for ID and price")
            except Exception as e:
                print("Something went wrong: " + str(e))

        elif choice == '3':
            # change price
            try:
                id = int(input("Item ID: "))
                item = restaurant.get_item(id)
                if item != None:
                    price = float(input("New price: "))
                    if price < 0:
                        print("Error! Price cannot be negative")
                    else:
                        item.change_price(price)
            except ValueError:
                print("Error! Please enter valid numbers")

        elif choice == '4':
            # toggle availability
            try:
                id = int(input("Item ID: "))
                item = restaurant.get_item(id)
                if item != None:
                    item.toggle_available()
            except ValueError:
                print("Error! Please enter a valid ID number")

        elif choice == '5':
            break


# table stuff
def table_section(restaurant):
    while True:
        print("\n--- TABLE MANAGEMENT ---")
        print("1. View Tables")
        print("2. Add Table")
        print("3. Reserve Table")
        print("4. Free Table")
        print("5. Back")

        choice = input("Choose: ")

        if choice == '1':
            restaurant.show_tables()

        elif choice == '2':
            try:
                num = int(input("Table number: "))
                seats = int(input("Seats: "))
                if seats <= 0:
                    print("Error! Number of seats must be positive")
                else:
                    table = Table(num, seats)
                    restaurant.add_table(table)
            except ValueError:
                print("Error! Please enter valid numbers")

        elif choice == '3':
            try:
                num = int(input("Table number: "))
                if num in restaurant.tables:
                    restaurant.tables[num].reserve_table()
                else:
                    print("Table not found")
            except ValueError:
                print("Error! Please enter a valid table number")

        elif choice == '4':
            try:
                num = int(input("Table number: "))
                if num in restaurant.tables:
                    restaurant.tables[num].make_free()
                else:
                    print("Table not found")
            except ValueError:
                print("Error! Please enter a valid table number")

        elif choice == '5':
            break


# order stuff
def order_section(restaurant):
    while True:
        print("\n--- ORDER MANAGEMENT ---")
        print("1. New Order")
        print("2. Add Item to Order")
        print("3. View Order")
        print("4. Change Status")
        print("5. Close Order")
        print("6. Back")

        choice = input("Choose: ")

        if choice == '1':
            # create new order
            try:
                table_num = int(input("Table number: "))
                restaurant.create_order(table_num)
            except ValueError:
                print("Error! Please enter a valid table number")

        elif choice == '2':
            # add item to order
            try:
                order_id = int(input("Order ID: "))
                if order_id in restaurant.orders:
                    restaurant.show_menu()
                    item_id = int(input("Item ID: "))
                    qty = int(input("Quantity: "))

                    if qty <= 0:
                        print("Error! Quantity must be positive")
                    else:
                        item = restaurant.get_item(item_id)
                        if item != None:
                            restaurant.orders[order_id].add_item(item, qty)
                else:
                    print("Order not found")
            except ValueError:
                print("Error! Please enter valid numbers")

        elif choice == '3':
            # view order details
            try:
                order_id = int(input("Order ID: "))
                if order_id in restaurant.orders:
                    restaurant.orders[order_id].print_order()
                else:
                    print("Order not found")
            except ValueError:
                print("Error! Please enter a valid order ID")

        elif choice == '4':
            # change order status
            try:
                order_id = int(input("Order ID: "))
                if order_id in restaurant.orders:
                    status = input("New status: ")
                    restaurant.orders[order_id].change_status(status)
                else:
                    print("Order not found")
            except ValueError:
                print("Error! Please enter a valid order ID")

        elif choice == '5':
            # close order
            try:
                order_id = int(input("Order ID: "))
                restaurant.close_order(order_id)
            except ValueError:
                print("Error! Please enter a valid order ID")

        elif choice == '6':
            break


# setup ramen menu
def setup_ramen_menu(restaurant):
    print("\nSetting up menu...")

    # ramen bowls
    restaurant.add_menu_item(MenuItem(1, "Shoyu Ramen", "Ramen", 12.00))
    restaurant.add_menu_item(MenuItem(2, "Miso Ramen", "Ramen", 12.50))
    restaurant.add_menu_item(MenuItem(3, "Tonkotsu Ramen", "Ramen", 13.50))
    restaurant.add_menu_item(MenuItem(4, "Spicy Tan Tan Ramen", "Ramen", 13.00))
    restaurant.add_menu_item(MenuItem(5, "Vegetable Ramen", "Ramen", 11.00))

    # toppings
    restaurant.add_menu_item(MenuItem(6, "Extra Chashu Pork", "Topping", 3.50))
    restaurant.add_menu_item(MenuItem(7, "Soft Boiled Egg", "Topping", 2.00))
    restaurant.add_menu_item(MenuItem(8, "Extra Noodles", "Topping", 2.50))
    restaurant.add_menu_item(MenuItem(9, "Corn", "Topping", 1.50))
    restaurant.add_menu_item(MenuItem(10, "Seaweed", "Topping", 1.00))
    restaurant.add_menu_item(MenuItem(11, "Green Onion", "Topping", 1.00))
    restaurant.add_menu_item(MenuItem(12, "Bamboo Shoots", "Topping", 2.00))

    # soup/broth
    restaurant.add_menu_item(MenuItem(13, "Extra Rich Broth", "Soup", 2.00))
    restaurant.add_menu_item(MenuItem(14, "Spicy Broth", "Soup", 1.50))
    restaurant.add_menu_item(MenuItem(15, "Garlic Oil", "Soup", 1.00))

    # drinks
    restaurant.add_menu_item(MenuItem(16, "Green Tea", "Beverage", 2.50))
    restaurant.add_menu_item(MenuItem(17, "Iced Tea", "Beverage", 3.00))
    restaurant.add_menu_item(MenuItem(18, "Ramune Soda", "Beverage", 3.50))
    restaurant.add_menu_item(MenuItem(19, "Asahi Beer", "Beverage", 5.00))
    restaurant.add_menu_item(MenuItem(20, "Sake", "Beverage", 6.00))

    # add tables
    restaurant.add_table(Table(1, 4))
    restaurant.add_table(Table(2, 4))
    restaurant.add_table(Table(3, 4))
    restaurant.add_table(Table(4, 4))
    restaurant.add_table(Table(5, 2))
    restaurant.add_table(Table(6, 2))
    restaurant.add_table(Table(7, 2))

    print("Setup complete!")


# main function
def main():
    print("==================================================")
    print("WELCOME TO RAMEN SHOP SYSTEM")
    print("==================================================")

    name = input("\nShop name: ")
    if name == "":
        name = "Ichiraku Ramen House"

    restaurant = Restaurant(name)

    load = input("Load ramen menu? (yes/no): ")
    if load == 'yes':
        setup_ramen_menu(restaurant)

    # main loop
    running = True
    while running:
        try:
            show_main_menu()
            choice = input("\nChoose (1-6): ")

            if choice == '1':
                menu_section(restaurant)
            elif choice == '2':
                table_section(restaurant)
            elif choice == '3':
                order_section(restaurant)
            elif choice == '4':
                # show status
                print("\nShop: " + restaurant.name)
                print("Menu Items: " + str(len(restaurant.menu)))
                print("Tables: " + str(len(restaurant.tables)))
                print("Orders: " + str(len(restaurant.orders)))
            elif choice == '5':
                # save/load
                print("\n1. Load Menu")
                print("2. Save Menu")
                sub = input("Choose: ")
                if sub == '1':
                    restaurant.load_menu()
                elif sub == '2':
                    restaurant.save_menu()
            elif choice == '6':
                print("\nThank you! See you again!")
                running = False
            else:
                print("Please choose 1-6")

        except KeyboardInterrupt:
            print("\n\nProgram stopped by user")
            running = False
        except Exception as e:
            print("\nAn error occurred: " + str(e))
            print("Please try again")


# run the program
if __name__ == "__main__":
    main()