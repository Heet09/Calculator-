def add(x, y):
   return x + y
print("1")

def subtract(x, y):
   return x - y
print("2")

def multiply(x, y):
   return x * y
print("3")

def divide(x, y):
   return x / y
print("4")

select = input("select1/2/3/4")

n1=int(input("enter n1"))
n2=int(input("enter n2"))

if select== "1":
    print(add(n1,n2))
elif select== "2":
    print(subtract(n1-n2))
elif select== "3":
    print(multiply(n1,n2))
else:
    print(divide(n1,n2))