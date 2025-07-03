class Stack:
    def __init__(self):
        self.__s=[]
    def push(self,e):
        self.__s.append(e)
    def pop(self):
        return self.__s.pop()
    def print_s(self):
        print(self.__s)

stack1=Stack()
stack1.push(10)
stack1.push(20)
stack1.push(30)
stack1.print_s()
x=stack1.pop()
y=stack1.pop()
print(x,y)