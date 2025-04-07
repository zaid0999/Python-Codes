def power(num):
    def find_power(p):
        r=num**p
        return r
    return find_power
p1=power(5)
res1=p1(2)
res2=p1(3)
res3=p1(4)
print(res1,res2,res3)

p2=power(3)
res4=p2(3)
res5=p2(4)
res6=p2(5)
print(res4,res5,res6)

res7=p1(5)
print(res7)