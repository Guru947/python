x = [0, 1, 1, 2, 3, 5, 8]

import sys
sys.setrecursionlimit(20)
print(sys.getrecursionlimit())
def fibonachi(n):
    a = 0
    b = 1
    print(a, b, end=' ')
    i = 0

    for i in range(2, n):
        c = a + b
        a = b
        b = c
        i +=1
        print(c, end=' ')
        print(i,end='')
    print()
    # fibonachi(n)
# n = 10
# fibonachi(n)


def pal(num,res=0):
    if num<=0:
        return res
    rem = num%10
    res = res*10 + rem
    num = num//10
    return pal(num,res)
n=121
res = (pal(n))
if n == res:
    print('palindrome')
else:
    print('not palindrome')
