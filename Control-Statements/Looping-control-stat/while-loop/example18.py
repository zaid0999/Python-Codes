# Write a program to conver decimal to hexadecimal

num=int(input("Enter any Number "))
hexa=""

while num>15:
    d=num%16
    match(d):
        case 10:
            hexa+="A"
        case 11:
            hexa+="B"
        case 12:
            hexa+="C"
        case 13:
            hexa+="D"
        case 14:
            hexa+="E"
        case 15:
            hexa+="F"
        case _:
            hexa+=str(d)
    num=num//16

match(num):
    case 10:
        hexa+="A"
    case 11:
        hexa+="B"
    case 12:
        hexa+="C"
    case 13:
        hexa+="D"
    case 14:
        hexa+="E"
    case 15:
        hexa+="F"
    case _:
        hexa+=str(num)

print("0x"+hexa[::-1])