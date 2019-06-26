class Date:
    def __init__(self,day,month,year):
       self._year=year
       self._month = month
       self._day = day
    def __add__(self,other):
        return self.val+other.val
    def setDate(self,d,m,y):

    def getDay(self):
        return self._day
    def getMonth(self):
        return self._month
    def getYear(self):
        return  self._year
    def __str__(self):
        return ""
myDate=Date(10,11,2019)
print(myDate.getDay())