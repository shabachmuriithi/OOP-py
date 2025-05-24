class Account:
    def __init__(self,name):
        self.name=name
        self.balance= 0
        self.deposits=[]
        self.withdrawals=[]
        self.is_frozen=False
        self.min_balance=0

# Get Balance: Method to calculate an account balance from deposits and withdrawals
    def get_balance(self):
        balance=self.balance
        return f"Hello {self.name}, your account balance is {self.balance}"
# Deposit: method to deposit funds, store the deposit and return a message with the new balance to the customer. It should only accept positive amounts.
    def deposit(self,amount):
        if amount <=0:
            return f"Deposit amount must be be greater than 0"
        self.balance+=amount
        self.deposits.append(amount)
        return f"Hello {self.name}, you have receieved {amount}, your new balance is {self.balance}"

# Withdraw: method to withdraw funds, store the withdrawal and return a message with the new balance to the customer. An account cannot be overdrawn.
    def withdraw(self,amount):
        if amount >=self.balance:
            return f"Please try a lower amount, account balance cannot be zero"
        self.balance -=amount
        self.withdrawals.append(amount)
        return f"Hello {self.name}, you have withdrawn {amount}, your new balance is {self.balance}"
# Transfer Funds: Method to transfer funds from one account to an instance of another account
    def transfer_funds(self,amount):
        if amount >self.balance:
            return f"Cannot complete transaction, try a lower amount"
        self.balance-=amount
        self.withdrawals.append(amount)
        return f"Hello {self.name}, you have transferred {amount}, your new balance {self.balance}"
# Request Loan: Method to request a loan amount
    def request_loan(self,amount):
        if amount>= self.balance:
            return f"Your account balance is {self.balance}, loan cannot be more than balance"
        self.balance+=amount
        self.deposits.append(amount)
        return f"Dear {self.name}, your loan of {amount} has been approved, your new account balance is {self.balance}"
# Repay Loan: Method to repay a loan with a given amount
    def repay_loan(self,amount):
        loan=500
        if amount< loan:
            return f"Your loan amount is {loan}, please pay in full"
        self.balance-=amount
        self.withdrawals.append(amount)
        return f"Dear {self.name}, your loan of {loan} has been fully repaid, your account balance is {self.balance}"
# View Account Details: Method to display the account owner's details and current balance
    def account_details(self):
        return f"Account name is {self.name} and the current balance is {self.balance}"
# Change Account Owner: Method to update the account owner's name
    def change_name(self, new_name):
        self.new_name=new_name
        return f"Dear {self.name}, your account name has changed to {self.new_name}"
# Account Statement: Method to generate a statement of all transactions in an account. (Print using a for loop).
    def account_statement(self):
        print(f"Account statement for {self.name}: as at 31st May 2025")
        print("Credit:")
        for deposit in self.deposits:
            print(f"{deposit}")
        print("Debit:")
        for withdrawal in self.withdrawals:
            print(f"{withdrawal}")
# Interest Calculation: Method to calculate and apply an interest to the balance. Use 5% interest
    def interest(self,rate):
        self.balance=(rate*self.balance)+self.balance  
        return f"Dear {self.name}, your account after interest is {self.balance}"
# Freeze/Unfreeze Account: Methods to freeze and unfreeze the account for security reasons
    def freeze(self):
        self.is_frozen=True
        return f"Dear {self.name}, your account has been frozen for security reasons, try transacting later."

    def unfreeze(self):
        self.is_frozen=True
        return f"Dear {self.name}, your account has been unfrozen, you can now transact successfully"
# Set Minimum Balance: Method to enforce a minimum balance requirement. You cannot withdraw if your balance is less
    def set_min_balance(self, amount):
        self.min_balance=amount
        return f"Dear {self.name}, your minimum balance has been set to {self.min_balance}"
# Close Account: Method to close the account and set all balances to zero and empty all transactions
    def close_account(self):
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]
        return f"Dear {self.name}, your account has been closed"





        


# deposit
# withdraw
# get balance
# loan
# repay_loan
# get_statement
# get_loan_statement

