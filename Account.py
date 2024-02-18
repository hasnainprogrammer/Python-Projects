
# Bank Account Project:-
# ---------------------

class Account():
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self,deposit_amt):
        self.balance += deposit_amt
        print(f'{deposit_amt} Money has been Added!')
    def withdraw(self,withdraw_amt):
        if self.balance >= withdraw_amt:
            self.balance -= withdraw_amt
            print(f'Withdraw {withdraw_amt} Money!')
        else:
            print('Sorry! Not Enough Money to Withdraw')
    def __str__(self):
        return f'Owner is:{self.owner} \nBalance is:{self.balance}$'
a = Account('Bill Gates',500)
print(a.owner)
print(a.balance)
a.deposit(100)
print(a.balance)
a.withdraw(200)
print(a.balance)
print(a)

