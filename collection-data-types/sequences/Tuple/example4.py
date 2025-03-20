# Python-Sum of tuple elements


test_tup=([7,8],[9,1],[10,7])
s=0
for a in test_tup:
    s=s+sum(a)
print(f'The Summation of tuple elements are {s}')


s=0
for a in test_tup:
    for b in a:
        s=s+b
print(f'The summation of tuple elements are {s}')