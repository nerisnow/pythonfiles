class stack:
    def __init__(self, *args):
        self.data = list(args)

    def pop(self):
        a = len(self.data)
        if (a==0):
            print('empty')
        else:
            temp=self.data[-1]
            self.data=self.data[0:-1]
            return  temp

    def push(self,item):

        '''a = len(self.data)
        for i in range(0,a-1):
            b = self.data
            self.data[i+1]=self.data[i]

        self.data[-1] = item

        print(self.data)'''
        self.data.append(item)

    def __str__(self):
        blank=""
        blank=blank+str(self.data[0])
        for i in self.data:
            blank=blank+','+str(i)
        return blank

s=stack(1,2,3,4)
print(s.data)
print(s.pop())

print(s.data)
s.push(5)
s.push(6)
s.push(7)
print(s)
