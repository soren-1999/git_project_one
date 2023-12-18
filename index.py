#Question 1:

class Account:
    def __init__(self, balance, number):
        self.balance = balance
        self.number = number
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(amount)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(-amount)
        else:
            print("Insufficient!")

    def display_balance(self):
        print(f"Balance: {self.balance:.2f} : {self.number}")

    def __str__(self):
        return f"Balance: {self.balance:.2f} : {self.number}"

acc = Account(1000,12345)
acc.deposit(500)
acc.withdraw(200)
acc.display_balance()