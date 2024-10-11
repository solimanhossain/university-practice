'''
  Practical Test 4

  accounts.py - class for bank account portfolio
  
  Student Name   :
  Student Number :
  Date/prac time :
'''

class Portfolio:

    def __init__(self):
        self.accounts = []

    def addAccount(self, name, number, balance):
        self.accounts.append(BankAccount(name, number, balance))

    def findAccount(self, name):
        for acct in self.accounts:
            if acct.name == name:
                return acct
        return None

    def deposit(self, name, amount):
        temp = self.findAccount(name)
        if temp:
            print("\n---> Depositing $" + str(amount) + " into account " + name)
            temp.deposit(amount)
            print("         Complete")
        else:
            raise AccountNotFoundError(name)

    def withdraw(self, name, amount):
        temp = self.findAccount(name)
        if temp:
            try:
                print(f"\n---> Attempting to withdraw ${amount} from account {name}")
                temp.withdraw(amount) 
                print("         Withdrawal Complete")
            # Fourth Modify accounts.py to: Add exception handling
            except InsufficientFundsError as e:
                print(e) 
        else:
            raise AccountNotFoundError(name)

    def balances(self):
        print('\n<----------------  Balances of All Accounts  ---------------->')
        total = 0
        for acct in self.accounts:
            print(f"Name: {acct.name}\tNumber: {acct.num}\tBalance: {acct.bal}")
            total += acct.bal
        print(f"\t\t\t\t\t\tTotal:   {total}")
        print('<------------------------------------------------------------>\n')

    # Second Modify account.py to: Add getNumAccounts() and getTotalBalance()
    def getNumAccounts(self):
        numberOfAccounts = len(self.accounts)
        print(f'\nIn this {self.__class__.__name__}, Number of Accounts: {numberOfAccounts}')
        return numberOfAccounts

    def getTotalBalance(self):
        totalBalance = sum(acct.bal for acct in self.accounts)
        print(f'\nIn this {self.__class__.__name__}, Total Balance: {totalBalance}')
        return totalBalance


class BankAccount ():

    def __init__(self, name, number, balance):
        self.name = name
        self.num = number
        self.bal = balance

    def withdraw(self, amount):
        # Fourth Modify accounts.py to: Add exception handling
        if amount > self.bal:
            raise InsufficientFundsError(self.name, self.bal, amount)
        else:
            self.bal -= amount

    def deposit(self, amount):
        self.bal = self.bal + amount


# Fourth Modify accounts.py to: Add exception handling
class InsufficientFundsError(Exception):
    def __init__(self, account_name, current_balance, attempted_withdrawal):
        self.account_name = account_name
        self.current_balance = current_balance
        self.attempted_withdrawal = attempted_withdrawal
        super().__init__(f"Insufficient funds in account '{account_name}': Attempted to withdraw ${attempted_withdrawal}, but only ${current_balance} available.")

    def __str__(self):
        return f"[{self.__class__.__name__}] Account '{self.account_name}': Insufficient funds. Balance: ${self.current_balance}, Withdrawal attempted: ${self.attempted_withdrawal}"


class AccountNotFoundError(Exception):
    def __init__(self, account_name):
        self.account_name = account_name
        super().__init__(f"Account '{account_name}' not found in the portfolio.")

    def __str__(self):
        return f"[{self.__class__.__name__}] Account '{self.account_name}' not found."


# First Modify testAccounts.py to : Add a new account and test deposit, withdrawal
testAcc = Portfolio()
testAcc.addAccount("Castle", "999999-1", 1000) 
testAcc.addAccount("Shrubbery", "999999-2", 100) 
testAcc.balances()
testAcc.deposit("Castle", 100)
try: # Fith Modify testAccounts.py: Add exception handling
    testAcc.withdraw("Shrubbery", 10) 
except InsufficientFundsError as err:
    print(err)
except AccountNotFoundError as err:
    print(err)
try: # Fith Modify testAccounts.py: Add exception handling
    testAcc.withdraw("Shrubbery", 1000)  
except InsufficientFundsError as err:
    print(err)
except AccountNotFoundError as err:
    print(err)
testAcc.balances()

# Third Modify testAccounts.py: Add a new account and test getNumAccounts and getTotalBalance
testAcc.addAccount("Grail", "999999-3", 100)
try: # Fith Modify testAccounts.py: Add exception handling
    testAcc.withdraw("Grail", 1000)  
except InsufficientFundsError as err:
    print(err)
except AccountNotFoundError as err:
    print(err)
testAcc.getNumAccounts()
testAcc.getTotalBalance()