# Write a program to read name, 3 subject marks of student 
# calculate total,avg and result 

name=input("Enter Name ")
marks=[]
for i in range(3):
    s=int(input(f'Enter Subject{i+1} Marks '))
    marks.append(s)
print(marks)

total=sum(marks)
avg=total/3
for s in marks:
    if s<40:
        result="Fail"
        break
    else:
        result="Pass"
print(f'Name {name}') 
print(f'Marks {marks}') 
print(f'Total {total}') 
print(f'Avg {avg:.2f}') 
print(f'Result {result}')