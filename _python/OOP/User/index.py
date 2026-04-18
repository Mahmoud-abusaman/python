# User class
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


# Create 3 users
user1 = User("Mah", "Mah@email.com")
user2 = User("khaled", "khaled@email.com")
user3 = User("shatha", "shatha@email.com")

# First user: 3 deposits, 1 withdrawal
user1.make_deposit(100)
user1.make_deposit(50)
user1.make_deposit(25)
user1.make_withdrawal(30)
user1.display_user_balance()

# Second user: 2 deposits, 2 withdrawals
user2.make_deposit(200)
user2.make_deposit(100)
user2.make_withdrawal(50)
user2.make_withdrawal(25)
user2.display_user_balance()

# Third user: 1 deposit, 3 withdrawals
user3.make_deposit(300)
user3.make_withdrawal(50)
user3.make_withdrawal(50)
user3.make_withdrawal(25)
user3.display_user_balance()

#  transfer money from user1 to user3
user1.transfer_money(user3, 50)

# Display balances after transfer
user1.display_user_balance()
user3.display_user_balance()