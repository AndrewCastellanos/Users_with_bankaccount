class BankAccount():
    all_instances =  []


    def __init__(self,int_rate, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_instances.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if (self.balance - amount) > 400:
            self.balance -= amount
        else: 
            print(f'Insufficent funds. Your balance: {self.balance}')
        return self
    
    def display_account_info(self):
        print(self.balance)
        return self
    
    def yield_interest(self):
        if self.balance > 200:
            self.balance += (self.balance * self.int_rate)
        else: 
            print(f'Negative Account Balance')
        return self


    @classmethod
    def print_instances(cls):
        for i in cls.all_instances:
            print(i.display_account_info())


andrew = BankAccount(.1, 300)
sam = BankAccount(0.5, 500)

BankAccount.print_instances()


andrew.deposit(150).deposit(150).deposit(100).withdraw(100).yield_interest().display_account_info()
sam.deposit(200).deposit(200).withdraw(50).withdraw(50).withdraw(20).withdraw(20).yield_interest().display_account_info()