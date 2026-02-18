class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            raise ValueError("No money")
        
    def __str__(self):
        return f"User {self.owner} with balance: {self.balance}"
        
if __name__ == "__main__":
    account = BankAccount("Victor")
    account.deposit(1000)

    result1 = account.withdraw(700)
    print(result1)

    result2 = account.withdraw(500)
    print(result2)

    print(account)