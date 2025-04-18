class Stack:
    def __init__(self):
        self.__s=[]
    def push(self,e):
        self.__s.append(e)
    def pop(self):
        return self.__s.pop()
    
stack1=Stack()
stack1.push(1)
stack1.push(3)
stack1.push(2)
x=stack1.pop()
y=stack1.pop()
print(x,y)
z=stack1.pop()
print(z)