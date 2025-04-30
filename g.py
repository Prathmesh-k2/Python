mark=int(input("enter thr mark:"))
if (mark> 1):
      print()
elif(mark>=90):
      print("A")
elif(mark<=89) and(mark>=80):
      print("B")
elif(mark<=79) and(mark>=70):
      print("c")
elif(mark<=69) and(mark>=60):
      print("D")
else :
      print("fail")

for i in range(2,100):
       if(mark %i == 0):
             print("is not prime")
else:
       print(" it is prime")