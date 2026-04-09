# Table class for managing tables in the shop

class Table:
    def __init__(self, number, seats):
        self.number = number
        self.seats = seats
        self.status = 'free'  # can be free, busy, or reserved
        self.order_id = None

    # make the table busy when customer sits
    def make_busy(self, order_id):
        self.status = 'busy'
        self.order_id = order_id
        print("Table " + str(self.number) + " is now busy")

    # free up the table when customer leaves
    def make_free(self):
        self.status = 'free'
        self.order_id = None
        print("Table " + str(self.number) + " is now free")

    # reserve a table
    def reserve_table(self):
        self.status = 'reserved'
        print("Table " + str(self.number) + " is reserved")

    # check if table is free
    def is_free(self):
        if self.status == 'free':
            return True
        else:
            return False

    # show table information
    def show_status(self):
        info = "Table " + str(self.number) + " (" + str(self.seats) + " seats) - " + self.status
        if self.order_id != None:
            info = info + " - Order #" + str(self.order_id)
        return info