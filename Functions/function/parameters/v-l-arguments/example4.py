def fun1(**a):
    for k,v in a.items():
        print(f'{k}-->{v}')

d1={'x':32,'y':65,'z':55}
fun1(**d1)

d2={'1':10,'2':20,'3':30}
fun1(**d2)