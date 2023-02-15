# class person():
#
#     def __init__(self,x,y):
#         self.name=x
#         self.age=y
#
#     def display(self):
#         print("name of person is: ",self.name)
#         print("age of the person is: ",self.age)
#
# class student(person):
#
#     def __init__(self, x, y, Sid,z,C_name):
#         super().__init__(x, y)
#
#         self.Sid=Sid
#         self.Spercentage=z
#         self.C_name=C_name
#
#     def display(self):
#         super(student, self).display()
#
#         print("student id:",self.Sid)
#         print("student percentage is: ",self.Spercentage)
#         print("student college name is: ", self.C_name)
#
#
#
# s1=student('chandan',22,"1JT17ME008",70,"jit")
# s1.display()

# def xyz_there(str):
#     str1 = str.split('.')
#     print(str1,len(str1),str1[0],str1[1])
#
#     if 'xyz' in str1[0]:
#         return True
#     elif len(str1)>=2:
#         if 'xxyz' in str1[1]:
#             return True
#         elif 'xyzxyz' in str1[1]:
#             return True
#         elif 'xyz' in str1[1]:
#             return True
#     else:
#         return False
# print(xyz_there('ayc.xyz'))
import math
import re


def mini(s):
    sl=[]
    Stuart=0
    Kevin=0
    kl=[]
    for i in range(len(s)):
        if s[i] in 'AEIOU':
            for j in range(i,len(s)):
                if s[i:j+1] not in kl:
                    kl+=[s[i:j+1]]
        else:
            for k in range(i, len(s)):
                if s[i:k + 1] not in sl:
                    sl += [s[i:k+1]]
    for m in sl:
        match=re.findall(m,s)
        Stuart += len(match)
    for n in kl:
        mat=re.findall(n,s)
        Kevin += len(mat)


    print(kl,Kevin)
    print(sl,Stuart)



# mini('BANANA')

def grading(g):
    sum=[]
    rem=0
    for i in g:
        if i<5:
            pass
        else:
            if 5<=i<38:
                sum+=[i]
            elif (i%5>=3):
                sum+=[i+(5-(i%5))]
            else:
                sum+=[i]
    return sum


print(grading([4,73,67,38,33,37,35]))

