class Account:
    def __init__(self, num):
        self.num = num
        self.balance = 0.0

    def checkBalance(self):
        return self.balance

    def credit(self, value):
        self.balance += value

    def debit(self, value):
        self.balance -= value

    def transfer(self, account, value):
        self.balance -= value
        account.balance += value


# account1 = Account(1)
# account1.credit(10)

# account2 = Account(2)
# account2.credit(5)

# print(account1.checkBalance())
# print(account2.checkBalance())

# account1.transfer(account2,5)

# print(account1.checkBalance())
# print(account2.checkBalance())


