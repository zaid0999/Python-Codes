# Python – Join Tuples if similar initial element 
# Input  : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
# Output:[(5, 6, 7, 8), (6, 10), (7, 13)]


test_list = [(5,6),(5,7),(5,8),(6,10),(7,13)]
res = []
for tup in test_list:
    if res and res[-1][0]==tup[0]:
        res[-1].extend(tup[-1:]) 
    else:
        res.append([ele for ele in tup])

res=list(map(tuple,res))
print(res)
