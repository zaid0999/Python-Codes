# Python – All pair combinations of 2 tuples 
# Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)  
# Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)] 


test_tuple1=(7,2)
test_tuple2=(7,8)
a=[]
for i in range(2):
    for j in range(2):
        a.append([test_tuple1[i],test_tuple2[j]])
for i in range(2):
    for j in range(2):
        a.append([test_tuple2[i],test_tuple1[j]])

a=list(map(tuple,a))
print(a)