import os

searchWord=input("enter word to search")
location=input("enter location to search")


print(os.getcwd())
os.chdir(location)
print(os.getcwd())
fileList=os.listdir()


for lists in fileList:
    if(os.path.isdir(lists)):
        os.chdir(location+"/"+lists)
        fileList1=os.listdir()
        for list1 in fileList1:
            folder=open(list1)
            i=1
            for text in folder.readlines():
                if searchWord in text:
                    print('found')
                    
                    print(i)
                i = i + 1

    else:
        file = open(lists)
        path = file.readlines()
        i = 1
        for line in path:
            if searchWord in line:
                print('found')

                print(i)
            i = i + 1