class bankaccount:
    def __init__(self):
        self.__balance = 0  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount")

    def get_balance(self):
        return self.__balance
a=bankaccount()
a.deposit(1000)
a.withdraw(500)
print(a.get_balance())