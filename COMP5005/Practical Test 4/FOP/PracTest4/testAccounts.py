'''
  Practical Test 4

  testAccounts.py - program to test functions of accounts.py
  
  Student Name   :
  Student Number :
  Date/prac time :
'''
from accounts import *

def main():
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

if __name__ == "__main__":
    main()
