balance = 100000
pin = 3464
name = "ABC"

class ATM:
    def __init__(self):
        self.balance = balance
        self.transaction_history = []

    def deposit(self):
        deposit_amount = float(input("Deposit Amount: "))
        self.balance += deposit_amount
        print(f"Balance is: {self.balance}")
        print("Congratulations Transaction Successful!!!")
        self.transaction_history.append(f"Deposited ${deposit_amount:.2f}")

    def withdraw(self):
        withdraw_amount = float(input("Withdraw Amount: "))
        if withdraw_amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= withdraw_amount
            print(f"Balance is: {self.balance}")
            print("Congratulations Transaction Successful!!!")
            self.transaction_history.append(f"Withdrew ${withdraw_amount:.2f}")

    def transfer(self, recipient_account):
        transfer_amount = float(input("Transfer Amount: "))
        if transfer_amount > self.balance:
            print("Insufficient funds for the transfer.")
        else:
            self.balance -= transfer_amount
            recipient.balance += transfer_amount
            print(f"Balance is: {self.balance}")
            self.transaction_history.append(f"Transferred ${transfer_amount:.2f} to {recipient.name}")
            recipient.transaction_history.append(f"Received ${transfer_amount:.2f} from {name}")

    def show_transaction_history(self):
        if not self.transaction_history:
            print("No transaction history.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)

# Load transaction history from a file
def load_transaction_history():
    try:
        with open("transaction_history.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

# Save transaction history to a file
def save_transaction_history(history):
    with open("transaction_history.txt", "w") as file:
        file.write("\n".join(history))

recipient = ATM()  # Create a recipient account
recipient.balance = 50000  # Set an initial balance for the recipient
recipient.name = "Recipient"


atm = ATM()
atm.transaction_history = load_transaction_history()  # Load history from the file

while True:
    print("-----------------")
    print("Welcome to TSB Bank")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    print("4. Transaction History")
    print("5.Exit")
    print("-------------------")
    n = int(input("Enter Your choice: "))
    if user_pin == pin:
        print(f"Hello, {name}")
        if n == 1:
            user_pin = int(input("Enter pin: "))
            atm.deposit()
        elif n == 2:
            user_pin = int(input("Enter pin: "))
            atm.withdraw()
        elif n == 3:
            user_pin = int(input("Enter pin: "))
            recipient.recipient_account=int(input(f"Enter {recipient.name} Account No: "))
            atm.transfer(recipient.recipient_account)
        elif n == 4:
            user_pin = int(input("Enter pin: "))
            atm.show_transaction_history()
        elif n==5:
            print("Visit Again")
    else:
        print("Enter a Valid Pin")

# Save the transaction history when the program exits
save_transaction_history(atm.transaction_history)
