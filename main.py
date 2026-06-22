# 1. Take numbers as input from the user (converted to float for decimals)
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# 2. Ask the user what operation they want to perform
print("\nChoose an operation:")
print("+ : Addition")
print("- : Subtraction")
print("* : Multiplication")
print("/ : Division")
operation = input("Enter the operator (+, -, *, /): ")

a="raees"
wwe="619"

# 3. Perform the calculation and show the output
print("\n--- Result ---")
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    # Handle division by zero edge case
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator selected.")
