def perform_operation(num1, num2, operation):
    if operation == "add":
        result = str(num1 + num2)
    elif operation == "subtract":
        result = str(num1 - num2)
    elif operation == "multiply":
        result = str(num1 * num2)
    elif operation == "divide":
        if num2 == 0:
            result = "Division by zero is not allowed"
        else:
            result = str(num1 / num2)
    return result