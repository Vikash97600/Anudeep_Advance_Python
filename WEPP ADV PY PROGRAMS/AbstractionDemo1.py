from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, account_number, balance):
      self.account_number = account_number
      self._balance = balance # Protected attribute
 
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
      return self._balance
# Concrete class representing a savings account

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
       super().__init__(account_number, balance)
       self.interest_rate = interest_rate
 
    def deposit(self, amount):
      self._balance += amount
      print(f"Deposited {amount} to Savings Account {self.account_number}")
 
    def withdraw(self, amount):
        if amount <= self._balance:
           self._balance -= amount
           print(f"Withdrew {amount} from Savings Account {self.account_number}")
        else:
           print("Insufficient funds!")

# Concrete class representing a current account

class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
 
    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount} to Current Account {self.account_number}")
    def withdraw(self, amount):
        if amount <= self._balance + self.overdraft_limit:
           self._balance -= amount
           print(f"Withdrew {amount} from Current Account {self.account_number}")
        else:
           print("Overdraft limit exceeded!")
# Example usage

savings = SavingsAccount("SAV123", 1000, 0.05)
current = CurrentAccount("CUR456", 2000, 500)
savings.deposit(500)
savings.withdraw(200)
current.deposit(1000)
current.withdraw(2500)
current.withdraw(3000) # Should trigger overdraft limit exceeded
