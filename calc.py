class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return float(x) + float(y)

    def multiple(self, x, y):
        return float(x) * float(y)

    def subtract(self, x, y):
        return float(x) - float(y)

    def divide(self, x, y):
        return float(x) / float(y)

# print(Calculator.divide((),2, 0))
# ZeroDivisionError: division by zero

print(Calculator.subtract((),2, 2.432782))


