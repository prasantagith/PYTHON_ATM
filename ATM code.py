
pin=int(input('create a pin:'))
balance=3000

print("Welcome to HDFC")
for i in range(3):
    pinno=int(input("enter your pin number:"))
    if pinno==pin:
        print("Deposit : d  Withdrawl : w ")
        option=input("choose the option")
        if option=="d":
            depositamount=int(input("Enter the amount you want to deposit:"))
            print("open the box and it will collect your amount")
            print("Amount deposited successfully")
            break
        else:
            withdrawlamount=int(input("enter the amount you want to withdraw:"))
            if withdrawlamount<=balance:
                
                print("Amount withdrawn successfully")
                break
            else:
                print("insufficient funds")
    
    
        
    
    else:
        print("your pin is incorrect")
else:
    print("card blcoked.")
