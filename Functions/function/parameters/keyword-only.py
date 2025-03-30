# Function with required keyword only arguments 

# In function with required keyword only arguments first parameters must be * folowed by user defined parameters 

# Syntax: 
# def <function-name>(*,param1,param2,param3): 
#      statement-1 
#      statement-2



def sub(*,a,b): # Keyword Only
    c=a-b
    print(f'difference of {a} and {b} is {c}')

sub(a=50,b=45)


# function positional only and keyword only 

def simple_interest(amt,t,/,*,rate):
    si=(amt*t*rate)/100
    print(si)


simple_interest(2000,12,rate=2)