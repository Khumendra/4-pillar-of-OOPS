from abc import ABCMeta, abstractmethod
from random import randint


class Account(metaclass=ABCMeta):

    @abstractmethod
    def createAccount(self):
        return 0

    @abstractmethod
    def authenticate(self):
        return 0

    @abstractmethod
    def withdraw(self):
        return 0

    @abstractmethod
    def deposit(self):
        return 0

    @abstractmethod
    def displayBalance(self):
        return 0


class SavingAccount:
    def __init__(self):
        # [key][0]=> name ; [key][1] => balance/initailDeposit
        self.savingsAccounts = {}

    def createAccount(self, name, initailDeposit):
        self.accountNumber = randint(10000, 99999)
        self.savingsAccounts[self.accountNumber] = [name, initailDeposit]
        print('Account creation has been successful. your account number is :', self.accountNumber)

    def authenticate(self, name, accountNumber):
        if accountNumber in self.savingsAccounts.keys():
            if self.savingsAccounts[accountNumber][0] == name:
                print('Authentication Successful')
                self.accountNumber = accountNumber
                return True
            else:
                print('Authentication Failed')
                return False
        else:
            print('Authentication Failed')
            return False

    def withdraw(self, withdrawalAmount):
        if withdrawalAmount > self.savingsAccounts[self.accountNumber][1]:
            print('Insufficient Balance')
        else:
            self.savingsAccounts[self.accountNumber][1] -= withdrawalAmount
            print('Withdrawal was successful.')
            self.displayBalance()

    def deposit(self, depositAmount):
        self.savingsAccounts[self.accountNumber][1] += depositAmount
        print('Deposit was successful.')
        self.displayBalance()

    def displayBalance(self):
        print('Availbale Balance :', self.savingsAccounts[self.accountNumber][1])


savingAccount = SavingAccount()

while True:
    print('Enter 1 to create a new account')
    print('Enter 2 to access an existing account')
    print('Enter 3 to exit')

    userChoice = int(input())

    if userChoice is 1:
        print('Enter Your Name : ')
        name = input()
        print('Enter the initial deposit : ')
        deposit = int(input())
        savingAccount.createAccount(name, deposit)

    elif userChoice is 2:
        print('Enter Your Name : ')
        name = input()
        print('Enter your account number : ')
        accountNumber = int(input())
        authenticationStatus = savingAccount.authenticate(name, accountNumber)

        if authenticationStatus is True:
            while True:
                print('Enter 1 to withdraw')
                print('Enter 2 to deposit')
                print('Enter 3 to display available balance')
                print('Enter 4 to go back to the previous menu')

                userChoice = int(input())
                if userChoice is 1:
                    print('Enter a withdrawal amount : ')
                    withdrawalAmount = int(input())
                    savingAccount.withdraw(withdrawalAmount)

                elif userChoice is 2:
                    print('Enter an amount to be deposited ')
                    depositAmount = int(input())
                    savingAccount.deposit(depositAmount)

                elif userChoice is 3:
                    savingAccount.displayBalance()

                elif userChoice is 4:
                    break

    elif userChoice is 3:
        quit()
