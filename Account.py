
class Account:
    def __init__(self, id=0, initial_balance=100.0, annual_interest_rate=0.0 ):
        self.id = id
        self.balance = initial_balance
        self.annual_interest_rate = annual_interest_rate

    def get_id(self):
        return self.id
    
    def get_balance(self):
        return self.balance
    
    def get_a_i_r(self):
        return self.annual_interest_rate * 100
    
    def set_id(self, id):
        self.id = id
    
    def set_balance(self, balance):
        self.balance = balance

    def set_a_i_r(self, air):
        self.annual_interest_rate = air / 100

    def get_monthly_interest_rate(self):
        return self.annual_interest_rate / 12
    
    def get_monthly_interest(self):
        return self.balance * self.get_monthly_interest_rate()
    
    def withdraw(self, withdrawal):
        self.balance -= withdrawal
    
    def deposit(self, deposited):
        self.balance += deposited
    
    def printout(self):
        the_string = str(self.get_id()) + " " + str(self.get_balance()) + " " + str(self.get_monthly_interest_rate()) + " " + str(self.get_monthly_interest())
        return(the_string)

# print(Account(1122, 20000.0, 4.5).printout())