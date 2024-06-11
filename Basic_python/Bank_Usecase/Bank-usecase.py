class Bank:
    def __init__(self, atm_pin, initial_balance=0):
        self._atm_pin = atm_pin
        self.balance = initial_balance

    def verify_pin(self, entered_pin):
        return self._atm_pin == entered_pin

    def withdraw(self, entered_pin, withdrawal_amount):
        if not self.verify_pin(entered_pin):
            return "Invalid pin"
        if withdrawal_amount > self.balance:
            return "Insufficient funds"
        self.balance -= withdrawal_amount
        return f"Withdrawal amount: {withdrawal_amount}, Remaining balance: {self.balance}"

    def deposit(self, entered_pin, deposit_amount):
        if not self.verify_pin(entered_pin):
            return "Invalid pin"
        self.balance += deposit_amount
        return f"Deposited amount: {deposit_amount}, Current balance: {self.balance}"

if __name__ == "__main__":
    user_bank_account = Bank(atm_pin=1234, initial_balance=1000)

    while True:
        user_choice = input("\n1. Withdraw\n2. Deposit\n3. Exit\nEnter your choice: ")

        if user_choice == '3':
            break

        entered_pin = int(input("Enter your ATM pin: "))
        transaction_amount = float(input("Enter amount: "))

        if user_choice == '1':
            print(user_bank_account.withdraw(entered_pin, transaction_amount))
        elif user_choice == '2':
            print(user_bank_account.deposit(entered_pin, transaction_amount))
        else:
            print("Invalid choice")


# In[ ]:




