class BankAccount:

    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.balance = initial_balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Withdrawal exceeds balance")
        self.balance -= amount

if __name__ == "__main__":
    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(20)
    print(account.get_balance())