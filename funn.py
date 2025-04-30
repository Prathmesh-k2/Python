def message():
    print("hiii")
message()

def a(age,name):
    print( f"hello {name} age is {age}")
a(15,"abc")

def asum(*args):
    total= sum(args)
    print(f"the sum is the {total}")

asum(1,2,3,4,5,6)

def fin(name,cn="usa"):
   print(f"the name is {name} and {cn}")

fin("aj")
fin("ab","bc")
fin("aj")