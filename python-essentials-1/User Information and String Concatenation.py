first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age_input = input("Enter your age: ")

if not age_input.lstrip('-').isdigit():
    print("Invalid age input")
else:
    age = int(age_input)
    
    if age < 0:
        print("Age cannot be negative")
    else:
        print("Full Name: " + first_name + " " + last_name)
        print("You will be", age + 1, "next year")
