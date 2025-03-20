# Write a program to count of even digits and odd digits of input number

num=int(input("Enter any number"))
ec=0
oc=0

while num>0:
    d=num%10
    if d%2==0:
        ec+=1
    else:
        oc+=1
    num=num//10
print(f'Count of Even Digits {ec}')
print(f'Count of Odd Digits {oc}')