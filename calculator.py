def add(x1, x2):
    return x1 + x2  # No need to convert again

def subtract(x1, x2):
    return x1 - x2  # No need to convert again

print("Welcome to Faizan Calculator!")
print("Enter two numbers:")

# Convert input only once
x1 = float(input("Enter first number: "))
x2 = float(input("Enter second number: "))

function_use = input("Which function do you want to use? (addition/subtraction): ").lower()

if function_use == "addition":
    result = add(x1, x2)
    print(f"Result of addition: {result}")
elif function_use == "subtraction":
    result = subtract(x1, x2)
    print(f"Result of subtraction: {result}")
else:
    print("Invalid input!")
