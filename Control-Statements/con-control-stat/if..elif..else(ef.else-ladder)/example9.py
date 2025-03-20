# A company decided to give bonus to employee according to following criteria:
# Time period of Service        Bonus
# More than 10 years             10%
# >=6 and <=10                   8%
# Less than 6 years              5%
#   Ask user for their salary and years of service and print net bonus amount.

salary=int(input("Salary "))
service=int(input("Service "))
if service>10:
    bonus=salary*(10/100)
elif service>=6 and service<=10:
    bonus=salary*(8/100)
else:
    bonus=salary*(5/100)
print(f'Salary {salary}')
print(f'Service {service}')
print(f'Bonus {bonus:.2f}')