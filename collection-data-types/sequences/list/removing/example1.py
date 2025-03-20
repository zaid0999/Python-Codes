# Write a program to implement stack data structure using list 


stack=[]

while True:
    print("1.Push")
    print("2.Pop")
    print("3.View Stack")
    print("4.Exit")
    opt=int(input("Enter your option :"))
    if opt==1:
        value=int(input("Enter value to push "))
        stack.append(value)
        print(f'{value} pushed inside stack')
    elif opt==2:
        if len(stack)==0:
            print("Stack is empty")
        else:
            value=stack.pop()
            print(f'{value} poped from stack')
    elif opt==3:
        print(f'Stack is {stack}')
    elif opt==4:
        break
    else:
        print("invalid option")

