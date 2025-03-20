# Python – Remove Tuples of Length K 
#Given list of tuples, remove all the tuples with length K. 
 
 
#Input :test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)], 
# K = 2  
#Output : [(4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]  
#Explanation : (4, 5) of len = 2 is removed. 


test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)] 

k=2

output_list=[]
for tup in test_list:
    if len(tup)!=2:
        output_list.append(tup)
print(output_list)

test_list=[(4,5),(4,),(8,6,7),(1,),(3,4,6,7)]
i=0
l=len(test_list)
while i<l:
    if len(test_list[i])==2:
        del test_list[i]
        l=l-1
        continue
    i=i+1
print(test_list)