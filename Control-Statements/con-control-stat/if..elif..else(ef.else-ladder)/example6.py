# Write a program to accept the cost price of a bike and display the road tax to be paid according to the followig criteria :
#  Cost price (in Rs)         Tax
#   >100000                   15%
#   >50000 and <=100000       10%
#   <=50000                   5%


bike_cost=int(input("Bike Cost "))
if bike_cost>100000:
    tax=bike_cost*(15/100)
elif bike_cost>50000 and bike_cost<=100000:
    tax=bike_cost*(10/100)
else:
    tax=bike_cost*(5/100)
print(f'Bike Cost {bike_cost}')
print(f'Road Tax{tax:.2f}')