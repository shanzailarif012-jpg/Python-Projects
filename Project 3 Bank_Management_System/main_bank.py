# Main File Bank_Management_System

print("\t\t\t\tBanking Management System")

class Account:
    # Constructor For New_Account
    def __init__(self, name, acc_no, pin, initial_balance=0):
        self.name = name
        self.acc_no = acc_no
        self.pin = pin
        self.balance = initial_balance
        self.transactions = []  # Store History


    # Verify Pin 
    def verify_pin(self, entered_pin):
        return entered_pin == self.pin
    

    # Deposit 
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid Amount")
            return
        
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        print("Deposited Successful", self.balance)



    # Withdraw 
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid Amount")
            return
        
        if amount > self.balance:
            print("Insufficient Balance")
            return
        self.balance -= amount
        self.transactions.append(f"Withdraw: {amount}")
        print("Withdraw Successful", self.balance)    



    # Account Details Display
    def display(self):
        print(f"Name: {self.name}") 
        print(f"Account No: {self.acc_no}") 
        print(f"Balance: {self.balance}") 

        

    # Transaction History
    def show_transactions(self):
        if self.transactions == []:
            print("No Transaction Yet")
        else:
            for transaction in self.transactions:
                print(transaction)


class Bank:

    def __init__(self):
        self.accounts = {}

    # New Account
    def create_account(self):
        name = input("Enter Your Name: ")
        acc_no = int(input("Enter Your Account_Number: "))

        if acc_no in self.accounts:
            print("Account Number Already Exists")
            return
        
        pin = int(input("Enter Pin Number: "))
        initial_balance = int(input("Enter Initial Balance: "))

        new_account = Account(name, acc_no, pin, initial_balance)
        self.accounts[acc_no] = new_account
        print("Account Created Successfully")

    # Find Account and Pin Num Verification
    def authenticate(self):
        acc_no = int(input("Enter Account_Number: "))
        if acc_no not in self.accounts:
            print("Account Not Found")
            return None
        account = self.accounts[acc_no]
        pin = int(input("Enter Pin_Number: "))
        if not account.verify_pin(pin):
            print("Incorrect Pin")
            return None
        
        return account
    
    # Main Menu With Loop
    def run(self):
        while True:
            print("Menu Options\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Display\n5. Transactions\n6. Exit")
            choice = int(input("Enter Choice Number: "))

            # Conditions To Choose Choice Options
            if choice == 1:
                self.create_account()

            if choice == 2:
                account = self.authenticate()
                if account: 
                    amount=int(input("Enter Amount: "))
                    account.deposit(amount)

            if choice == 3:
                account = self.authenticate()
                if account:
                    amount = int(input("Enter Amount: ")) 
                    account.withdraw(amount)

            if choice == 4:
                account = self.authenticate()
                if account:
                    account.display()

            if choice ==5:
                account = self.authenticate()
                if account:
                    account.show_transactions()

            if choice == 6:
                print("ThankYou GoodBye")
                break


if __name__ == "__main__":
    bank = Bank()
    bank.run()