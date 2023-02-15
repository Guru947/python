def asa(a,i=0,out={}):
    if i>=len(a):
        return out
    else:
        out[a[i]] =len(a[i])
    return asa(a,i+1,out)
a=['Python','BangloRe']
print(asa(a))

# def cap(d,i=0,res=[],temp=''):
#
#     if i >= len(d):
#         return res
#
#     for j in d[i]:
#         if d[i][1]:
#             temp += d[i][1]
#         elif 'A' <= j <= 'Z':
#             temp += chr(ord(j)+34)
#         else:
#             temp += j
#     res+=temp
#     temp=''
#
#     i+=1
#     return cap(d,res,temp,i)
# d=['Python','BangloRe']
# result = cap(d)
# print(result)

def cap(d,i=0,res=[],temp='',j=0):

    if i >= len(d):
        return res
    if 'A' <= d[i][0] <= 'Z':
        for j in range(len(d[i])):
            if j==0:
                temp += d[i][0]
            elif 'A' <= d[i][j] <= 'Z':
                temp += chr(ord(d[i][j])+32)
            else:
                temp += d[i][j]
        res += [temp]
        temp = ''
    else:
        pass
    return cap(d,i+1,res,temp,j=0)
d=['Python','BangloRe','testYantra','BASAVANGUDI']
result = cap(d)
print(result)

# str='hey hello how are '
# st=str.split()
# print(st)

def dict(st,out={},i=0):
    if i >= len(st):
        return  out
    if st[i] in 'AEIOUaeiou':
        out[st[i]]=ord(st[i])
    else:
        out[st[i]]=1
    return dict(st,out,i+1)
st='aemcns'
print(dict(st))

def fro(li,sum=0,i=0):
    if i>=len(li):
        return sum

    if len(str(li[i]))==4:
        sum+=li[i]
    return fro(li,sum,i+1)
li=[1,234,3454,7634,9868,15318,67876,8765]
print(fro(li))

def conting(a,res=[],c=0,i=0):
    if i>=len(a):
        return res
    for j in a[i]:
        if '0'<=j<='9':
            c+=1
    res+=[c]
    c=0
    return conting(a,res,c,i+1)
list=['hai1','21a22','corona321','hello']
print(conting(list))