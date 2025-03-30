# Function with required positional only arguments 

# The function with positional only arguments is defined with last parameter with / 

# Syntax: 
# def <function-name>(param1,param2,param3,/): 
#        statement-1 
#        statement-2 



def avg(a,b,/): # Positional only
    c=(a+b)/2
    print(f'avg of {a} and {b} is {c:.2f}')

avg(10,50) # Positional only
# avg(a=11,b=55)  Error