############### 30/11/21 tuesday
# n = 5
# sum = 1
# for i in range(n+1):
#     if i != 0:
#         sum *= i
#
#     else:
#         break
# print(sum)

# st = 'indiaidd'
# # print(st[::2])
# s =''
# i = 0
# while i<=len(st):
#     if i%2 != 0:
#
#         s+=st[i]
#     i+=1
# print([s])

# s = ''
# for i in range(len(st)):
#     if i%2 != 0:
#        continue
#     else:
#         s += st[i]
# print([s])

#####  separating

# s ='cbhvcgx cg124571357!@$#!^$!%SSGCVHJSGXTY'
# alpha = ''
# ALPHA = ''
# num = 0
# spe = ''
# for i in s:
#     if 'A'<= i <='Z' :
#         alpha += i
#     elif 'a' <= i <= 'z':
#         ALPHA += i
#     elif '0' <= i
# print(num,':numerics:')
# print(spe,':special char:',len(spe))

###???? toggle?

# s ='cbhvcgx cg124571357!@$#!^$!%SSGCVHJSGXTY'
# k = ''
# for i in s:
#     if 'A' <= i <= 'Z':
#         k += chr(ord(i)+32)
#
#     elif 'a' <= i <= 'z':
#         k += chr(ord(i)-32)
#
#     else:
#         k += i
# print(k)

#####[' hay4', 'hai3', 'this4', 'is2'] o/p

var = 'hay hai this is'
list = []
st = ''

for i in var:
    if i == ' ':
        d = str(len(st))
        list +=[st+d]

        st =''
    else:
        st+=i
if st:
    d = str(len(st))
    list+=[st+d]
print(list)


####['yah ', 'iah ', 'siht ', 'si ']


var = 'hay hai this is'
list = []
st = ' '
for i in var:
    if i == ' ':
        st =st[::-1]
        list +=[st]
        st=''
    else:
        st+=i
if st:
    st = st[::-1]
    list+=[st]
print(list)

###

var = 'hay this is not csr'
li1= []
li2=[]
c ={}
st = ''
for i in var:
    if i == ' ':
        li2 += [len(st)]
        li1 += [st]

        st=''
    else:
        st+=i
if st:
    li2 += [len(st)]
    li1 +=[st]

for i in range(len(li1)):
    c[li1[i]] = li2[i]
print('dictionary of given string:',c)

