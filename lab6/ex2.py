class Account:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def calculate_interest(self):
        return 0.0


class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate


class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance=0.0, overdraft_limit=100.0):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or overdraft limit reached.")


savings_account = SavingsAccount(account_number="SA123", account_holder="John Doe", balance=1000.0)
savings_account.deposit(500)
savings_account.withdraw(200)
print("Savings Account Interest:", savings_account.calculate_interest())

checking_account = CheckingAccount(account_number="CA456", account_holder="Jane Smith", balance=500.0)
checking_account.deposit(200)
checking_account.withdraw(700)
