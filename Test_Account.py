from Account import Account
import unittest

class Test_Account(unittest.TestCase):

    def setUp(self):
        self.__account = Account(1122, 20000.0, 4.5)

    def test_withdrawal(self):
        self.__account.withdraw(2500)
        self.assertEquals(self.__account.get_balance(), 17500)

    def test_deposit(self):
        self.__account.deposit(3000)
        self.assertEquals(self.__account.get_balance(), 23000)
    
    def test_printout(self):
        self.assertEqual(self.__account.printout(), "1122 20000.0 0.375 7500.0")

def main():
    account = Account(1122, 20000.0, 4.5)

    account.withdraw(2500)
    account.deposit(3000)

    print(account.id, account.balance, account.get_monthly_interest_rate(), account.get_monthly_interest())


if __name__ == "__main__":
    unittest.main()