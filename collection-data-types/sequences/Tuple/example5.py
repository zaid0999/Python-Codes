# Python-Modulo of tuple elements

test_tup1=(10,4,5,6)
test_tup2=(5,6,7,5)

a=tuple([test_tup1 [i]%test_tup2[i] for i in range(4)])
print(a)