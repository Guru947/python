# s='cjdbMCKJBCBJNMN'
# k=''
# l=''
# i = 0
# while i<len(s):
#     if 'A'<= s[i]<='Z':
#         k+=s[i]
#     else:
#         pass
#     i +=1
# print(k,':upper case')


st = 'cjdbMCKJBCjvg cx mbn xgvh csfcbnxvBJNMN'
k = ''
i =0
while i<len(st):
    if 'a'<= st[i] <= 'z':
        if i%2 == 0:
            print(i,end=' ')
            k+=st[i]
    i+=1
print(k,len(k))


st = '1h23h7646tf6e874485345ffxfvdghctgnx67JNMN9'
k = ''
i =0
while i<len(st):
    if '0'<= st[i] <= '9' and ord(st[i])%2 == 0:
        k+=st[i]

    i+=1
print(k,'hcb')


s=''
k=''
n= 'hvhjznbgcxvbjkgb25e8ew65@#$%^&%#$%^&*('
for i in n:
    if ord(i)%2 == 0:
        s =' '+ i + s
    else:
        k+=i


print(s)
print(k,end=' ')


