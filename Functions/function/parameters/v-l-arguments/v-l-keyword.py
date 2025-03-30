# Variable length keyword arguments 
 
# A function with variable length keyword argument receives 0 more values but each value is identity with key. 
# A function with variable length keyword arguments receives key and value. 
# Variable length keyword argument is of type dictionary. 
# This parameter is prefix with ** 

# Syntax 
# def <function-name>(**kwargs): 
#     statement-1 
#     statement-2 


def fun1(**a): # a is variable length keyword only arguments
    print(a,type(a))

fun1()
fun1(x=19)
fun1(z1=10,z2=20,z3=30)
fun1(x=54,y=1.3,z="zaid")