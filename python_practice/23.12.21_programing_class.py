def pal(num,res=0):
    if num<=0:
        return res
    res=res*10+(num%10)
    num//=10
    return pal(num,res)
print(pal(121))


# n = int(input('entre'))
# val = pal(n)
# print(val)
# if val == n:
#     print('palindrome')
# else:
#     print('not pal')


# def per(n,s=0,i=1):
#     if i>=n:
#         return s
#     elif n%i==0:
#
#         s+=i
#
#
#     return per(n,s,i=i+1)
# n =6
# if n == per(n):
#     print('perfect')
# else:
#     print('not perfect')


# def stg(num,res=1,rem=0):
#     if num<=0:
#         return rem
#
#     for i in range(1,(num%10)+1):
#         res*=i
#     num=num//10
#
#     return stg(num,rem=rem+res)
#
# def rg(st,en):
#     for i in range(st,en):
#         if i == stg(i):
#             print(i)
# rg(10,1000)




def sum(num,res=0):
    if num<=0:
        return res
    res +=num%10
    num=num // 10
    return sum(num,res)
# n = int(input('entre the num: '))
# print(sum(17))
# if n == sum(n):
#     print("sum num")
# else:
#     print('nt sum num')
def per(num,temp,res=0):
    if num<=0:
        return res
    elif temp%num == 0:
        res += num
    num-=1
    return per(num,temp,res)
n=6
temp = n
print(per(n-1,temp))






