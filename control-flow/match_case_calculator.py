num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")
match operation:
    case "+":
        result = f"The result is { num1 + num2 }."
    case "*":
        result = f"The result is { num1 * num2 }."
    case "/":
        if num2 == 0:
            result = "Cannot divide by zero."
        else:
            result = f"The result is { num1 / num2 }."
        
print(result)
