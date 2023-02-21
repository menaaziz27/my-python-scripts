class Bank:
    def __init__(self, Balance):
        
        self.Balance = Balance

    def displayBalance(self):
        print(f"Your currently balance is {self.Balance})

    def withdraw(self, username, pw, amount):
        if self.UserName == username and self.Password == pw
            self.Balance -= amount
            print(f"your currently balance is {self.Balance}")
        else:
            print(f'invalid input')

    def deposit(self, username, pw, amount):
        if self.UserName == username and self.Password == pw
            self.Balance += amount
            print(f"your currently balance is {self.Balance}")
        else:
            print(f'invalid input')

class Client(Bank):
    def __init__(self, ClientName, AccountNumber, UserName, Password,
                 PhoneNumber):
        self.ClientName = ClientName
        self.AccountNumber = AccountNumber
        self.UserName = UserName
        self.Password = Password
        self.PhoneNumber = PhoneNumber
