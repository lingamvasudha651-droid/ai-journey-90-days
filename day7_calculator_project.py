def add(a,b):
    return a+b
def sub(a,b):
    return a-b
print("1, add")
print("2, sub")
choice=input("choose 1 or 2:")
num1=int(input("first number"))
num2=int(input("second number"))

if choice=="1":
    print("Result {add(num1,num2)}")
else:
    print("Result{sub(num1,num2)}")
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

print("1. Add")
print("2. Sub")
choice = input("Choose 1 or 2: ")

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

if choice == "1":
    print(f"Result: {add(num1, num2)}")
else:
    print(f"Result: {sub(num1, num2)}")
      
