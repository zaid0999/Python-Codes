# Python – Remove Tuples from the List having every element as None
# Input : test_list = [(None, 2), (None, None), (3, 4), (12, 3), (None, )]  
# Output : [(None, 2), (3, 4), (12, 3)]  
# Explanation : Al None tuples are removed. 



# test_list = [(None, 2), (None, None), (3, 4), (12, 3), (None, )] 
# output_list=[tup for tup in test_list if tup!=(None,)*len(tup)]
# print(test_list)
# print(output_list)

test_list = [(None, 2), (None, None), (3, 4), (12, 3), (None, )] 
i=0
l=len(test_list)
while i<l:
    if test_list[i]==(None,)*len(test_list[i]):
        del test_list[i]
        l=l-1
        continue
    i=i+1
print(test_list)