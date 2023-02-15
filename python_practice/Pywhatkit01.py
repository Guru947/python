# import os
# sec = int(input('enter the time in sec to shoutdown: '))
# str1='restart /s /t '
# str2 = str(sec)
# os.system(str1+str2)


class node:
    def __init__(self,data):
        self.data=data
        self.ref = None
class LL:
    def __init__(self):
        self.head = None
    def print_ll(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,'-->',end=" ")
                n = n.ref
    def add_begin(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.ref =self.head
            self.head = new_node

    def add_end(self,data):
        new_node = node(data)
        n = self.head
        while n.ref is not None:
            n = n.ref
        n.ref = new_node

    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n=n.ref
        if self.head is None:
            print("there no node in list")
        else:
            new_node=node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def add_befor(self,data,x):
        n = self.head
        if n is None:
            print("ll is empty")
        elif self.head.data == x:
            new_node = node(data)
            new_node.ref = n
            self.head = new_node
        else:
            while n.ref is not None:
                if n.ref.data == x:
                    break

                n = n.ref
            if n.ref is None:
                print(f'{x}"node is found')
            else:
                new_node = node(data)
                new_node.ref = n.ref
                n.ref = new_node
    def insert_empty(self,data):
        if self.head is None:
            new_node= node(data)
            self.head = new_node
        else:
            print("ll is not empty")
    def dele_beg(self):
        if self.head is None:
            print("ll is empty we can't delete")
        else:
            self.head=self.head.ref
    def del_end(self):
        n = self.head
        if n is None:
            print("ll is empty")
        else:
            while n.ref is not None:
                if n.ref.ref is None:
                    n.ref = None
                    break
                n=n.ref
    def del_value(self,x):
        n = self.head
        if n is None:
            print("list is empty")
        elif n.data == x:
            self.head = n.ref
        else:
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n.ref is None:
                print(f"{x}not found node")
            else:
                n.ref = n.ref.ref




ll1=LL()
ll1.add_begin(100)
ll1.add_begin(200)
ll1.add_end(50)
ll1.add_end(25)
ll1.add_after(40,100)
ll1.add_befor(45,100)
# ll1.insert_empty(10)
# ll1.dele_beg()
# ll1.del_end()
# ll1.del_value(100)

ll1.print_ll()
