# Create a new class Transaction to store all transactions with attributes for date and time, narration, amount, transaction type etc.

# The Account class should have a new attribute called transactions which will store every transaction that happens in the account

# Each transaction should be stored as an instance of the Transaction

# The get balance method should use the transactions list to compute the current balance


# Add encapsulation to the Account class to have sensitive attributes like balance and account number only accessible via given class methods. 
from datetime import datetime
class Transaction:

    def __init__(self,datetime, narration, amount, transaction_type):
        self.datetime=datetime.now()
        self.narration=narration
        self.amount=amount
        self.transaction_type=transaction_type

    def __str__(self):
        return f"{self.datetime.strftime('%Y-%m-%d %H:%M:%S')} | {self.narration} | {self.amount:.2f} | {self.transaction_type}"

class Account:
    def __init__(self,name,account_number):
        self.name=name
        self.__account_number=account_number
        self.__balance=0.0
        self.transactions=[]
        self.__loan_balance=0.0
        self.__minimum_balance=0.0
        self.is_frozen=False


    def deposit(self,amount):
        if amount <=0:
            return f"Deposit must be a positive value"
        if self.is_frozen:
            return f"Account is frozen, cannot complete transaction."
        
        now=datetime.now()
        deposits=Transaction(now, f"Deposit {amount:.2f}",amount,"deposit")
        self.transactions.append(deposits)
        self.__balance+=amount
        return f"Dear {self.name}, deposit of {amount:.2f} was successful, your account balance is {self.__balance:.2f}"

    def withdraw(self,amount):
        if amount <=0:
            return f"Withdrawal amount must be a positive number."
        if self.is_frozen:
            return f"Account is frozen, Cannot complete transaction."
        if self.__balance-amount<= self.__minimum_balance:
            return f"Insufficient funds, withdrawal amount is more than the minimum balance."
        if self.__balance >=amount:
            now=datetime.now()  
            withdrawal=Transaction(now, f"Withdraw{amount:.2f},",-amount,"Withdrawal")
            self.transactions.append(withdrawal)
            self.__balance -=amount
            return f"Dear {self.name}, withdrawal of {amount:.2f} successful, your balance is {self.__balance:.2f}"
        else:
            return "Insufficient funds"

    def transfer_funds(self,target_account,amount):
        if amount <=0:
            return f"Transaction failed, transfer amount must be positive."
        if self.is_frozen:
            return "Account is frozen cannot complete transaction."
        if amount>self.__balance:
            return f"Dear {self.name}, your account balance is {amount:.2f}, please try a lower amount."
        if amount < self.__balance:
            now=datetime.now()
            withdrawal=Transaction(now,f"Transer amount {amount:.2f}, to account {target_account},",-amount,"Transfer")
            self.transactions.append(withdrawal)
            self.__balance-=amount
            return f"Dear {self.name}, transfer of {amount:.2f} to {target_account} was successful, new account balance is {self.__balance}"

    def get_balance(self):
        now=datetime.now()
        self.__balance=sum(transaction.amount for transaction in self.transactions)
        return f"Dear {self.name} your account balance as at {now} is {self.__balance}"

    def request_loan(self,amount):
        if amount <=0:
            return f"Loan amount must be positive"
        total_deposit=sum(transaction.amount for transaction in self.transactions if transaction.transaction_type =="deposit")
        if amount > total_deposit:
            return f"Dear {self.name}, your loan limit is {total_deposit}, try a lower amount"
        self.__loan_balance+=amount
        loans=Transaction(datetime.now(), f"loan of {amount:.2f}", amount, "loan")
        self.transactions.append(loans)
        self.__balance+=amount
        return f"Dear {self.name}, your loan request of {amount:.2f} has been approved, new account balance is {self.__balance}"
    
    def repay_loan(self,amount):
        if amount <=0:
            return f"Loan repayment amount  must be positive"
        if amount< self.__loan_balance:
            return f"Dear {self.name}, your loan balance is {self.__loan_balance}, please pay full amount"
        if amount >=self.__loan_balance:
            self.__balance-=amount
            now=datetime.now()
            repay_loan=Transaction(now,f"Loan repayment {amount:.2f}",-amount,"Loan repayment")
            self.transactions.append(repay_loan)
            return f"Dear {self.name}, loan repayment of {amount:.2f} was successful, new account balance is {self.__balance}"
    def view_account(self):
        now=datetime.now()
        return f"Account name: {self.name} | Account number: {self.__account_number} | Account balance{self.__balance} {now}"

    def change_owner(self, new_owner):
        return f"Dear {self.name}, your account name has been update to {new_owner}"

    def account_statement(self):
        now=datetime.now()
        print(f"Account for {self.name}, {self.__account_number} as at {now}")   
        for transaction in self.transactions:
            print(transaction)

    def interest_calculation(self):
        rate = 0.05
        interest= self.__balance*rate
        self.__balance+=interest
        now=datetime.now()
        interest_earned=Transaction(now,f"Interest {interest:.2f} earned", interest, "interest")
        self.transactions.append(interest)
        return f"Dear {self.name}, yoour account has been credited with {interest} in interest. You new account is {self.__balance}"
    def freeze(self):
        is_frozen= False
        return f"Dear {self.name}, your account is frozen, cannot complete transaction"

    def unfreeze(self):
        is_frozen= True
        return f"Dear {self.name}, your account has been unfrozen, you can transact."

    def minimum_balance(self, amount):
        if amount <=0:
            return f"minimum balance cannot be negative."
        amount=self.__minimum_balance
        return f"Dear {self.name}, your minimum balance has been set to {self.__minimum_balance}"

    def close_account(self):
        self.__balance=0.0
        self.transactions=[]
        self.__loan_balance=0.0
        self.__minimum_balance=0.0
        return f"Dear {self.name}, your account has been successfully closed. Thank you for banking with us."  


        from index import Account
        acc1=Account("Anna", 23456)
        acc1.deposit(5000)
        acc1.withdraw(2300)
        acc1.transfer_funds(2356475,1500)
        acc1.get_balance()
        acc1.request_loan(1700)
        acc1.repay_loan(1700)
        acc1.view_account()
        acc1.change_owner("Mitchelle")
        acc1.statement()
        acc1.interest_calculation()
        acc1.freeze()
        acc1.unfreeze()
        acc1.minimum_balance(1000)
        acc1.close_account()

