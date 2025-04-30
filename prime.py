num=int(input("enter the num"))
for i in range(2,num):
  if num % i==0:
    print("not primr")
    break
  else:
    print("prime")
    break