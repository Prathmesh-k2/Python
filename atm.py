balance=1000
print("welcome to atm")
print("your balance is",balance)
amount=int(input("enter the amount"))
if(amount<=0):
      print("amount is less than zero")
elif(amount>balance):
       print("anount is greter tham balence")
elif(amount%10!=0):
       print("enter the amount in 10  multiply")
else:
       amount-=balance
       print("withdrawl the cash")
       print("your balance is:",amount)
  