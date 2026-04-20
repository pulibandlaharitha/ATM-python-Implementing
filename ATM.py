import time
password=1919
balance=10000
print("welcome to ATM")
print("insert your card")
print("press1.yes2.no")
choice=int(input())
if choice==1:
    print("enter the pin")
    pin=int(input())
    if pin==password:
        print("select the language")
        print("1.english2.kannada3.tamil")
        lang=int(input())
        if lang==1:
            print("enter the option")
            print("1.balance enquiry 2.withdraw")
            choice=int(input())
            if choice==1:
                print("your current balance is",balance)
            elif choice==2:
                print("enter the amount to be withdrawed")
                amt=int(input())
                if amt % 100 != 0:
                    print("enter the valid number")
                    if amt>balance:
                        print("your balance is below the number that you entered")
                    elif amt==balance and amt<balance:
                        print("your transaction is in process")
                        time.sleep(5)
                        print("collect your cash")
                        time.sleep(5)
                        print("would u like to check your balance")
                        print("1.yes2.no")
                        choice=int(input())
                        if balance<0:
                            if choice==1:
                                print("your balance is",balance)
                            elif choice==2:
                                print("thank you visit again")
                            else:
                                print("something went wrong.please try again")