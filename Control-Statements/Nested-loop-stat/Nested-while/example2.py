# Write a program to generate armstrong numbers 
# 100 to 999 using while loop

num=100 
while num<=999: 
    num1=num 
    s=0 
    while num1>0: 
        d=num1%10 
        s=s+(d**3) 
        num1=num1//10 
    if num==s: 
        print(num) 
    num=num+1