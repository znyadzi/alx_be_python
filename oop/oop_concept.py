# 1 Declaring a class
"""
class Sport:
    type = "Golf"
"""

# 2 Calling variables of a class

"""
class Person:
    name = "Lord"

lord = Person()
print(lord.name)
"""

# 3 Methods in classes
"""
class Car:
    manufacturer = "Mercedes"
    build_date = 2022

    #This function prints the manufacturer and the build year.
    def print_info(self):
        print("Car Manufacturer is ", self.manufacturer)
        print("The build date is ", build_date)
    
    #Another example
    class Dog:
    voice = "Woof"

    def bark(self):
        print(self.voice)
"""

# 4 Updating variable values withn a class
"""
class Point:
    x = 0
    y = 0
    
    def update_x(self, new_x):
        self.x = new_x
    def update_y(self, new_y):
        self.y = new_y
"""

# 5 Class Contructors
"""
class Sports:
    def __init__(self, sports_name, sports_type):
        self.name = sports_name
        self.type = sports_type
golf = Sports("Football", "Outdoor Sports")
print(golf.name)
print(golf.type)
"""

# 6 Inheritance
"""
# Parent class
class Sports:
    type = "Outdoor"
    distance = "short"
    use_hands = False

# Child Class
class Football(Sports):
    name = "Football"
"""
# 