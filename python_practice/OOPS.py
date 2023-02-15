# class school:
#     school_name='Qspider'
#     principle ='kashi'
#
# #objectName=className()
# dinga = school()
# print(dinga)
# print(school.__dict__)
# print(dinga.school_name)

# class rev_str:
#
#     def rev(self):
#         var=input('enter the str: ')
#         res =''
#         for i in var:
#             res = i + res
#         print(res)
# obj=rev_str()
# obj.rev()

# var=(1,2.3,5.6,8.999,1.0001,89.757)
# def fract(tup,sum=0):
#     for i in tup:
#         j=str(i)
#         c=0
#         st=''
#         for k in j:
#             if k == '.':
#                 c =0
#                 st=''
#             else:
#                 c += 1
#                 st += k
#         if c>2:
#             sum += float(i)
#     print(sum)
# fract(var)

# class clg:
#     fname='hii'  #generic data varname = value
#     lname='bye'
#     Fname='maybe'
# # objname =classname()
# k =clg()
# ka =clg()
# Fname='maybe'
# k.fname='gandu'
#
# # k.fname='gandu'
# print(clg.fname,clg.lname,clg.Fname)
# print(k.fname,k.lname,k.Fname)
# print(ka.fname)

# class sbi:
#     bName='sbi'
#     loc='basavangudi'
#     ceo='ps'
# vamsi=sbi()
# rohit=sbi()
# # change generic data by using class name
# #classname.variable=value
# print(vamsi)
# print(rohit)
# vamsi.bName='canara'
# sbi.bName='ib'
# print(f"the bank name of vamshi {vamsi.bName} and company is {vamsi.ceo}")
# print(sbi.bName,sbi.ceo)
#
# vamsi.ceo='pm'
# print(f"the bank name of vamshi {vamsi.bName} and company is {vamsi.ceo}")
# del vamsi.bName
# print(f"the bank name of vamshi {vamsi.bName} and company is {vamsi.ceo}")


# def increament1(st,j=0,temp=''):
#     if j>=len(st):
#         return temp
#     if j == 0 and 'a' <= st[j] <= 'z':
#         temp += chr(ord(st[j]) - 32)
#     elif j != 0 and 'A' <= st[j] <= 'Z':
#         temp += chr(ord(st[j]) + 32)
#     else:
#         temp += st[j]
#     return increament1(st,j+1,temp)
#
#
# a=['BangloRe','pyTHon','DeVELPor']
# def recur(a,i=0,sum=[]):
#     if i>=len(a):
#         return sum
#     temp=increament1(a[i])
#     sum +=[temp]
#
#     i+=1
#     return recur(a,i,sum)
# print(recur(a))
#
#
# class trip:
#     place = 'paris'
#     plane ='Air india'
#     cost = 11000
#     type ='round'
# f_trip = trip()
# print(trip.place, trip.plane, trip.cost, trip.type)
# print(f"i'm to going to plane trip to '{f_trip.place}' through '{f_trip.plane}' so i have discount it will cost around '{f_trip.cost}' it is for '{f_trip.type}'.")
# trip.type='single'
# print(f"i'm to going to plane trip to '{f_trip.place}' through '{f_trip.plane}' so i have discount it will cost around '{f_trip.cost}' it is for '{f_trip.type}'.")
# del trip.type
# print(f"i'm to going to plane trip to '{f_trip.place}' through '{f_trip.plane}' so i have discount it will cost around '{f_trip.cost}' it is for .")
#
#
# class sbi:
#     b_name="sbi"
#     loc='Banglore'
#     b_manager='denga'
#     b_code='SBIN00098'
#
# nithin = sbi()
# abhishek = sbi()
# nithin.name = 'nithin'
# nithin.balance = 10000
# abhishek.name='abhi'
# abhishek.balance = 11100
# print(abhishek.name,nithin.balance)
# print(abhishek,nithin)
# sbi.name='hey'
# print(sbi.name)
#
# def not_str(str):
#     temp =str.split()
#     if 'not' in temp[0]:
#         return str
#     else:
#         return 'not '+str
#
# def hour(a,b,c):
#     x=30
#     A=a*x
#     y = 6
#     B=b*y
#     C=0
#
#     if (A-B)<0:
#         C=(A-B)*-1
#     else:
#         C= A-B
#
#
#     return C+0.00
# print(hour(0,55,0))
#
#




# creating class with respect to method to take inputs and display

class rcb:
    owner ='moulya'
    coach ='sanjay'
    def __init__(self,name,age,sal,jerseyno):
        self.name=name
        self.age=age
        self.sal=sal
        self.jerseyno=jerseyno
    def display(self):
        
        print(self.owner)
        print(self.coach)
        print(self.name)
        print(self.age)
        # print(self.sal)
        print(self.jerseyno)
    def change_jerseyno(self,new_jerseyno):
        self.jerseyno=new_jerseyno
    def del_sal(self):
        del self.sal
p1=rcb('virat',31,'17cr',18)
p1.change_jerseyno(10)
p2=rcb('siraj',28,'7cr',73)
p2.change_jerseyno(00)
p1.display()
print("*"*20)

rcb.display(p2)
p2.del_sal()
print('-'*20)
rcb.display(p2)










