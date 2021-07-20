import time

print("Enter your card")

time.sleep(3)

password=1235

pin=int(input("Enter your password"))

balance=5555

if pin==password:
    while True:
        print("""
          1==balance
          2==withdraw balance
          3==deposit balance
          4==exit
          """
          )
        try:
          option=int(input("Please enter your choice  :"))
        finally:
          print("Enter a valid choice  :")

        if option==1:
          print(f"Your current balance is  {balance}")

        if option==2:
          withdraw_amount=int(input("Enter the amount you want to withdrawn from your account  :"))
          balance=balance-withdraw_amount

        print(f"Your current balance is  {balance}")

        if option==3:
          deposit_amount=int(input("Enter the amount you want to deposit  :"))

          balance=balance+deposit_amount
          print(f"{deposit_amount} is created to your account")
          print(f"Your updated balance is   {balance}")

        if option==4 :
          print("Exit from the loop")
          break

else: 
        print("Wrong pin please try again!!")




