#write a program to input name,sub1,sub2 marks
#calculate total,avg and result

name=input("Name ")
sub1=int(input("Enter Subject1 Marks "))
sub2=int(input("Enter Subject2 Markes "))
total=sub1+sub2
avg=total//2
result="PASS" if sub1>40 and sub2>40 else "FAIL"
print(f'''Name {name}
Subject1 Marks {sub1}
Subject2 Marks {sub2}
Total Marks {total}
Avg Marks {avg}
Result {result}''')