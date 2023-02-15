# def add(a,b):
#     return a+b
# def mal(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# def pow(a,b):
#     return a**b
# def get_data():
#     a = int(input('enter 1st number: '))
#     b = int(input('enter 2st number: '))
#     return a,b
#
# # ap = int(input('1 fro +,2 fro *,3 for /, 4 for **,5 for stop'))
# # a = int(input('enter 1st number'))
# # b = int(input('enter 2st number'))
#
#
# # while True:
# #     ap = int(input('1 fro +,2 fro *,3 for /, 4 for **,5 for stop: '))
# #
# #     if ap == 1:
# #         data=get_data()
# #         print(add(*data))
# #     elif ap == 2:
# #         data = get_data()
# #         print(mal(*data))
# #     elif ap == 3:
# #         data = get_data()
# #         print(div(*data))
# #     elif ap == 4:
# #         data = get_data()
# #         print(pow(*data))
# #     elif ap == 5:
# #         print('calculaton is stopped.')
# #         break
# #     else:
# #         print('wrong input or enter above mentioned value')


# is num is prime r not
#def prime(n):
#     if n == 1:
#         return 'prime num'
#     for i in range(2,n):
#         if n%i == 0:
#             return 'not prime'
#     return 'prime num'
# num = int(input('enter the num: '))
# print(prime(num))


# to print prime number range of m to n:
# def prime(n):
#     if n == 1:
#         return 'prime num'
#     for i in range(2,n):
#         if n%i == 0:
#             return 'not prime'
#     return 'prime num'
# def ps(m,n):
#     for i in range(m,n):
#         if prime(i) == 'prime num':
#             print(i,end=' ')
#
# ps(3,15)

def perfect(n):

    s = 0
    for i in range(1,n):
        if n%i == 0:
            s+=i
    return n==s
    # if n == s:
    #     print('perfect num')
    # else:
    #     print('not perfect')
# print(perfect(7))


def fact(n):
    if n==1:
        return

    return n*fact(n-1)
# print(fact(5))



def f(n,s=1):
    s=s*n
    if n==1:
        return
    f(n-1,s)
    return s
# print(f(5))

#armstrong number n=153
def(num,sum = 0):
    