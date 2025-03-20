# Python-Maximum and Minimum K elements in Tuple

test_tup=(3,7,1,18,9)
k=2
t2=tuple(sorted(test_tup))
print(t2)
t3=t2[:k]+t2[-k:]
print(t3)