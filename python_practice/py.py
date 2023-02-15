# n = int(input('enter the num '))
# for i in range(2,n):
#     if n%i == 0:
#         print(n,'not prime')
#         break
# else:
#     print(n,'prime num')
# i = 0
# j = 2
# while j<i:
#
#     if i%j == 0:
#         print('not prime')
#         break
#     else:
#         print('prime nu',n)
#     i+=1


## printing prime number
###### for i in range(sp,ep+1)
#####      for j in range(2,i)


# n = 100
# for i in range(1,n):
#
#     for j in range(2,8):
#         if i%j == 0:
#
#             break
#     else:
#         print(i,end=' ')

m = [   i for i in range(10) if i>5 ]
print(m)

# m = 0
# n = 100
# while m<=n:
#     i = 1
#     f = 0
#     while i<m:
#         if m%i== 0:
#             f += 1
#             break
#         else:
#             print(m,end=' ')
#         i+=1
#
#     m+=1
# if f == 0:
#     print(m)
#### prime r not prime by while

# i = 0
# j = 2
# n = 11
# while j<n:
#     if n%j == 0:
#         print('not prime')
#
#
#         i +=1
#         break
#
#     j += 1
# else:
#     print('prime number')


# a = int(input('enter the side lenth a; '))
# b = int(input('enter the side lenth b; '))
# c = int(input('enter the side lenth c; '))
# d = int(input('enter the side lenth d; '))
#
# if a==b and b==c and c==d and d==a:
#     print('square')
# elif a==b and c==d:
#     print('rectanle')
# elif a==c and b==d:
#     print('rectanle')
# else:
#     print('any quadrangle')



#### for cheking triangle



# if a == b == c:
#     print('equatral')
# elif a==b or c==a or b == c:
#     print('isosoes')
# else:
#     print('scaler triangle')

#### range 50 to 200 even r odd

# a = (input('enter the side lenth a; ')).lower()
# b = int(input('enter the side lenth a; '))

# if  50<= a <= 200:
#     if a%2 ==0:
#         print('even number')
#         print(a**2)
#     else:
#         print('odd number')
#
#         print(len(str(a)))
# else:
#     print('invalide input')


# sum = 0
# while a<=b:
#     sum+=a
#     a+=1
# print(sum)

# sum = 0
# while a<=b:
#     if a%2 !=0:
#
#         sum+=a*a
#         print(sum,a)
#
#     a+=1
#
# print(sum)


# n = 5
# sum = 1
# i = 1
# while i<=n:
#     sum *= i
#     i +=1
#
#
# print(sum)
k = ''
e =[]
s = 'hai this is nan'
for i in s:
    if i != ' ':
        k+=i
    else:
        e +=[k]
        k = ' '
if k:
    e+=[k]
print(e)

















