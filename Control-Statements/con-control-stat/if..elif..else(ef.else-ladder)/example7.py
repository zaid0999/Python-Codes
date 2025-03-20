# Write a program to accept the cost price of a car and display the road tax to be paid according to the following criteria:
# Cost Price (in Rs)           Tax
# >1500000                     20%
# >1000000 and <=1500000       15%
# >500000 and <=1000000        10%
# <=500000                     5%


car_cost=int(input("Enter Car Cost "))
if car_cost>1500000:
    tax=car_cost*(20/100)
elif car_cost>1000000 and car_cost<=1500000:
    tax=car_cost*(15/100)
elif car_cost>500000 and car_cost<=1000000:
    tax=car_cost*(10/100)
else:
    tax=car_cost*(5/100)
print(f'Car Cost{car_cost}')
print(f'Road Tax {tax:.2f}')