class pyspider:
    branch = 'Basavangudi'
    b_code='qpm21'
    trainer='pooja'
    subject ='python'
    @classmethod
    def change_branch(cls,new_branch):
        cls.branch=new_branch
    @classmethod
    def change_batch_code(cls,new_b_code):
        cls.b_code=new_b_code
    @classmethod
    def change_trainer(cls,new_trainer):
        cls.trainer =new_trainer
    @classmethod
    def change_subject(cls,new_subject):
        cls.subject = new_subject
    @classmethod
    def change_everything(cls,branch,b_code,trainer,subject):
        cls.branch=branch
        cls.b_code=b_code
        cls.trainer=trainer
        cls.subject=subject

    def __init__(self):
        self.name=self.name()
        self.age=self.age()
        self.phno=self.phone_nu()
        self.email=self.email()
        self.target_fee=self.target_fee()
    @staticmethod
    def name():
        return input("enter the fullname:")
    @staticmethod
    def age():
        return input("enter the your age:")
    @staticmethod
    def phone_nu():
        return input("enter the ur phone:")
    @staticmethod
    def email():
        return input("enter the email:")
    @staticmethod
    def target_fee():
        return int(input("enter target_fee:"))
    print(chr(563)*24)
    def display(self):
        print("name of student:",self.name)
        print("branch of students:", self.branch)
        print("branch code:", self.b_code)
        print("age of student:" ,self.age)
        print("phone number of student:",self.phno)
    def change_name(self,new_name):
        self.name=new_name
    def change_age(self,newage):
        self.age = newage
    def change_phone(self,new_phone):
        self.phno=new_phone
    def change_email(self,new_email):
        self.email=new_email
    def change_target_fee(self,new_target_fee):
        self.target_fee = new_target_fee
    def paid_fee(self,amount):
        self.paid_fees =amount
    def bal_fee(self):
        self.bals_fee= self.target_fee-self.paid_fees
        print("amount to be paid:",self.bals_fee)

student1=pyspider()
student1.display()
student1.paid_fee(41000)
student1.bal_fee()
student1.change_name('Chandanbv')
print(chr(2593))
student1.display()