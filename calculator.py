def add(x, y):
    return x+y

def sub(x, y):
    return x-y

def mult(x, y):
    return x*y

def div(x, y):
    return x/y


print("select an operation:")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

while True:
 
 choice = input("enter your choice: ")
 print("now enter 2 numbers: ")
 num1 = float(input("enter num1: "))
 num2 = float(input("enter num2: "))
 if choice == '1':
         print(add(num1, num2))
 elif choice == '2':
         print(sub(num1, num2))
 elif choice == '3':
         print(mult(num1, num2))
 elif choice == '4':
        print(div(num1, num2))





