print()

# Login Application

users={'naresh':'n123',
       'suresh':'s123',
       'ramesh':'r123'}
uname=input("UserName: ")
password=input("Password: ")
if uname in users and users[uname]==password:
    print(f'{uname} Welcome')
else:
    print("Invalid Username or Password")

print()