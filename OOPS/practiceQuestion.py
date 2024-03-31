# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.

class Account:

    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance
    
    def debit(self, amount):
        self.balance   -= amount
        print("amount is debited your current Balance is: ", self.balance )

    def credit(self, amount):
        self.balance   += amount
        print("amount is credited, your current Balance is: ", self.balance ) 
    
    def print_balance(self):
        print("your current Balance is: ", self.balance)

a1 = Account(773930, 50000)
a1.print_balance()


        