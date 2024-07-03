def perform_operation(num1, num2, operation):
    if operation == "add":
        result = str(num1 + num2)
    elif operation == "subtract":
        result = str(num1 - num2)
    elif operation == "multiply":
        result = str(num1 * num2)
    elif operation == "divide":
        if result != 0:
            result = str(num1 / num2)
        else: result = "Division by zero is not allowed"
        
    return result