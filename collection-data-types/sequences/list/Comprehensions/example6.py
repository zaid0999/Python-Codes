# Generate a list of numbers with their squares if number is 
# even 

# without comprehension

A=[]
for num in range(1,11):
    if num%2==0:
        A.append(num**2)
print(A)

# with comprehension

a=[num**2 for num in range(1,11) if num%2==0]
print(a)