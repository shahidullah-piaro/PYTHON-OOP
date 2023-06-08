class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.loan_amount = 0
        self.transaction_history = []

    def add_loan(self, amount):
        self.loan_amount += amount
        print("Loan request approved!")

    def add_transaction(self, transaction_type, amount):
        transaction = {
            'type': transaction_type,
            'amount': amount
        }
        self.transaction_history.append(transaction)


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.accounts = []

    def display_accounts(self):
        if not self.accounts:
            print("No accounts found.")
        else:
            print("Accounts:")
            for account in self.accounts:
                print(f"Account Number: {account.account_number} | Balance: {account.balance} | Loan Amount: {account.loan_amount}")

    def create_account(self, account_number, initial_balance):
        account = Account(account_number, initial_balance)
        self.accounts.append(account)
        print("Account created successfully!")

    def deposit(self, account_number, amount):
        for account in self.accounts:
            if account.account_number == account_number:
                account.balance += amount
                account.add_transaction('Deposit', amount)
                print("Deposit successful!")
                return
        print("Account not found.")

    def withdraw(self, account_number, amount):
        for account in self.accounts:
            if account.account_number == account_number:
                if account.balance >= amount:
                    account.balance -= amount
                    account.add_transaction('Withdrawal', amount)
                    print("Withdrawal successful!")
                else:
                    print("Insufficient balance.")
                return
        print("Account not found.")

    def request_loan(self, account_number, amount):
        for account in self.accounts:
            if account.account_number == account_number:
                account.add_loan(amount)
                account.add_transaction('Loan Request', amount)
                return
        print("Account not found.")


class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.loan_enabled = True

    def create_account(self, user, account_number, initial_balance):
        user.create_account(account_number, initial_balance)

    def check_bank_balance(self, users):
        total_balance = 0
        total_loan = 0
        for user in users:
            for account in user.accounts:
                total_balance += account.balance
                total_loan += account.loan_amount
        print(f"Total Bank Balance: {total_balance}")
        print(f"Total Loan Amount: {total_loan}")

    def view_transaction_history(self, user):
        for account in user.accounts:
            print(f"Account Number: {account.account_number}")
            print("Transaction History:")
            for transaction in account.transaction_history:
                print(f"Type: {transaction['type']} | Amount: {transaction['amount']}")

    def toggle_loan_functionality(self):
        self.loan_enabled = not self.loan_enabled
        status = "enabled" if self.loan_enabled else "disabled"
        print(f"Loan functionality {status}.")


def main():
    users = []  # Store user objects

    admin = Admin("admin", "adminpass")  # Create admin object

    while True:
        print("\nBank Management Menu:")
        print("1. User Login")
        print("2. Admin Login")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")

            # Check if user exists
            for user in users:
                if user.username == username and user.password == password:
                    logged_in_user = user
                    while True:
                        print("\nUser Menu:")
                        print("1. Display Accounts")
                        print("2. Create Account")
                        print("3. Deposit")
                        print("4. Withdraw")
                        print("5. Request Loan")
                        print("6. View Transaction History")
                        print("7. Logout")

                        user_choice = input("Enter your choice (1-7): ")

                        if user_choice == "1":
                            logged_in_user.display_accounts()
                        elif user_choice == "2":
                            account_number = input("Enter account number: ")
                            initial_balance = float(input("Enter initial balance: "))
                            logged_in_user.create_account(account_number, initial_balance)
                        elif user_choice == "3":
                            account_number = input("Enter account number: ")
                            amount = float(input("Enter amount to deposit: "))
                            logged_in_user.deposit(account_number, amount)
                        elif user_choice == "4":
                            account_number = input("Enter account number: ")
                            amount = float(input("Enter amount to withdraw: "))
                            logged_in_user.withdraw(account_number, amount)
                        elif user_choice == "5":
                            if admin.loan_enabled:
                                account_number = input("Enter account number: ")
                                amount = float(input("Enter loan amount: "))
                                logged_in_user.request_loan(account_number, amount)
                            else:
                                print("Loan functionality is currently disabled by the admin.")
                        elif user_choice == "6":
                            admin.view_transaction_history(logged_in_user)
                        elif user_choice == "7":
                            break
                        else:
                            print("Invalid choice! Please try again.")
                    break
            else:
                print("Invalid username or password!")
        elif choice == "2":
            admin_username = input("Enter admin username: ")
            admin_password = input("Enter admin password: ")

            # Check if admin credentials are correct
            if admin.username == admin_username and admin.password == admin_password:
                while True:
                    print("\nAdmin Menu:")
                    print("1. Create Account")
                    print("2. Check Bank Balance")
                    print("3. View Transaction History")
                    print("4. Toggle Loan Functionality")
                    print("5. Logout")

                    admin_choice = input("Enter your choice (1-5): ")

                    if admin_choice == "1":
                        username = input("Enter username of the user: ")
                        account_number = input("Enter account number: ")
                        initial_balance = float(input("Enter initial balance: "))
                        user_found = False
                        for user in users:
                            if user.username == username:
                                admin.create_account(user, account_number, initial_balance)
                                user_found = True
                                break
                        if not user_found:
                            print("User not found!")
                    elif admin_choice == "2":
                        admin.check_bank_balance(users)
                    elif admin_choice == "3":
                        username = input("Enter username of the user: ")
                        user_found = False
                        for user in users:
                            if user.username == username:
                                admin.view_transaction_history(user)
                                user_found = True
                                break
                        if not user_found:
                            print("User not found!")
                    elif admin_choice == "4":
                        admin.toggle_loan_functionality()
                    elif admin_choice == "5":
                        break
                    else:
                        print("Invalid choice! Please try again.")
            else:
                print("Invalid admin username or password!")
        elif choice == "3":
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
