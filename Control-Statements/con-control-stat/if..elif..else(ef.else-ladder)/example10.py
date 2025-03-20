#A company provides an annual performance bonus to employees based on their performance rating. The bonus is calculated as a percentage of their annual salary according to the following criteria:
#  Perfomance Rating        Bonus
#  Excellent(>=9)            12%
#  Good(>=7 and <9)          8%
#  Average(>=5 and <7)       5%
#  Below Average(<5)         No Bonus


salary=int(input("Salary "))
service=int(input("Service "))
if service>=9:
    bonus=salary*(12/100)
elif service>=7 and service<9:
    bonus=salary*(8/100)
elif service>=5 and service<7:
    bonus=salary*(5/100)
else:
    service<5
    print("No Bonus")
print(f'Salary {salary}')
print(f'Bonus {bonus:.2f}')
print(f'Service {service}')