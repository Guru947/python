# var = 'hello world @12345'
# rev = ''
# res = ''
# for i in var:
#     if 'a'<= i <='z' or 'A'<= i <='Z' or '0'<= i <='9':
#         rev =i + rev
#     else:
#
#         res+=rev
#         res += i
#         rev =''
# if rev:
#     res +=rev
# print(res)

#/ by 3&5
# a = int(input('enter the number: '))
# if a%3==0 and a%5==0:
#     print('the given input is divisible by 3&5')
# else:
#     print('number not divisible by 3&5')

#   /3 or 5
# a = int(input('enter the number: '))
# if a%3==0 or a%5==0:
#     print('the given input is divisible by 3 or 5')
# else:
#     print('number not divisible by 3 or 5')

#  string polindrome
# a = input('enter the string: ')
# res = ''
# for i in a:
#     res = i + res
# if a == res:
#     print('polindrome')
# else:
#     print('not a polindrme')


# maltiples of 5
# a = int(input('entre the number: '))
# if a%5 == 0:
#     print('the given num is div by 5')
# else:
#     print('the num is not div 5')


# /3&5, /3 =p>fizz /5>buzz /3&5 > fizz_buzz
# a = int(input('entre the number: '))
# if a%3== 0 and a%5 ==0:
#     print('fizz buzz')
# elif a%3== 0 :
#     print('fizz')
# elif a%5 ==0:
#     print(' buzz')
# else:
#     print('buzz_fizz')

# max of 3 numbers
# a = int(input('entre the number1: '))
# b = int(input('entre the number2: '))
# c = int(input('entre the number3: '))
# if a>b and a>c:
#     print('a is greater')
# elif b>a and b>c:
#     print('b is greater')
# else:
#     print('c is greater')


# input special,alpha,small
# var ='hnjcncnmnhgyeMCJSBCBHJCMLN#$%^&*(*&^%$#@#$%^&*('
# spe =''
# alpa = ''
# cap =''
# for i in var:
#     if 'a'<= i<='z':
#         alpa+=i
#     elif 'A'<= i <= 'Z':
#         cap+=i
#     else:
#         spe+=i
# print(spe,':speacial symbols')
# print(alpa,':alpabets')
# print(cap,':capital lettters')


# replacing special with *
# var ='hnjcncnmnhgyeMCJSBCBHJCMLN#$%^&*(*&^%$#@#$%^&*('
# spe =''
#
# for i in var:
#     if 'a'<= i<='z':
#         spe += i
#     elif 'A'<= i <= 'Z':
#         spe+=i
#     else:
#         spe+='*'
# print(spe)


### square of even number present inside the input list

# var =[]
# for i in range(11):
#     if i%2 == 0:
#         var +=[i**2]
# print(var)


### wap to find sum of all number present inside list of collections


# list = [11,12,13,15,17,19,21,31,41,51,61,71,81,91,10]
# res = 0
# for i in list:
#     if i%2 == 1:
#         res+=i
#
# print(res)


# ### 3 tables
# for i in range(1,11):
#     print('3*',i,'=',3*i)


var = ['venugopal','python']
for i in var:
    st =''
    st1 =''
    st2 =''
    for j in range(len(i)):
        if j <2:
            st +=i[j]
        elif j >= (len(i)-2):
            st1 += i[j]
        else:
            st2 += i[j]

    print(st1+st2+st)






