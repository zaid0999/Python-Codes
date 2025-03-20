# Generate a list of common multiples of 3 and 5 upto 100 
 
# without comprehension 


A=[]
for num in range(1,101):
    if num%3==0 and num%5==0:
        A.append(num)
print(A)

# With Comprehension

A=[num for num in range(1,101) if num%3==0 and num%5==0]
print(A)