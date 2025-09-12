class Account:
    def __init__(self, owner: str, opening_balance: float = 0.0):
        self.owner = owner
        self._balance = opening_balance

    def deposit(self, amount):
        if not isinstance(amount,(int, float)):
            raise TypeError("Amount must be a number.")
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if isinstance(amount, bool):
            raise TypeError("Amount must be a number.")
        if not isinstance(amount,(int, float)):
            raise TypeError("Amount must be a number.")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient Funds")
        self._balance -= amount
        return self._balance

    @property
    def balance(self):
        return self._balance














a = Account("Alice", 100)

print(a.balance)   # 100.0

a.deposit(25)
print(a.balance)   # 125.0

a.withdraw(20)
print(a.balance)   # 105.0

try:
    # Test the read-only property: this should fail
    a.balance = 999
except AttributeError as e:
    print("Good: read-only property:", e)

