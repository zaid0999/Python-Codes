# Banking Application (Withdraw/Deposit)

accno=int(input("Enter Your Account No. "))
balance=int(input("Your Balance "))
ttype=input("Transaction Type (D)Deposit or (W)Withdraw ")
tamt=int(input("Amount to Deposit/withdraw "))
if ttype=="D":
    balance+=tamt
elif ttype=="W":
    if tamt<balance:
        balance-=tamt
    else:
        print(f'Insuff Balance')
else:
    print("Invalid Transaction Type")
print(f'''Account :{accno}
Balance: {balance}
Transaction Type: {ttype}
Transaction Amount: {tamt}''')