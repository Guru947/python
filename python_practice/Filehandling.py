#  file handling
'''n=int(input('enter the number: '))
def sum(n):
    if n==0:
        return
    print("enter a & b values sum: ")
    a,b=map(int,input().split())
    print(a+b)
    return a+b ,sum(n-1)
sum(n)
fobj = open("filehandlins.txt",'a')
data = ' hi this is chandan bx'
fobj.write(data)
fobj.close()
fobj = open("filehandlins.txt",'r')
data=fobj.read()
print(data)
fobj.close()'''

# File Handling by parsing technique 1.Json 2.pickle
'''
from json import *
original_data=list(range(21))
print(type(original_data))
fobj=open("filehandlins.txt",'w')
json_data=dumps(original_data)
fobj.write(json_data)
print(type(json_data))
fobj.close()
'''
# reading data in json
# from json import *
# fobj=open("filehandlins.txt",'r')
# orinal=fobj.read()
# var=loads(orinal)
# print(var,type(var),sep='\n')
# fobj.close()

# By using pickle
from pickle import *
fobj=open("filehandlins.txt",'wb')
data=[1,2,3,4,5,6,7]
# data="hey this is chandan"
dump(data,fobj)
fobj.close()

from pickle import *
fobj=open("filehandlins.txt",'rb')
var=load(fobj)
print(var)
fobj.close()


