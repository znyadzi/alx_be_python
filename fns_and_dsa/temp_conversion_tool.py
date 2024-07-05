# Constants for conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    # Conversion formula: C = (F - 32) * (5/9)
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    # Conversion formula: F = (C * (9/5)) + 32
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Example usage
fahrenheit_temp = 100
celsius_temp = convert_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp} Fahrenheit is {celsius_temp:.2f} Celsius")

celsius_temp = 37.78
fahrenheit_temp = convert_to_fahrenheit(celsius_temp)
print(f"{celsius_temp:.2f} Celsius is {fahrenheit_temp} Fahrenheit")
