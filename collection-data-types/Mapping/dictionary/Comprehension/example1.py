# Power Dictionary 
# key --> number 
# value --> number power 2 

# without comprehension

d1={}
for num in range(1,11):
    d1[num]=num**2
print(d1)



# with comprehension 
d1={num:num**2 for num in range(1,11)}
print(d1)