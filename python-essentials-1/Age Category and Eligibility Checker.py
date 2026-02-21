name = input("Enter your name: ")
age_input = input("Enter your age: ")

if not age_input.lstrip('-').isdigit():
    print("Invalid age input")
else:
    age = int(age_input)
    
    if age < 0:
        print("Age cannot be negative")
    else:
        print("Hello " + name)
        
        if age < 13:
            print("You are a Child")
        elif 13 <= age <= 17:
            print("You are a Teenager")
        elif 18 <= age <= 59:
            print("You are an Adult")
        else:
            print("You are a Senior Citizen")
        
        if age >= 18:
            print("You are eligible to vote")
        else:
            print("You are not eligible to vote")
