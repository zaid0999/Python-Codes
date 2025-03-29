# Function with required parameters or arguments 

# Function with required parameters required values at the time of invoking or caling the function. 

# Syntax: 
# def <function-name>(param1,param2,param3,…): 
#        statement-1 
#        statement-2 


def fun1(a,b):
    print(a,b)

fun1(100,200)
fun1(10,20) # Posional argument
fun1(a=90,b=190) # Keyword argument
fun1(b=500,a=600) # Keyword argument


# Giving values to parameters using their position is called positional arguments 

# Giving values to parameters using parameter names is called keyword arguments 

# If function is defined with required arguments it allows receiving values with position and keyword.