FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32) 

def convert_to_fahrenheit(celsius):
    return (celsius + 32) * CELSIUS_TO_FAHRENHEIT_FACTOR

temperature = int(input("Enter the temperature to convert: "))
response = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if response == "C":
    print(temperature, " is ", convert_to_fahrenheit(temperature), "°F")
elif response == "F":
    print(temperature, " is ", convert_to_celsius(temperature), "°F")