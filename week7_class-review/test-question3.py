# classes and objects
class BankAccount:
    balance = 0
    def __init__(self, deposit, withdraw):
        self.deposit = 0
        self.withdraw = 0

b = BankAccount(10)
b.deposit(25)
b.withdraw(1)
b.balance = int(b) + int(b.deposit) - int(b.withdraw)
print("The balance of the bank account is now " + str(b.balance))