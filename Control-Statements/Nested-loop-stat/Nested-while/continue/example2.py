# Password validation for 5 attempts 

epassword="nit123" 
 
for i in range(5): 
    password=input("Password :") 
    if password!=epassword: 
        print("Invalid password") 
        continue 
    print("Welcome") 
    break