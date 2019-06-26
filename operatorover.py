class A:
    def __init__(self,d,m,y):
        self.day=d
        self.month=m
        self.year=y



    def __add__(self,other):
        res=A(self.day+other.day,self.month+other.month,self.year+other.year)
        a=res.day//30
        b=res.day%30
        res.month=res.month+a
        res.day=b
        c=res.month//12
        d=res.month%12
        res.year=res.year+c
        res.month=d
        return res

    def __sub__(self,other):
        ressub = A(self.day - other.day, self.month - other.month, self.year - other.year)


    def getYear(self):
        return str(self.year)
    def getMonth(self):
        return str(self.month)
    def getDay(self):
        return str(self.day)
x=A(5,10,2001)
y=A(73,13,2005)
z=x-y
print(z.getDay()+"/"+z.getMonth()+"/"+z.getYear())