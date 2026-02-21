num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

if not (num1.lstrip('-').isdigit() and num2.lstrip('-').isdigit()):
    print("Invalid input")
else:
    a = int(num1)
    b = int(num2)

    if b == 0:
        print("Cannot divide by zero")
    else:
        print("Sum:", a + b)
        print("Division:", a / b)
