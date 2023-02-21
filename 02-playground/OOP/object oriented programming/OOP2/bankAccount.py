class Bank:
    def __init__(self, name, balance):
        self.owner = name 
        self.balance = balance
    
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

client = Bank("Mark" , 15000)

print(client.deposit(500))
print(client.withdraw(200))
