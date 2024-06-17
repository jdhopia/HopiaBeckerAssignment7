class BankAccount:
    def __init__(self, first_name, last_name, account_number, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_number = account_number
        self.balance = float(balance)

    @property
    def first_name(self):
        return self.first_name

    @property
    def last_name(self):
        return self.last_name

    @property
    def account_number(self):
        return self.account_number

    @property
    def balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
