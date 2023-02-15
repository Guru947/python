# abstraction
from abc import ABC, abstractmethod


class sam(ABC):
    a = 10

    @abstractmethod
    def msg(self):
        pass

    @abstractmethod
    def hey(self):
        pass


class a(sam):
    def msg():
        print("haii")

    def msg2():
        print("bye")


# ob=a
# print(ob.a,ob.msg(),ob.msg2())
# print(sam.a)


from abc import ABC, abstractmethod


class Bank(ABC):
    bname = 'sbi'
    IFSC = 'SBIN0005'
    manager = 'Mr r'

    def __init__(self, name, phno, addr, acv, bal):
        self.name = name
        self.phno = hno
        self.addr = addr
        self.acc = acv
        self.balance = bal

    @abstractmethod
    def chd_phno(self, new):
        pass

    @abstractmethod
    def chg_addr(self, new_addr):
        pass

    def odisplay(self):
        print(self.name, self.phno, self.addr, self.acc, self.balance, sep="\n")

    @classmethod
    def cdisplay(cls):
        print(cls.bname, cls.IFSC, cls.manager)

    @staticmethod
    def msg():
        print("Modification is done")

    def deposite(self, amt):
        self.balance = self.add(self.balance, amt)

    def debit(self, amt):
        self.balance = self.sub(self.balance, amt)
        print("Amount debited")

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b


class Bank2(Bank):
    def chg_phno(self, new):
        self.phno = new

    def chg_addr(self, new):
        self.addr = new


def num(a, b):
    c = str(a)
    d = str(b)
    add = sub = mul = 0
    for i in range(len(c)):
        add = add * 10 + (int(c[i]) + int(d[i]))
        sub = sub * 10 + abs(int(c[i]) - int(d[i]))
        mul = mul * 10 + (int(c[i]) * int(d[i]))
    return add, sub, mul


# print(num(234,456))

def spe(st):
    sp = 0
    for i in st:
        if not ('a' <= i <= 'z' or 'A' <= i <= 'Z' or '0' <= i <= '9' or i == ' '):
            sp += 1

    return sp


# print(spe('aa a234Bc@@# sad$%% hsgD^'))


def num(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    if sum == 26 or sum % 26 == 0:
        print(chr(64 + 26))
    else:
        print(chr(sum % 26 + 64))


# num(6442)

class student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        a1 = self.m1 + self.m2
        a2 = other.m1 + other.m2
        return a1, a2

    def __gt__(self, other):
        a1 = self.m1 + self.m2
        a2 = other.m1 + other.m2
        if a1 > a2:
            return "a1 is gt"
        else:
            return "a2 is gt"

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1 = student(10, 20)
s2 = student(30, 40)


# print(s1+s2)
# print(s1.m1,s1.m2)
# print(s2.m1,s2.m2)
# print(s1>s2)
# print(a.__str__(s1))


class Encap:
    __a = 10

    def __display(self):
        print("india")


obj = Encap()

# obj._Encap__display()
# print(obj._Encap__a)

from abc import ABC, abstractmethod


class Com(ABC):
    @abstractmethod
    def pro(self):
        pass


class Lop(Com):
    def intel(self):
        print("hey")

# lo = Lop()
