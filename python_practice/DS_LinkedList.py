# # singly linked list
# class node:
#     def __init__(self,data):
#         self.data=data
#         self.ref = None
# class LL:
#     def __init__(self):
#         self.head = None
#     def print_ll(self):
#         if self.head is None:
#             print("linked list is empty")
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data,'-->',end=" ")
#                 n = n.ref
#     def add_begin(self,data):
#         new_node = node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             new_node.ref =self.head
#             self.head = new_node
#
#     def add_end(self,data):
#         new_node = node(data)
#         n = self.head
#         while n.ref is not None:
#             n = n.ref
#         n.ref = new_node
#
#     def add_after(self,data,x):
#         n = self.head
#         while n is not None:
#             if n.data == x:
#                 break
#             n=n.ref
#         if self.head is None:
#             print("there no node in list")
#         else:
#             new_node=node(data)
#             new_node.ref = n.ref
#             n.ref = new_node
#     def add_befor(self,data,x):
#         n = self.head
#         if n is None:
#             print("ll is empty")
#         elif self.head.data == x:
#             new_node = node(data)
#             new_node.ref = n
#             self.head = new_node
#         else:
#             while n.ref is not None:
#                 if n.ref.data == x:
#                     break
#
#                 n = n.ref
#             if n.ref is None:
#                 print(f'{x}"node is found')
#             else:
#                 new_node = node(data)
#                 new_node.ref = n.ref
#                 n.ref = new_node
#     def insert_empty(self,data):
#         if self.head is None:
#             new_node= node(data)
#             self.head = new_node
#         else:
#             print("ll is not empty")
#     def dele_beg(self):
#         if self.head is None:
#             print("ll is empty we can't delete")
#         else:
#             self.head=self.head.ref
#     def del_end(self):
#         n = self.head
#         if n is None:
#             print("ll is empty")
#         else:
#             while n.ref is not None:
#                 if n.ref.ref is None:
#                     n.ref = None
#                     break
#                 n=n.ref
#     def del_value(self,x):
#         n = self.head
#         if n is None:
#             print("list is empty")
#         elif n.data == x:
#             self.head = n.ref
#         else:
#             while n.ref is not None:
#                 if n.ref.data == x:
#                     break
#                 n = n.ref
#             if n.ref is None:
#                 print(f"{x}not found node")
#             else:
#                 n.ref = n.ref.ref
#
# ll1=LL()
# ll1.add_begin(100)
# ll1.add_begin(200)
# ll1.add_end(50)
# ll1.add_end(25)
# ll1.add_after(40,100)
# ll1.add_befor(45,100)
# ll1.insert_empty(10)
# ll1.dele_beg()
# ll1.del_end()
# ll1.del_value(100)
#
# ll1.print_ll()

# doubly linked list
import numpy


class node:
    def __init__(self, data):
        self.pref = None
        self.data = data
        self.nref = None


class ll:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("dl is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, '-->', end=' ')
                n = n.nref

    def print_ll_rev(self):
        if self.head is None:
            print("ll is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, '<--', end='  ')
                n = n.pref

    def add_beging(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            new_node.nref = n
            n.pref = new_node
            self.head = new_node

    def add_end(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                # while n is not None:
                # if n.nref is None:
                #     break
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def add_after(self, data, x):
        n = self.head
        new_node = node(data)
        while n is not None:
            if n.data == x:
                break
            n = n.nref
        if n is None:
            print("given node is note found")
        # elif n.nref is None:
        #     n.nref = new_node
        #     new_node.pref = n
        # else:
        #     new_node.nref = n.nref
        #     n.nref.pref=new_node
        #     n.nref=new_node
        #     new_node.pref=n
        else:
            new_node.nref = n.nref
            new_node.pref = n
            if n.nref is not None:
                n.nref.pref = new_node
            n.nref = new_node

    def add_before(self, data, x):
        n = self.head
        new_node = node(data)
        if n is None:
            print("empty ll")
        else:
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print("given not found")
            else:
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node
    def del_beg(self):
        n = self.head
        if n is None:
            print("DLL is empty")
        elif n.nref is None:
            self.head = None
            print("one node is del")

        else:
            self.head= self.head.nref
            self.head.pref = None

    def del_end(self):
        if self.head is None:
            print("dll is empty")
        elif self.head.nref is  None:
            self.head = None
        else:
            n = self.head
            while n.nref is not  None:
                n = n.nref
            n.pref.nref = None

    def del_by_val(self,x):
        n = self.head
        if self.head is None:
            print("dll is empty")

        elif n.data == x and n.nref is None :
            self.head = None
            print("one node is del")
        else:
            n = self.head
            if n.data == x:
                n=n.nref
                n.pref = None
            else:
                while n.nref is not None:
                    if n.pref is None and n.data == x:
                        n=n.nref
                        n.pref=None
                    else:
                        if n.data == x:
                            n.nref.pref=n.pref
                            n.pref.nref = n.nref
                        else











dd1 = ll()
dd1.add_beging(10)
# dd1.add_beging(20)
dd1.add_end(30)
# dd1.add_before(100,20)
# dd1.add_before(80,20)
# dd1.add_after(40, 30)
# dd1.add_after(35, 30)
# dd1.del_beg()
dd1.del_end()
dd1.print_ll()
# dd1.print_ll_rev()



