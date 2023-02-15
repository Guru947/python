
print('strong number using recursion and loops')

def strong(num,res=0,rem=1):
    if num<=0:
        return res
    for i in range(1,(num%10)+1):
        rem*=i
    num//=10
    return strong(num,res=res+rem,rem =1)
n=145

print(strong(n))

print('-----------------------------------------')


print('strong number using complete  recurtion without loops')


def fct(n,r=1,rt=1):
    if r >= n+1:
        return rt
    rt *=r
    r+=1
    return fct(n,r,rt)
def str(num,res=0):
    if num<=0:
        return res
    rem=num%10
    res += fct(rem)
    num//=10
    return str(num,res)
print(str(145))

print('----------------------------------------------')
print('add key:value pair to dict')


var=['hey','hello','hii','bye']
def dict(*args):
    print(*args)

print(dict('hey','hello','hii','bye'))


c = 1
d = 20
for i in range(10):
    print(('*'*c).center(d))
    c +=2
print('| |'.center(d))

print('-------------------------')
def dict(var,teemp='',res={},i=0):

    if i>=len(var):
        if :
            res[teemp]=len(teemp)
        return res
    elif var[i] != ' ':
        teemp += var[i]

    elif var[i] == ' ':
        res[teemp] = len(teemp)
        teemp =''

    return dict(var,teemp,res,i=i+1)



var='python is easy'
print(dict(var))

a=[20,17,19,100,3]
for t in range(0,len(a)-1):
    if a[t]>a[t+1]:
        a[t],a[t+1]=a[t+1],a[t]
print(a)
a=[20,17,19,100,3]
for i in range(0,len(a)):
    for t in range(0,len(a)-1):
        if a[t]>a[t+1]:
            a[t],a[t+1]=a[t+1],a[t]
print(a)
a=[20,17,19,100,3]
for passno in range(1,len(a)+1):
    minp
