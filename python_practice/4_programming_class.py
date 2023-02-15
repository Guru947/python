# ord = 49
# n = 5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end=' ')
#     print()
# print()
#
# n = 5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end=' ')
#     print()
#
# n = 5
# for j in range(1,n+1):
#     for i in range(1,n+1):
#         if i<=j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# n = 5
# for j in range(1,n+1):
#     k = 21
#     for i in range(1,n+1):
#         if i>=j:
#             print(k,end=' ')
#             k+=1
#         else:
#             print(' ',end='  ')
#     print()
#
#
# n = 5
# for i in range(1,n+1):
#     k=1+i
#     for j in range(1,n+1):
#         if i>=j:
#             print(k,end=' ')
#             k +=1
#         else:
#             print(' ',end=' ')
#     print()
#
#
# n = 5
#
# for i in range(1,n+1):
#     k = 65 + i -1
#     for j in range(1,n+1):
#         if i<=j:
#             print(' ',end=' ')
#         else:
#             print(chr(k),end=' ')
#             k+=1
#     print()



# var = 'pyspider is very good'
# st = ''
# for i in range(len(var)):
#     if i%2 == 0:
#         st += var[i]
# print(st)







# n = 5
# for i in range(1,n+1):
#     ch =65
#     k = 1
#     for j in range(1,n+1):
#         if i>=j:
#             if i%2 == 1:
#                 print(k,end=' ')
#                 k+=1
#             else:
#                 print(chr(ch), end=' ')
#                 ch+=1
#         else:
#             print(' ',end='')
#     print()




#output
# 1
# A B
# 1 2 3
# A B C D
# 1 2 3 4 5



#-----------------------------------------------------

# n =5
# for j in range(1,n+1):
#     for i in range(1,n+1):
#         if j == n//2+1 or (j == 1 and 1<i<n) or (i ==1 and j>1 ) or (i == n and j>1 ):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()



# output
#   * * *
# *       *
# * * * * *
# *       *
# *       *



#------------------------------------------------



n = 5
for j in range(1,n+1):
    for i in range(1,n+1):
        if (j == n//2+1 and i<n) or(i ==1 ) or (j ==1 and i<n) or (i == n and  1<j < n//2+1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

# * * * *
# *       *
# * * * *
# *
# *

print()

n = 5
for j in range(1,n+1):
    for i in range(1,n+1):
        if (i == n//2+1 and j>2) or (j == i and (i<=3)) or ((i+j)==(n+1) and i>=3):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#output
# *       *
#   *   *
#     *
#     *
#     *

print()
#---------------------------------

n = 5
for j in range(1,n+1):
    for i in range(1,n+1):
        if (i == n//2+1 ) or j==1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#  output
# * * * * *
#     *
#     *
#     *
#     *

print()
#-----------------------------

n = 5
for j in range(1,n+1):
    for i in range(1,n+1):
        if (j == n//2+1 ) or i==1 or i ==n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#   output
# *       *
# *       *
# * * * * *
# *       *
# *       *

print()
#----------------------------------

n = 5
for j in range(1,n+1):
    for i in range(1,n+1):
        if (j ==1 and 1<i<n) or (j ==n and 1<i<n) or (i==1 and 1<j<n) or ( i==n and 1<j<n):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#output
#   * * *
# *       *
# *       *
# *       *
#   * * *

print()
#-----------------------------

n = 5
for j in range(1,n+1):
    for i in range(1,n+1):
        if (i == 1) or (i == n) or (i==j):
            print('*',end=" ")
        else:
            print(' ',end=' ')

    print()

#output
# *       *
# * *     *
# *   *   *
# *     * *
# *       *



print()
n = 5
for j in range(1, n + 1):
    for i in range(1,n+1):
        if (j == n//2+1 and i<n) or(i ==1 ) or (j ==1 and i<n) or (i == n and  1<j < n//2+1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    for i in range(1, n + 1):
        if (i == 1) or i ==2:
            print(' ', end=" ")
    for i in range(1,n+1):
        if (i == n//2+1 and j>n//2) or (j == i and (i<n//2+1)) or ((i+j)==(n+1) and i>n//2+1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    for i in range(1, n + 1):
        if (i == 1) or i ==2:
            print(' ', end=" ")
    for i in range(1,n+1):
        if (i == n//2+1 ) or j==1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    for i in range(1, n + 1):
        if (i == 1) or i == 2:
            print(' ', end=" ")
    for i in range(1,n+1):
        if (j == n//2+1 ) or i==1 or i ==n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    for i in range(1, n + 1):
        if (i == 1) or i ==2:
            print(' ', end=" ")
    for i in range(1,n+1):
        if (j ==1 and 1<i<n) or (j ==n and 1<i<n) or (i==1 and 1<j<n) or ( i==n and 1<j<n):
            print('*',end=' ')
        else:
            print(' ',end=' ')

    for i in range(1, n + 1):
        if (i == 1) or i ==2:
            print(' ', end=" ")
    for i in range(1, n + 1):
        if (i == 1) or (i == n) or (i == j):
            print('*', end=" ")
        else:
            print(' ', end=' ')
    print()

