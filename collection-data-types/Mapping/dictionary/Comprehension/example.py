# Dictionary Comprehension 
# Creating dictionary using dictionary comprehension 

# Syntax1: {key:value for variable in iterable} 
# Syntax2: {key:value for variable in iterable if test} 


# Example:

# ASCII Dictionary of uppercase

# with comprehension 
ascii_upper={n:chr(n) for n in range(65,91)}
print(ascii_upper)


print("===============================================================")


# without comprehension 
d1={}
for n in range(65,91):
    d1[n]=chr(n)
print(d1)