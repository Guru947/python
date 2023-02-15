class student:
    def __init__(self):
        self.name=self.input_name()
        self.surname=self.input_surname()
        self.age=self.input_age()
        self.fullname=self.name+" "+self.surname

    @staticmethod
    def input_name():
        return input("enter th first name:")
    @staticmethod
    def input_surname():
        return  input("enter the surname:")
    @staticmethod
    def input_age():
        return input("enter the age:")
    def display(self):
        # print(self.name)
        # print(self.surname)
        print(self.fullname)
        print(self.age)
obl = student()
obl.display()
