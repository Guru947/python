
# *       *     * * * * *     *             *               * * *         *       *       * * *       * * * *       *             * * * *
# *       *     *             *             *             *       *       *       *     *       *     *       *     *             *       *
# * * * * *     * * * * *     *             *             *       *       *   *   *     *       *     * * * *       *             *       *
# *       *     *             *             *             *       *       * *   * *     *       *     *     *       *             *       *
# *       *     * * * * *     * * * * *     * * * * *       * * *         *       *       * * *       *       *     * * * * *     * * * *
n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or j == n or i == n//2+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    for j in range(1,n+1):
        if j==1 or j == 2:
            print(' ',end=' ')
    for j in range(1,n+1):
        if j==1 or i == n or i == n//2+1 or i ==1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    for j in range(1,n+1):
        if j==1 or j == 2:
            print(' ',end=' ')
    for j in range(1,n+1):
        if j==1 or i == n :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    for j in range(1,n+1):
        if j==1 or j == 2:
            print(' ',end=' ')
    for j in range(1,n+1):
        if j==1 or i == n :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    for j in range(1,n+1):
        if j==1 or j == 2:
            print(' ',end=' ')
    for j in range(1,n+1):
        if (j == 1 and 1<i<n) or (i == 1 and 1<j<n) or (j == n and 1<i<n) or (i == n and 1<j<n) :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    for j in range(1,n+1):
        if j<n-1:
            print(' ',end=' ')
    for j in range(1, n + 1):
        if j == 1 or j ==n or (i==j and i>=n//2+1) or ((i+j == n+1)and j<=n//2+1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    for j in range(1,n+1):
        if j==1 or j == 2:
            print(' ',end=' ')
    for j in range(1, n + 1):
        if (j == 1 and 1 < i < n) or (i == 1 and 1 < j < n) or (j == n and 1 < i < n) or (i == n and 1 < j < n):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    for j in range(1,n+1):
        if j==1 or j == 2:
            print(' ',end=' ')
    for j in range(1, n + 1):
        if j == 1 or (i ==1 and j<n) or (i==n//2+1 and j<n) or (j == n and 1<i<n//2+1) or (i==j and i>=n//2+1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    for j in range(1,n+1):
        if j==1 or j == 2:
            print(' ',end=' ')
    for j in range(1,n+1):
        if j==1 or i == n :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    for j in range(1,n+1):
        if j==1 or j == 2:
            print(' ',end=' ')
    for j in range(1,n+1):
        if j==1 or (i ==1 and j<n) or (i == n and j<n) or (j==n and 1<i<n):
            print('*',end=' ')
        else:
            print(' ',end=' ')

    print()


#         *
#       *   *
#     *       *
#   *           *
# *               *
# * * * * * * * * *
# * *           * *
# *   *       *   *
# *     *   *     *
# *       *       *
# *     *   *     *
# *   *       *   *
# * *           * *
# * * * * * * * * *
# *               *
#   *           *
#     *       *
#       *   *
#         *

n = 9
m = n // 2+1
for i in range(1,m+1):
    for j in range(1,n+1):
        if (i+j == m+1) or (j-i == n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i+j == n+1) or (j ==i) or i ==1 or i ==n or j ==1 or j ==n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(1,m+1):
    for j in range(1,n+1):
        if (i==j) or (j+i == n+1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



#### rocket printing programs
n = 9
m = n//2+1
k =m//2+1
e = n//2
print(k)
for i in range(1,k+1):
    for j in range(1,n+1):
        if i+j == m+1 or j-i == m-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(1,m+1):
    for j in range(1,n+1):
        if j == k or j == e+k or (i==1 and k<j<e+k)  :
            print('*',end=' ')
        elif (i==m and k<j<e+k):
            print('-',end=' ')
        else:
            if (j == k-1 and i>=k) or (j == m+k and i>=k):
                print('|',end=' ')
            else:
                print(' ',end=' ')
    print()
for i in range(1,k+1):
    for j in range(1,n+1):
        if j-i == m+1 or i+j == k+1 :
            print('*',end=' ')
        elif i == k:
            print('-',end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(1,k+1):
    for j in range(1,n+1):
        if (j ==k and i<k) or j == k+1 or j == m+1 or (j == m and i<k) or (j == m+k-1 and i<k) :
            print('!',end=' ')
        else:
            print(' ',end=' ')
    print()
