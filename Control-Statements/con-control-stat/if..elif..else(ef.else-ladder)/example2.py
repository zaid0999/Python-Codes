# Write a program to calculate the electricity bill (accept number of unit from user) according to the followint criteria :
#      Unit                  Price
#  First 100 units        no charge
#  Next 100 units         Rs 5 per unit
#  After 200 units         Rs 10 per unit


units=int(input("Enter Units :"))
if units<=100:
    amt=0
elif units>100 and units<=200:
    amt=5*(units-100)
else:
    amt=0+500+(units-200)*10
print(f'Total Bill {amt}')