# Python-Row-wise element Addition in Tuple Matrix

test_list = [[('Gfg', 3)], [('best', 1)]] 
output_list=[]
cus_eles=[1,2]
i=0
for row in test_list:
    for col in row:
        a=list(col)
        a.append(cus_eles[i])
    output_list.append([tuple(a)])
    i=i+1
print(test_list)
print(output_list)