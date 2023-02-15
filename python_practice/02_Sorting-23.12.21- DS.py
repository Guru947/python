# se = {1, 2, 3, 4, 'hey', 'nhvc'}
# st = str(se)
# res = ''
# i = 0
# while i<len(st):
#     if st[i]=='{' or st[i] == '}':
#         pass
#     elif st[i] == ',':
#         print(str(res),end=' ')
#         res = ''
#     else:
#         res+=st[i]
#     i+=1
# if res:
#     print(str(res),end=' ')
# st ='Apple'
# c = ''




#selection sort()
# a = [1,4,3,5,2]
# for passno in range(1,len(a)):
#     minp = passno-1
#     for i in range(minp+1,len(a)):
#         if a[minp]>a[i]:
#             minp = i
#     a[passno-1], a[minp] = a[minp], a[passno-1]
# print(a)

# bubble sort()
# a = [1,4,3,6,2]
# for passno in range(1, len(a)):
#     x=passno-1
#     for i in range(x+1,len(a)):
#         if a[x]>a[i]:
#             a[x],a[i]=a[i],a[x]
# print(a)


# insetion sorting
# a = [1,4,3,6,5,2,8,1,7]
# for passno in range(1,len(a)):
#     i=passno
#     while i!=0 and a[i]<a[i-1]:
#         a[i],a[i-1] = a[i-1],a[i]
#         i-=1
# print(a)

# a=['hia',1,3.4,6,7,'byee',{1,2,3,4},('hcncc','123')]
# res=[]
# for i in a:
#     if type(i) in[int,float,complex,bool]:
#         res+=[1]
#     else:
#         res+=[len(i)]
# print(res)

# from calendar import *
# y = 2021
# m = 1
#
# print(month(y,m))


### strong number using recursion

#
#
def prime(n,i=2,c=0):
    if i>=n-1:
        if c == 0:
            print('prime')
        else:
            print('not prime')
        return
    elif n%i == 0:
        c+=1
    i+=1
    return prime(n,i,c)
def rec(a,i = 0,s='',c=0):
    if i>=len(a):
        return (c+1)//len(s),s
    if a[i] not in s:
        s+=a[i]
    elif a[i] == s[0]:
        c+=1
    i+=1
    return rec(a,c,s,i)
a='abcdefghabcdefghabcdefghabcdefgh'
print(rec(a))

def rec(a,i=0,res={},temp=''):
    if i>=len(a):
        if temp:
            res[temp]=len(temp)-1
        return res
    if a[i] == ' ':
        res[temp]=len(temp)-1
        temp=''
    else:
        temp += a[i]
    i +=1
    return rec(a,i,res,temp)
a='python training institute'
print(rec(a))

# def cap(d,i=0,res=[],temp=''):
#     if i >= len(d) :
#         return res
#     if 'A'<= d[i][1]<='Z':
#         for j in d[i]:
#             if d[i][1]:
#                 temp += d[i][1]
#             elif 'A' <= j <= 'Z':
#                 temp += chr(ord(j)+34)
#             else:
#                 temp +=j
#         res+=temp
#         temp=''
#     else:
#         pass
#     i+=1
#     return cap(d,res,temp,i)
# d=['Python','BangloRe']
# print(cap(d))



















