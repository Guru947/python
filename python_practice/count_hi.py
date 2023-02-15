str='abc hi ho'
st = ''
for i in str:
    if i == 'h':
        st += i
    elif i == 'i':
        st += i
        st += " "
print(st)