# Variable length positional parameters 
# In variable length positional parameter store values using position. 
# Variable length positional parameter is of type tuple 
# Variable length positional parameter is prefix with * 

# Syntax: 
# def <function-name>(*param): 
#         statement-1 
#         statement-2 

def fun1(*a): # variable length positional parameter
    print(a,type(a))

fun1()
fun1(50)
fun1(1,2,3,4,5,6)
fun1(10,"naresh","python",420.32)


# In application development function with variable length arguments is used to perform aggregate operations (OR) an operation required more than one value. 