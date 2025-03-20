# Write a Python program that takes a temperature as input and prints:

# "Cold" if the temperature is below 15°C
# "Warm" if it is between 15°C and 30°C
# "Hot" if it is above 30°C

tem=int(input("Enter temperature "))
if tem<15:
    print("Cold")
elif tem>=15 and tem<30:
    print("Warm")
else:
    print("Hot")