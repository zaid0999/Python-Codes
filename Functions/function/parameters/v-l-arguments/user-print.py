import sys
def display(*args,sep=' ',end='\n',file=sys.stdout):
    a=list(map(str,args))
    s=sep.join(a)
    s=s+end
    file.write(s)

display(10,20)
display(10,20,30,sep=',')
display(1,2,3,4,5,sep=':',end=';')