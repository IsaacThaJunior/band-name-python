class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self) -> str:
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"

    def deposit(self, number):
        print('Deposit Accepted')
        self.balance = number + self.balance
        return self.balance

    def withdraw(self, number):
        if number > self.balance:
            print('Funds Unavailable!')
        else:
            print('Withdrawal Accepted')
            self.balance = self.balance - number
            return self.balance


acct1 = Account('Jose', 100)
print(acct1)


acct1.deposit(40)
print(acct1)

acct1.withdraw(400)
print(acct1)