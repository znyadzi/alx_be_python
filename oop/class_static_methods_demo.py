class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        # Returning the sum of the two numbers
        return a + b

    @classmethod
    def multiply(cls, a, b):
        # Returning the product of the two numbers
        print(f"Calculation type: {cls.calculation_type}")
        return a * b