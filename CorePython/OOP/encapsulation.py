class Account:

    def __init__(self):
        self.__number = None
        self.__accountType = None
        self.__balance = 0.0

    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number = number

    def get_account_type(self):
        return self.__accountType

    def set_account_type(self, account_type):
        self.__accountType = account_type

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def deposit(self, amt):
        self.__balance += amt
        print("Total balance after deposit:", self.__balance)

    def withdrawal(self, amt):
        if amt <= self.__balance:
            self.__balance -= amt
            print("Total balance after withdrawal:", self.__balance)
        else:
            print("Insufficient funds")


kabir = Account()

kabir.set_number(1001)
kabir.set_account_type("Savings")
kabir.set_balance(5000)

print("Account Number:", kabir.get_number())
print("Account Type:", kabir.get_account_type())
print("Current Balance:", kabir.get_balance())

kabir.deposit(2000)
kabir.withdrawal(3000)

print("Final Balance:", kabir.get_balance())
