# BankAccount class
class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self  

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self  

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self  

    def yield_interest(self):
        
        self.balance += self.balance * self.int_rate
        return self  


# Create 2 accounts
account1 = BankAccount(0.02, 100)   # 2% interest, $100 starting
account2 = BankAccount(0.03, 200)   # 3% interest, $200 starting


# First account: 3 deposits, 1 withdrawal, interest, display 
account1.deposit(50).deposit(25).deposit(25).withdraw(40).yield_interest().display_account_info()


# Second account: 2 deposits, 4 withdrawals, interest, display 
account2.deposit(100).deposit(50).withdraw(50).withdraw(50).withdraw(100).withdraw(500).yield_interest().display_account_info()