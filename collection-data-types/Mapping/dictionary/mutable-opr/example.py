# Create Contact List where perform operations like 
# adding contact and update contact 

contacts={}
while True:
    print("1.Add Contact")
    print("2.Update Contact")
    print("3.Show Contact")
    print("4.Exit")
    opt=int(input("Enter Your Option "))
    match(opt):
        case 1:
            name=input("Name: ")
            if name not in contacts:
                phoneno=int(input("PhoneNo: "))
                contacts[name]=phoneno
                print("Contact Added")
            else:
                print(f'{name} exists within contact')
        case 2:
            name=input("Name: ")
            if name in contacts:
                phoneno=int(input("New PhoneNo: "))
                print(f'Contact Updated')
            else:
                print(f'Contact Not Found')
        case 3:
            for name,phoneno in contacts.items():
                print(f'{name}===>{phoneno}')
        case 4:
            break
        case _:
            print("Invalid Option")