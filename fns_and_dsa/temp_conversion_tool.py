FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
temp_val_check = True
while temp_val_check:
    try :
        temperature = int(input("Enter the temperature to convert: "))
        temp_val_check = False
    except:
        print("Invalid temperature. Please enter a numeric value.")

response = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if response == "C":
    print(temperature, " is ", convert_to_fahrenheit(temperature), "°F")
elif response == "F":
    print(temperature, " is ", convert_to_celsius(temperature), "°F")