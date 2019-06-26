class Account:

    def __init__(self,amt):
        self._balance=amt

    def getBalance(self):
        return self._balance
    def setBalance(self,bal):
        if(bal>=0):
            self._balance=bal
    def transferTo(self,payee,amt):
        self._balance=self.getBalance()-amt
        temp=payee.getBalance()+amt
        payee.setBalance(temp)

myAccount=Account(100)
yourAccount=Account(50)


print(myAccount._balance)
print(myAccount.getBalance())