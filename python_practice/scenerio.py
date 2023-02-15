def no_ears(n,s=0):
    for i in range(1,n+1):

        if i%2 == 0:
            s+=2

        else:
            s+=3

    return s
print(no_ears(10))

def block(n,b=0):
    for i in range(1,n+1):
        b+=i
    return b
num= 5 #int(input('enter the number of layers: '))
print(block(num))

# given a list of intergers return the total num of
a=[1,2,3,4,5,6,7,8,9]
def total(n,tot=0):
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in a:
        if i%n == 0:
            tot +=1
    return tot
print(total(2))

# print('enter the below line:')
# print([i**3 for i in range(1,11) if i%2==0])


# print('enter the values below for list')
# [int(i)**2 for i in input().split()]

def speed(s,b=0,v=0,j=0):

    if s<=(60+b):
        j=0
    elif (61+b)<=s<=(80+b):
        j=1
    elif s>(80+b):

        v=input('Is today is ur BD if yes enter:1 else:0 :')
        if v:
            b=5
        else:
            b=0
        j = 2
    print(j)
# print(speed(90))

var = [1,3,4,5,6,7,8,9]
def abs(var,no_odd=0,no_even=0):
    for i in var:
        if i%2 == 0:
            no_even +=1
        else:
            no_odd += 1
    print('no of ',no_odd-no_even)
abs(var)


