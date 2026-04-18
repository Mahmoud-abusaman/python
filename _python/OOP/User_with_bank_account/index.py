
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





# User class
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.USDaccount = BankAccount()  
        self.JODaccount = BankAccount()  
        self.ISaccount = BankAccount()
        self.defultAccount="USD"

    def make_deposit(self, amount,account):
        depositToAccount=None
        if account=="USD":
            depositToAccount=self.USDaccount
        elif account=="JOD":
            depositToAccount=self.JODaccount
        elif account=="IS":
            depositToAccount=self.ISaccount
        else:
            print("Invalid account type. Please choose 'USD', 'JOD', or 'IS'.")
            return self
        depositToAccount.deposit(amount)
        return self

    def make_withdrawal(self, amount, account):
        withdrawFromAccount=None
        if account=="USD":
            withdrawFromAccount=self.USDaccount
        elif account=="JOD":
            withdrawFromAccount=self.JODaccount
        elif account=="IS":
            withdrawFromAccount=self.ISaccount
        else:
            print("Invalid account type. Please choose 'USD', 'JOD', or 'IS'.")
            return self
        withdrawFromAccount.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"""User: {self.name}, Balance: 
              USD: ${self.USDaccount.balance},
              JOD: ${self.JODaccount.balance},
              IS: ${self.ISaccount.balance}""")
        return self


# Create users
user1 = User("Alice", "alice@email.com")
user2 = User("Bob", "bob@email.com")

# Test functionality
user1.make_deposit(100, "USD").make_deposit(50, "USD").make_withdrawal(30, "USD").display_user_balance()

user2.make_deposit(200, "USD").make_withdrawal(50, "USD").display_user_balance()