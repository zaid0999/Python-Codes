# Write a program to read 3 students 3 subject marks
# Calculate to totalmarks, avg and result

marks=[]
for i in range(3):
    stud=[]
    for j in range(3):
        s=int(input(f'Enter subject{j+1} Marks'))
        stud.append(s)
    marks.append(stud)

for stud in marks:
    total=sum(stud)
    avg=total/3
    result="PASS" if stud[0]>=40 and stud[1]>=40 and stud[2]>=40 else "FAIL"
    print(f'{stud}\t{total}\t{avg:.2f}\t{result}')