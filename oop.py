class Account:
    balance=0
    def __init__(self,amt):
        self.balance=amt
    def transferTo(self,payee,amt):
        if amt < 0:
            return False
        elif self.balance>=amt:
            self.balance = self.balance - amt
            payee.balance = payee.balance + amt
            return True
        else:
            return False



myAccount=Account(100)
yourAccount=Account(50)

print("my",myAccount.balance)
print("your",yourAccount.balance)

check=myAccount.transferTo(yourAccount,100)
if(check):
    print('successful')
else:
    print('unsuccessful')


print("your",yourAccount.balance)