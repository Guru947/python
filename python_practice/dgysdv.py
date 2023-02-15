# wap to find factors of a number user input


# def fact(n):
#     num = 0
#     for i in range(1,n+1):
#         if n%i == 0:
#             print(i,end=' ')
# n = int(input("enter the number: "))
# fact(n)

# leap year

# def leap_year(n):
#     if n%4==0 and n%400==0 :
#         print('leap year')
#     elif n%4==0 and n%100 !=0:
#         print("leap year")
#     else:
#         print("not a leap year")
#
# n = int(input('enter the num: '))
# leap_year(n)


# class natural:
#     def __init__(self, n):
#         self.n = n
#     def __iter__(self):
#         self.i = 1
#         return  self
#     def __next__(self):
#         if self.i<=self.n:
#             res = self.i
#             self.i += 1
#             return res
#         raise StopIteration
# a = natural(10)
# print(list(a))

s = 'abcdeanbv'
l = list(s)
# print(l.index('a'))
print(l)
l[5]='0'
l=''.join(l)
print(l)




















