# write a function that should generate 1 to 5 numbers 
# using recursion 


def generate_number(n):
    if n>1:
        #recursion call
        generate_number(n-1)
    print(n)
generate_number(6)