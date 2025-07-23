# defining a variable
def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return float('inf')  # Division by zero
    else:
        return None  # Invalid operation


# Ask user for input
print("Enter the first number:")
num1 = float(input())

print("Enter the second number:")
num2 = float(input())

print("Choose the operation: add, subtract, multiply, divide")
operation = input().strip().lower()  # remove spaces and lowercase

# Perform the operation
result = perform_operation(num1, num2, operation)

# Display result
if result is None:
    print("Invalid operation selected.")
elif result == float('inf'):
    print("Error: Cannot divide by zero.")
else:
    print("The result is:", result)
