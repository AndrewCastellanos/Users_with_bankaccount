from bankaccount import BankAccount


class User:
    def __init__(self, name, account_balance):
        self.name = name
        self.account = BankAccount (int_rate=.02, balance=0)

    def make_deposit(self, amount):
        self.account += amount
        return self

    def make_withdraw(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        return self.display_user_balance

andrew=User(name ='andrew', account_balance = '120')

sam=User(name ='sam', account_balance = '720')

andrew.deposit(150).deposit(150).deposit(100).withdraw(100).yield_interest().display_account_info()
sam.deposit(200).deposit(200).withdraw(50).withdraw(50).withdraw(20).withdraw(20).yield_interest().display_account_info()

andrew.display_user_balance()
sam.display_user_balance()