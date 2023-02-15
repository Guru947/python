# stacks
s=[]
def push():

    a=int(input('enter the number:'))
    s.append(a)
    print(s)
def pop_element():
    if not s:
        print('stack is empty')
    else:

        print('removed element',s.pop())
        print(s)
# while True:
#     print('selct choice 1.push , 2.pop ,3.quite')
#     b=int(input('enter ur choice: '))
#     if b==1:
#         push()
#     elif b==2:
#         pop_element()
#     elif b==3:
#         break
#     else:
#         print('enter the correct operation')

# import collections
# stack=collections.deque()
# print(stack)
# stack.append(10)
# stack.append(20)
# print(stack)
# stack.pop()
# print(stack)
q=[]
def enqueue():
    n=int(input("enter the number: "))
    s.insert(0,n)

def dequeue():
    if not s:
        print('queue is empty')
    else:
        print('the number to be pop is: ',s.pop())
def display():
    print(s)
while True:
    print('enter ur choice 1=insert,2=delete,3=quite,4=display')
    c=int(input('enter ur choice: '))
    if c==1:
        enqueue()
    elif c==2:
        dequeue()
    elif c==3:
        break
    elif c==4:
        display()
    else:
        print("enter the currect choice")



class node:
    def __init__(self, data):
        self.data = data
        self.ref = None
class linkedList:
    def __init__(self):
        self.head=None
    def print(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:

