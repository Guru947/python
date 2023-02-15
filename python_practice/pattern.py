# n = 5
# for i in range(n-1):
#     for j in range(i+1):
#         print('*',end=' ')
#     for j in range(n-i-2):
#         print('#',end=' ')
#     for j in range(n-i-1):
#         print('#',end=' ')
#     for j in range(i+1):
#         print('*',end=' ')
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(' ',end=' ')
#     for j in range(n-i-1):
#         print('*',end=' ')
#     for j in range(n - i - 2):
#         print('*', end=' ')
#     print()


# n = 2
# for i in range(n):
#     for j in range(1):
#         print('*',end='')
#     for j in range(3):
#         print('-',end='')
#     for j in range(1):
#         print('*', end='')
#     print()


a = 'hello'
b = 'l'
s=0
i =0
while i<len(a):
    if b == a[i]:
        s+=1
    i +=1
print(s)

i = 0
while i<len(a):
    j =0
    k =0
    print(i,end=' ')
    while j<len(a):
        if a[j] == a[i]:
            k += 1

        j+=1
        

    i +=1



a = 'hey'
sp ='r'
i =0
c =0
while i<len(a):
    if i%2 ==0 and a[i] == sp:
        c += 1

    i+=1
print(c,sp)
a ='hey'
d ={}
for i in range(len(a)):
    d[a[i]] = i


print(d)


#
# n = 4
# num = 1
# for i in range(n):
#     num =1
#     for j in range(i+1):
#         print(num,end=' ')
#         num+=1
#     for j in range(n-i-1):
#         print(" ",end=' ')
#     for j in range(n-i-1):
#         print(" ",end=' ')
#     num = i+1
#     for j in range(i+1):
#         print(num,end=' ')
#         num -=1
#
#     for i in range(n):
#         for j in range(i):
#             print('#',end=' ')
#     for j in range(2):
#         print('*',end="")
#
#     print()
# for i in range(n*2):
#     print('*',end=' ')
# print()
#
# for i in range(n):
#     a = 65
#     for j in range(n-i):
#         print(chr(a),end=' ')
#         a+=1
#     for j in range(i):
#         print(' ',end=' ')
#     for j in range(i):
#         print(' ', end=' ')
#
#     for j in range(n-i):
#         print(chr(a),end=' ')
#         a-=1
#     print()


st ='IndIyana'
i,b = 0,0
while i<len(st):
    if st[i] in 'AEIOU':
        b+=1
    i+=1
print(b)

c =0
for i in st:
    c +=1
print(c,'len')

st ='extract'
c =''
d =''
for i in range(
        len(st)):
    if i%2 == 0:
        c+=st[i]
    else:
        d+=st[i]
print(c)
print(d)


#odd index and lowercase
st ='accurence'
c =0
d=''
for i in range(0,len(st)):

    if (i)%2 == 1 and 'a' <= st[i] <= 'z':
        d+=st[i]
        c +=1
print(c,d,':odd index char')


### 3-digits numbers present in list

l = [1,23,456,789,455,8642]
c =[]
for i in l:
    if 99< i <= 999:
        
        c +=[i]
print(c,'3dit')


var = {'a':1,'b':2,'c':3}
var1 = {'x':1,'y':2,'z':3}
for i in var1:

    var[i] = var1[i]

print(var)

res ={}
for i in (var,var1):
    for j in i:
        res[j]=i[j]
print(res)






c =0
st =''
res ={}

a =['facebook.com','instgram.com','olk.in']
for j in a:
    st=''
    c =0
    for i in j:

        if i != '.' and c == 0:
            st +=i
        elif i == '.':
            c +=1
        else:
            c+=1
    res[st] = c-1
print(res)

# n = int(input('entre number of num'))
# a=[]
# for i in range(n):
#     b =print('enter the to add: ')
#     a.append(b)


var =['facebook..com','goougle123.com.in']
res ={}
for i in var:

    st = 0
    st1 =0
    for j in i:
        if 'A'<= j <='Z' or 'a'<=j<='z':
            st+=1
        else:
            st1+=1
    res[st] = st1
print(res)







