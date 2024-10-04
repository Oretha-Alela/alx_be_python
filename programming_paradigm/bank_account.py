class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance= self.balance + amount

        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            return True
        else:
            return False

    def display_balance(self):
         current_balance = self.balance
         message = f"Current Balance: ${current_balance}"
         print(message)
         


