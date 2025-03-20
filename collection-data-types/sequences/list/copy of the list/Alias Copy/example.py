# Write a program to search given element/value within list 
# without using "in" operator 
# Linear Search 




A=[10,20,30,40,50,60,70,80,90,100] 
s=50
for i in range(len(A)):
    if s==A[i]:
        print(True)
        break
else:
 print(False)