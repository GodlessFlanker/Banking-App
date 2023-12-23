import csv
import datetime

class Bank:
    def __init__(self):
        self.usd_balance = 0
        self.euro_balance = 0
        self.try_balance = 0

    def currency(self):
        currency = input("Enter the currency symbol ($ for USD, € for Euro, TRY for Turkish Lira): ")
        return currency

    def get_current_date(self):
        current_date = datetime.datetime.now().strftime("%d/%m/%Y")
        return current_date

    def deposit(self):
        deposit_currency = self.currency()
        deposited_amount = int(input(f"Enter the amount in {deposit_currency} that you want to deposit: "))

        if deposit_currency == "$":
            self.usd_balance += deposited_amount
        elif deposit_currency == "€":
            self.euro_balance += deposited_amount
        elif deposit_currency == "TRY" or deposit_currency == "Turkish Lira":
            self.try_balance += deposited_amount

        print(f"You have successfully deposited {deposited_amount} {deposit_currency}. Your new balance is: ")
        self.show_balance()

        current_date = self.get_current_date()

        with open('transaction_history.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([current_date, deposit_currency, deposited_amount, 'Deposit'])

    def withdraw(self):
        withdraw_currency = self.currency()
        withdrawn_amount = int(input(f"Enter the amount in {withdraw_currency} that you want to withdraw: "))
        
        if withdraw_currency == "$":
            if withdrawn_amount > self.usd_balance:
                print("Insufficient balance. Please enter a lower amount.")
                self.withdraw()
            else:
                self.usd_balance -= withdrawn_amount
        elif withdraw_currency == "€":
            if withdrawn_amount > self.euro_balance:
                print("Insufficient balance. Please enter a lower amount.")
                self.withdraw()
            else:
                self.euro_balance -= withdrawn_amount
        elif withdraw_currency == "TRY":
            if withdrawn_amount > self.try_balance:
                print("Insufficient balance. Please enter a lower amount.")
                self.withdraw()
            else:
                self.try_balance -= withdrawn_amount

        print(f"You have successfully withdrawn {withdrawn_amount} {withdraw_currency}. Your new balance is: ")
        self.show_balance()

        current_date = self.get_current_date()

        with open('transaction_history.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([current_date, withdraw_currency, withdrawn_amount, 'Withdraw'])

    def show_balance(self):
        print(f"USD Balance: {self.usd_balance}$")
        print(f"Euro Balance: {self.euro_balance}€")
        print(f"TRY Balance: {self.try_balance}TRY")

    def view_transaction_history(self):
        with open('transaction_history.csv', 'r') as file:
            reader = csv.reader(file)
            print("Transaction History:")
            for row in reader:
                print(f"{row[0]} {row[1]} {row[2]} {row[3]}")

def main():
    bank = Bank()

    while True:
        action = input("Enter 'D' to deposit, 'W' to withdraw, 'B' to check your balance, 'H' to view transaction history, or 'Q' to quit: ")

        if action.lower() == 'd':
            bank.deposit()
        elif action.lower() == 'w':
            bank.withdraw()
        elif action.lower() == 'b':
            bank.show_balance()
        elif action.lower() == 'h':
            bank.view_transaction_history()
        elif action.lower() == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid action. Please enter a valid action.")

if __name__ == "__main__":
    main()
       