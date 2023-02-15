def display(x):
    return x+25
print(display(10))

var=lambda x: x+25
print(var(10))

var1 =lambda x,y,a:x*y**a
print(var1(2,3,4))

lis=list(range(20))
lis=list(filter(lambda num:num%4==0 and num%8==0,list(range(100))))
print(lis)

lis1=list(map(lambda num:num*num,list(range(11))))
print(lis1)

# a=10
# lam=list(filter(lambda a:"even" if a%2==0 else "odd",lis))
# print(lam(10))




def prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True


# col=[3,4,5,6,7,8,9]
print(list(filter(lambda num1:prime(num1),list(range(100)))))



