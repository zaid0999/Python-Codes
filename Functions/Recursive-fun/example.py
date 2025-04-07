def fun1():
    print("inside fun1")
    fun1() # recursion
# fun1()



# inside fun1 
# inside fun1 
# inside fun1 
# inside fun1 
# inside fun1 
# inside fun1 
# inside fun1 
# inside fun1 
# inside fun1 
# … 
# 1000 times run 
# RecursionError: maximum recursion depth exceeded

import sys
print(sys.getrecursionlimit())
