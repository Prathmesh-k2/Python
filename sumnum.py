num=int(input("enter the num "))
t=0
while(num>0):
   dig=num%10
   t=t+dig
   num=num//10 
print("sum",t)
r=int(input("enter thr row"))
for i in range(1,r+1):
    for j in range(0,r-i+1):
        print(''c,sep=",end=",)
       c=c*(i-j)//10
   
        
