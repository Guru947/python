# 11 12 13 14 15  16 17 18 19
# 21 22 23 24 25  26 27 28 29
# 31 32 33 34 35  36 37 38 39
# 41 42 43 44 45  46 47 48 49
# 51 52 53 54 55  56 57 58 59

# 61 62 63 64 65 66 67 68 69
# 71 72 73 74 75 76 77 78 79
# 81 82 83 84 85 86 87 88 89
# 91 92 93 94 95 96 97 98 99


n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if (j>= i and i+j <= n+1) :
            print('*',end=' ')
        elif (i>=j and i+j >= n+1 ) :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(1,3):
    for j in range(1,n+1):
        if (i>n//2) :
            print(' ',end=' ')
    print()
for i in range(1,n+1):
    for j in range(1,n+1):


        if (j>= i and i+j >= n+1) :
            print('*',end=' ')
        elif (i>=j and i+j <= n+1 ) :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

a = "i don't Know THat "
r = ' '
for i in a:
    if 'A'<=i<='Z':
        r+= chr(ord(i)+32)
    else:
        r+=i
print(r)

n = 831
temp = n

rem = 0
p = len(str(n))
res = 0
while n>0:
    rem = n%10
    res += rem**p
    n = n//10
if temp == res:
    print(res)
else:
    print( res,'not arm')


n = 145
rem = 0
res = 1
fact = 0
while n>0:
    rem = n%10

    for i in range(1,rem+1):
        res *= i

    n = n//10
    fact += res

    res = 1
print(fact)

print('-----------------------')
n = 6
temp = n

fct = 0
while n>0:
    rem =0
    rem = n%10
    for i in range(1,rem):
        if rem%i == 0:
            fct += i
    n =n//10
print(fct)

import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
n = 24
h =0
for i in range(360):
    c = colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n
    t.color(c)
    t.circle(180)
    t.left(10)





