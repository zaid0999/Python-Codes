# Write code for allow password 5 attempts
# Use while..else and break


epassword="nit123"
i=1
while i<=5:
    password=input("Password :")
    if password==epassword:
        print("Welcome")
        break
    i=i+1
    print("Wrong Password")
else:
    print("Wrong Password 5 attempts are completed your account is blocked")