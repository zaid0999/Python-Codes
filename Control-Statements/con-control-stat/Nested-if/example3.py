#  Write a program to find input year is leap or not
#  Using nested if

year=int(input("Enter any Year "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f'{year} Leap Year')
        else:
            print(f'{year} Is Not Leap Year')
    else:
        print(f'{year} Leap Year')
else:
    print(f'{year} Is Not Leap Year')