# Write a program to count +ve, -ve, zero values

A=[1,2,3,4,-1,-2,-3,-4,7,8,9,-7,-8,0,0,1,2,3]
pc,nc,zc=0,0,0

for value in A:
    if value>0:
        pc=pc+1
    elif value<0:
        nc=nc+1
    else:
        zc=zc+1
print(A)
print(f'Positive Values are {pc}')
print(f'Negative Values are {nc}')
print(f'Zeros are {zc}')