class Date:
    def __init__(self,d,m,y):
        self.day=d
        self.month=m
        self.year=y
    def __add__(self,other):
        res=Date(self.day+other.day,self.month+other.month,self.year+other.year)
        a=res.day//30
        b=res.day%30
        res.month=res.month+a
        res.day=b
        c=res.month//12
        d=res.month%12
        res.year=res.year+c
        res.month=d
        return res
    def __str__(self):
        return(str(self.day)+'/'+str(self.month)+'/'+str(self.year))

    def getNepaliDate(self):
        diff = Date(17, 8, 56)
        nep = self + diff
        return nep
    def convertToNepaliChar(self):
        tempy= ""
        tempm=""
        tempd=""
        for i in range(0, len(str(self.year))):
            last = self.year%10
            self.year = self.year // 10
            tempy = chr(2406 + last) + tempy
        for i in range(0, len(str(self.month))):
            last = self.month%10
            self.month = self.month // 10
            tempm = chr(2406 + last) + tempm
        for i in range(0, len(str(self.day))):
            last = self.day%10
            self.day = self.day // 10
            tempd= chr(2406 + last) + tempd
        return Date(tempd,tempm,tempy)


d1=Date(17,6,2019)
d2=d1.getNepaliDate()
print(d2)
print(d2.convertToNepaliChar())



















