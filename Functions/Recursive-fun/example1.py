import sys
sys.setrecursionlimit(20)
def fun1():
    print("inside fun1")
    fun1() #recursion
fun1()