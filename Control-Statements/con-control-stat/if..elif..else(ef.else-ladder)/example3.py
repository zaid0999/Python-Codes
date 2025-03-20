#1. Water Bill Calculation
#Write a program to calculate the water bill based on the following criteria:
#First 50 liters: No charge
#Next 100 liters: Rs 2 per liter
#After 150 liters: Rs 5 per liter
#(Example: If input is 200 liters, the total bill is Rs 450.)



water=int(input("How Much Water "))
if water<=50:
    bill=0
elif water>50 and water<=150:
    bill=2*(water-50)
else:
    bill=0+200+(water-150)*5
print(f'Total bill {bill}')