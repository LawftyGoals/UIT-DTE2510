
from Account import *

class ATM():
    def __init__(self):
        self.account_list = [Account(0, 100), Account(1, 100), Account(2, 100), 
            Account(3, 100), Account(4, 100), Account(5, 100), Account(6, 100),
            Account(7, 100), Account(8, 100), Account(9, 100)]
        
        while True:
            choose_account = int(input("\nEnter an account: "))
            if choose_account in range(10):
                self.get_choice(self.account_list[choose_account])
            elif choose_account > 9 or choose_account < 0:
                print("Invalid input")


    def get_choice(self, account):
        while True:
            print("\nMain menu")
            print("1: check balance")
            print("2: withdraw")
            print("3: deposit")
            print("4: exit")
            print("Enter a choice: ", end = "")
            choice = int(input())
            if choice < 1 or choice > 4:
                print("\nWrong choice, try again: ", end = "")
            elif choice == 1:
                print(account.get_balance())
            elif choice == 2:
                account.withdraw(float(input("\nEnter amount to be withdrawn: ")))
                print(account.get_balance())
            elif choice == 3:
                account.deposit(float(input("\nEnter amount to be deposited: ")))
                print(account.get_balance())
            else:
                break


ATM()