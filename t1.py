a= int(input("enter a"))
b= int(input("enter b"))

def add(a, b):
 return a+b
 print("1")

def substract(a,b):
 return a-b
 print("2")

def multiply(a,b):
 return a*b
 print("3")

def divide(a,b):
 return a/b
 print("4")

select = input("select 1/2/3/4")

if select== "1":
    print(a+b)
elif select== "2":
    print(a-b)
elif select == "3":
    print(a*b)
else:
    print(a/b)
    
