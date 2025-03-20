# Write a program to accept age from the user and display the category according to the following criteria:
#    Age             Category
#  >60               Senior Citizen
#  >30 and <=60      Adult
#  >=18 and <=30     Young Adult
#  Below 18          Minor


age=int(input("Enter Age :"))
if age>60:
    print("Senior Citizen")
elif age>30 and age<=60:
    print("Adult")
elif age>=18 and age <=30:
    print("Young Adult")
else:
    print("Minor")