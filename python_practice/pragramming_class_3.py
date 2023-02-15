# n =153
# n1 = n
# n2 = n
# s = 0
# c = 0
# c1 = c
# sum1 = 0
# while n1 > 0:
#     n1 = n//10
#     c +=1
# while n>0:
#     rem = n%10
#     sum += rem ** c
#     n = n//10
#     print(sum)
#
# if sum1 == n2:
#     print('its armstrong num')
# else:
#     print('its not armstrong')


# arthamatic operations
# a = int(input('enter the first num:'))
# b = int(input('enter the 2nd num'))
# c =input('enter the operator:')
# if c== '+':
#     sum = a+b
#     print(sum)
# elif c=='-':
#     sub = a-b
#     print(sum)
# elif c == '/':
#     div = a/b
#     print(div)
# elif c =='*':
#     mal = a*b
#     print(mal)
# elif c == '**':
#     pow= a**b
#     print(pow)
# else:
#     print('enter input first')
#
# a = 12
# b = 14
# ch=input('enter 1 to add, 2 to sub,3 to mal,4 to div:')
# if ch not in '1234':
#     print('enter the valide choice')
# else:
#     a = int(input('enter the value'))
#     b = int(input('enter the value'))
#
#     if ch =='1':
#         print(a+b)
#     elif ch == '2':
#         print(a-b)
#     elif ch == '3':
#         print(a*b)
#     else:
#         print(a/b)

# a = int(input('enter the marks b/w 0 to 100:'))
# if a<0 or a>100:
#     print('number is not-valide')
# else:
#
#     if 90<= a <= 100 :
#         print('S+')
#     elif 80<= a < 90:
#         print('A+')
#     elif 70 <= a <80:
#         print('A')
#     elif 60 <= a <70:
#         print('B+')
#     elif 50 <= a <60:
#         print('B')
#     elif 35 <= a <50:
#         print('C')
#     else:
# #         print('fail')
# a = int(input('enter the number'))
# b = int(input('enter the number'))
# c= int(input('enter the number'))
# d = int(input('enter the number'))
#
# c=[a,b,c,d]
# print(max(c))
n = 5
for i in range(0,n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print()













