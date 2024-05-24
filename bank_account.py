# Define the BankAccount class
class BankAccount:
    # Initialize the BankAccount with account number, holder's name, and an optional balance
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number  # Store the account number
        self.account_holder = account_holder  # Store the account holder's name
        self.balance = balance  # Store the initial balance (default is 0.0)

    # Method to deposit an amount into the account
    def deposit(self, amount):
        if amount > 0:  # Check if the deposit amount is positive
            self.balance += amount  # Add the amount to the balance
            print(
                f"Deposited ${amount}. Current balance: ${self.balance}"
            )  # Print confirmation
        else:
            print(
                "Deposit amount must be positive."
            )  # Print error if amount is not positive

    # Method to withdraw an amount from the account
    def withdraw(self, amount):
        if 0 < amount <= self.balance:  # Check if the withdrawal amount is valid
            self.balance -= amount  # Subtract the amount from the balance
            print(
                f"Withdrew ${amount}. Current balance: ${self.balance}"
            )  # Print confirmation
        else:
            print(
                "Insufficient balance or invalid withdrawal amount."
            )  # Print error if amount is invalid

    # Method to get the current balance
    def get_balance(self):
        return self.balance  # Return the current balance

    # Method to get a string representation of the account
    def __str__(self):
        return f"Account Holder: {self.account_holder}, Account Number: {self.account_number}, Balance: ${self.balance}"


# Define the SavingsAccount class, which is a subclass of BankAccount
class SavingsAccount(BankAccount):
    # Initialize the SavingsAccount with additional interest rate
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.01):
        super().__init__(
            account_number, account_holder, balance
        )  # Initialize the base class
        self.interest_rate = interest_rate  # Store the interest rate

    # Method to apply interest to the balance
    def apply_interest(self):
        interest = self.balance * self.interest_rate  # Calculate the interest
        self.balance += interest  # Add the interest to the balance
        print(
            f"Applied interest: ${interest}. New balance: ${self.balance}"
        )  # Print confirmation

    # Method to get a string representation of the savings account
    def __str__(self):
        return f"Savings Account Holder: {self.account_holder}, Account Number: {self.account_number}, Balance: ${self.balance}, Interest Rate: {self.interest_rate * 100}%"


# Function to demonstrate banking operations
def start_banking():
    # Create a BankAccount instance
    account = BankAccount("654320", "Alaa Deeb")
    account.deposit(1000)  # Deposit money into the account
    account.withdraw(500)  # Withdraw money from the account
    print(account)  # Print the account details

    # Create a SavingsAccount instance
    savings_account = SavingsAccount(
        "024567", "Alaa Deeb", balance=1000, interest_rate=0.05
    )
    savings_account.apply_interest()  # Apply interest to the savings account
    print(savings_account)  # Print the savings account details


# Start the banking demonstration
start_banking()
