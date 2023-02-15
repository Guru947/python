#W.a.P to create classes called a resume, resume1,resume2 uosing mutilevel inheritance and use of constructor chaining and mwthod chaing in it.


class resume():

    def __init__(self,name,age,edu):
        self.name=name
        self.age=age
        self.p_edu=edu
    def get_method(self):
        return self.name
class resume1(resume):

    def __init__(self,name,age,p_edu,S_edu,perc):
        super().__init__(name, age, p_edu)
        self.S_edu=S_edu
        self.Perc=perc
class resume2(resume1):

    def __init__(self,name,age,p_edu,S_edu,perc,d_edu,d_perc):
        super(resume2, self).__init__(name,age,p_edu,S_edu,perc)
        self.D_edu=d_edu
        sel.D_perc=d_perc

    def get_method(self):
        return super(resume2, self).get_method()

# obj=resume2('chandan',22,"ghs","vpu",78,"jit",70)
# obj.get_method()


class Resume:
    qual='10th'
    def __init__(self,name,ph_no,email,addr,Tyop,Tp):
        self.name=name
        self.phone_no=ph_no
        self.email=email
        self.address=addr
        self.Ten_pass_out=Tyop
        self.Ten_YEAR=Tp
    def display(self):
        print(self.name,self.phone_no,self.email,self.address,self.Ten_pass_out,self.Ten_YEAR,sep='\n')
    def change_no(self,new):
        self.phone_no=new
class Resume1(Resume):
    Qual='12th'
    def __init__(self,name,ph_no,email,addr,Tyop,Tp,twyop,Twp):
        super().__init__(name,ph_no,email,addr,Tyop,Tp)
        self.Twyop=twyop
        self.T_percentage=Twp
    def display(self):
        super().display()
        print(self.Twyop,self.T_percentage,sep='\n')
class Resume2(Resume1):
    qual = 'degree'
    def __init__(self,name,ph_no,email,addr,Tyop,Tp,twyop,Twp,Dyop,Dp):
        super().__init__(name,ph_no,email,addr,Tyop,Tp,twyop,Twp)
        self.DYOP=Dyop
        self.Dp=Dp
    def display(self):
        super(Resume2, self).display()
        print(self.DYOP,self.Dp,sep='\n')

# obj1=Resume2('Chandan BV',7338042598,'chandanreddybv99@gmail.com','banglore',2015,76,2017,78,2021,70)
# obj1.display()

def house(n):
    str1=[]
    str2=[]
    for i in n:
        if i%2!=0:
            str1 += [i]
        else:
            str2+=[i]
    str1.reverse()
    return str1+str2
# print(house([1,2,3,4,5,6]))

def sep(m):
    c=0
    str1=''
    list=[]
    for i in m:
        if i<0:
            c+=1
            str1+=str(abs(i))
        else:
            str1+=str(i)
    if c%2 !=0:
        print(-int(str1))
    else:
        print(int(str1))

# sep([0,-7,-8,9])

class pc:
    a=10
    b=11
class a(pc):
    c=29
class b(pc):
    pass
abc=b()
print(abc.a,abc.b)

class Testyanntra:
    Iname=''
    CEO="Mr. Girish"
    C_addr="Basavanagudi-Bengaluru"
    def __init__(self,name,phno,addr,mail,dyop,dp):
        self.name=name
        self.phone_number=phno
        self.addreass=addr
        self.mail=mail
        self.dyop=dyop
        self.dp=dp
    def display(self):
        print(self.name,self.phone_number,self.addreass,self.mail,self.dyop,self.dp,sep="\n")
    @classmethod
    def C_display(cls):
        print(cls.Iname,cls.CEO,cls.C_addr,sep='\n')
    

class Qspider(Testyanntra):
    Iname="Qspider"
    type_Q="testing"
class Pysider(Testyanntra):
    Iname = "Pyspider"
    branch_head="Pooja"
    Type='Developmenr'
class jspider(Testyanntra):
    Iname="Jspider"
    branch_head='kashi'
    Type='java development'


# chan=Qspider('chandan BV',7338042598,'Banglore','chandan@',2021,70)
# chan.C_display()
# chan.display()

def pay(n,pep,dis,sku):
    sum=[]
    for i in range(n):
        if sku[i]>0:
            sum+=[pep[i]*dis[i]]
    return sum
print(pay(6,[87,103,229,41,8,86],[3,1,9,2,1,2],[7,-21,30,0,-4,-3]))



class AB:
    __a=10
    __b=20
    __c=30
    def __init__(self,d,e):
        self.d=d
        self.e=e
    def __display(self):
        print(self.d,self.e)
# oa=AB(40,50)
# AB._AB__display()


