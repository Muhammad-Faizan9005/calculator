import math

def add(x1, x2):
    return x1 + x2  

def subtract(x1, x2):
    return x1 - x2  

def divide(x1, x2):
    if x2 == 0:
        return "Error! Division by zero."
    return x1 / x2

def multiply(x1, x2):
    return x1 * x2

def power(x1, x2):
    return x1 ** x2

def remainder(x1, x2):
    if x2 == 0:
        return "Error! Division by zero."
    return x1 % x2

def floor_division(x1, x2):
    if x2 == 0:
        return "Error! Division by zero."
    return x1 // x2

def square_root(x1):
    return x1 ** 0.5

def cube_root(x1):
    return x1 ** (1/3)

def percentage(x1, x2):
    return (x1 / x2) * 100

def factorial(x1):
    if x1 < 0:
        return "Error! Factorial of a negative number is not defined."
    elif x1 == 0:
        return 1
    else:
        return math.factorial(int(x1))

def log(x1):
    if x1 <= 0:
        return "Error! Logarithm of non-positive numbers is undefined."
    return math.log(x1)

print("\nWelcome to Faizan Calculator! 🔢")
print("\nAvailable operations:")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
print("5. power")
print("6. remainder")
print("7. floor_division")
print("8. square_root")
print("9. cube_root")
print("10. percentage")
print("11. factorial")
print("12. log\n")

# User input
function_use = input("Which function do you want to use? ").lower()

try:
    # Functions that require only one number
    if function_use in ["square_root", "cube_root", "factorial", "log"]:
        x1 = float(input("Enter a number: "))
        result = eval(f"{function_use}(x1)")
    else:
        x1 = float(input("Enter first number: "))
        x2 = float(input("Enter second number: "))
        result = eval(f"{function_use}(x1, x2)")

    print(f"\n✅ Result: {result}")

except NameError:
    print("\n❌ Invalid function name! Please check the available functions.")
except ValueError:
    print("\n❌ Invalid input! Please enter valid numbers.")
except ZeroDivisionError:
    print("\n❌ Error! Division by zero is not allowed.")
except Exception as e:
    print(f"\n❌ Unexpected error: {e}")
