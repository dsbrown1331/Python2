class BankAccount:
    balance = 0
    def __init__(self, name, rate):
        print("Initializing object")
        self.owner = name
        self.rate = rate

    def print_owner(self):
        print(self.owner)

    def set_owner(self, name):
        self.owner = name

    def deposit(self, amount):
        self.balance += amount

    def print_balance(self):
        print("Balance: {}".format(
                        self.balance))

name = "Daniel S. Brown"
rate = 0.05
my_checking = BankAccount(name, 0.01)
print(my_checking.owner)
my_checking.print_balance()
my_checking.deposit(351)
my_checking.print_balance()
