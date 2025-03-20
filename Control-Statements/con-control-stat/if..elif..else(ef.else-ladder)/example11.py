#  Accept the kilometers coverd and calculate the bill according to the following criteria:
#  First 10Km       Rs11/km
#  Next 90Km        Rs10/km
#  After that       Rs9/km


kilometer=int(input("Kilometers "))
if kilometer<=10:
    bill=kilometer*11
elif kilometer>10 and kilometer<=100:
    bill=(10*11)+(kilometer-10)*10
else:
    bill=(10*11)+(90*10)+(kilometer-100)*9
print(f'Kilometer {kilometer}')
print(f'Bill {bill}')