# #####[' hay4', 'hai3', 'this4', 'is2'] o/p
#
# var = 'hay hai this is'
# list = []
# st = ''
#
# for i in var:
#     if i == ' ':
#         d = str(len(st))
#         list +=[st+d]
#
#         st =''
#     else:
#         st+=i
# if st:
#     d = str(len(st))
#     list+=[st+d]
# print(list)
#
#
# ##?? while loop
# var = 'ananconda python very'
# list = []
# st = ''
# i = 0
# while i<len(var):
#     if var[i] ==' ':
#         list += [st]
#         st =''
#     else:
#         st+=var[i]
# if st:
#     list += [st]
# print(list)
#
#
# ####['yah ', 'iah ', 'siht ', 'si ']
#
#
# var = 'hay hai this is'
# list = []
# st = ' '
# for i in var:
#     if i == ' ':
#         st =st[::-1]
#         list +=[st]
#         st=''
#     else:
#         st+=i
# if st:
#     st = st[::-1]
#     list+=[st]
# print(list)
#
# ###
#
# var = 'hay this is not csr'
# li1= []
# li2=[]
# c ={}
# st = ''
# for i in var:
#     if i == ' ':
#         li2 += [len(st)]
#         li1 += [st]
#
#         st=''
#     else:
#         st+=i
# if st:
#     li2 += [len(st)]
#     li1 +=[st]
#
# for i in range(len(li1)):
#     c[li1[i]] = li2[i]
# print('dictionary of given string:',c)


# var = 'ananconda python very'
# list = []
# st = ''
# i = 0
# while i<len(var):
#     if var[i] ==' ':
#         st = st[::-1]
#         list += [st]
#         st =''
#     else:
#         st+=var[i]
#     i += 1
# if st:
#     st = st[::-1]
#     list += [st]
# print(list)
#
#
# var = 'ananconda python very'
# list = []
# st = ''
# i = 0
# while i<len(var):
#     if var[i] ==' ':
#         d = str(len(st))
#         list += [st+d]
#         st =''
#     else:
#         st+=var[i]
#     i += 1
# if st:
#     d = str(len(st))
#     list += [st + d]
# print(list)
#
#
#
#
#
#
#
#
# var = 'ananconda python very'
# li1 = []
# li2 = []
#
# st = ''
# i = 0
# while i<len(var):
#     if var[i] ==' ':
#         d = (len(st))
#         li2 +=[d]
#         li1 += [st]
#         st =''
#     else:
#         st+=var[i]
#     i += 1
# if st:
#     d = (len(st))
#     li2+=[d]
#     li1 += [st]
#
# c={}
# for i in range(len(li2)):
#     c[li1[i]] = li2[i]
# print(c)
#
#

###### nth number of ARMSTRONG number

# num = int(input('enter the number: '))
# temp = num
# res=0
# a = len(str(num))
# for i in range(num):
#     rem = num%10
#     res =res*10 +rem**a
#     num = num//10
# print(res)

# n =145
# t = n
# s=1
# k = 0
# while n>0:
#     rem = n%10
#     print(rem)
#     i = 1
#     while i<=rem:
#         s*=i
#         i+=1
#     k +=s
#     print(k)
#     s= 1
#
#     n = n//10
# if t == k:
#     print('strong')
# else:
#     print('not strong')


# n = 145
# t = n
# r = 0
# f = 1
#
# while n>0:
#     rem = n%10
#     f = 1
#     for i in range(1,rem+1):
# #         f*=i
# #     print(f)
# #     r+=f
#     n = n//10
# print(r)
# if t==r:
#     print('st')
# else:
#     print('nst')
#
#
#
# n = 6
# t = n
# r=0
# for i in range(1,n):
#     if n%i == 0:
#         r+=i
# if r == t:
#     print('perfect number')
# else:
#     print('not perfect num')



# import turtle
# b = turtle.Turtle()
# # b.forward(100)
# # b.left(45)
# # b.forward(100)
# # b.right(90)
# # b.forward(100)
# b.color("red","cyan")
#
#
# b.forward(100)
# b.left(90)
# b.forward(100)
# b.left(90)
# b.forward(100)
# b.left(90)
#
# b.forward(100)
# for i in range(4):
#     b.forward(100)
#     b.right(90)
#
# b.begin_fill()
# b.color("red")
# b.penup()
# b.forward(20)
# b.pendown()
# b.forward(100)
# for i in range(4):
#     b.forward(100)
#     b.right(90)
# b.end_fill()
#
# turtle.done()
# import math
# import turtle
# a = turtle.Turtle()
# a.color("blue","orange")
# a.speed(1000)
#
# a.begin_fill()
# for i in range(1000):
#     a.forward(10)
#     a.left(math.sin(i/10)*25)
#     a.left(20)

# a.end_fill()
#
#
# turtle.done()

# a = 'vakkaliga kottigepally banglore'
# s =''
# j=''
# l1=[]
# d = {}
# l = []
# for i in a:
#     if i !=' ':
#         s= s+i
#         j=i+j
#     else:
#         l+=[s + str(len(s))]
#         d[s]=len(s)
#         l1+=[j]
#         j=''
#         s =''
# if s:
#     l+=[s+str(len(s))]
#     d[s] = len(s)
# if j:
#     l1 +=[j]
#
#
# print(l)
# print(d)
# print(l1)


# v = int(input('enter the number of wheels for 2/4 wheeler vehicle: '))
# w = int(input('enter the number of wheels for vehicle: '))
# v = 200
# w = 540
# z = 540//4
# y = 540//2
# print



#  st='miss' o/p =
# st = "abc"
# l = list(st)
# print(l)
#
# for i in range(len(l)-1):
#     l[i],l[i+1] = l[i+1],l[i]
#     s = ''
#     for j in l:
#         s+=j
#     print(s)
#
# i = 0
# while i<len(l)-1:
#     l[i], l[i + 1] = l[i + 1], l[i]
#     s = ''
#     j =0
#     while j<len(l):
#         s+=l[j]
#         j+=1
#     i+=1

    # print(s)
from math import *
l = [1,2,3,4,5,6,7,8,9]
b = int(sqrt(len(l)))
i =0
while i<b:
    j=0
    while j<len(l):
        if j%3 = 0:
            print(j)
            break
        j+=1
    i+=1
    print()











