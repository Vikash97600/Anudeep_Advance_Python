class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Dear customer, {amount} amount has been added to your account.")
        else:
            print("Dear customer , the amount that you want to deposit is invalid.")
    
    def withdraw(self,amount):
        if 0<amount<=self.balance:
            self.balance-= amount
            print(f"Dear customer, {amount} amount  has been withdraw from your account.")
        else:
            print("Dear customer,the amount that you want to withdraw  is invalid or insufficient balance.")
    
    def checkBalance(self):
        return print(f"Dear customer, your current balance is {self.balance}")

account=BankAccount("Vikash Chaurasiya",10000)
account.deposit(5000)
account.withdraw(8000)
account.checkBalance()