# Pass by Reference 
 
# Python does not support pass by value. In python variable does not hold value, it hold reference or address of object or value. 


# Example:


def fun1(a):
    print(a,id(a))

L1=[10,20,30]
print(L1,id(L1))
fun1(L1)
T1=(10,20,30)
print(T1,id(T1))
fun1(T1)
s1="ABC"
print(s1,id(s1))
fun1(s1)






# In pass by reference the object passed to function is mutable; the changes done within function are applicable to actual object.

# In pass by reference changes done using formal arguments those changes reflect to actual arguments 


# Example

def swapfirstlast(a:list):
    a[0],a[-1]=a[-1],a[0]

n1=[10,20,30,40,50,60]
print(f'Before Swapping {n1}')
swapfirstlast(n1)
print(f'After Swapping {n1}')       