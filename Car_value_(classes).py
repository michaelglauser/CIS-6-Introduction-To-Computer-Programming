
# 9.13 LAB: Car value (classes)

# Complete the Car class by creating an attribute purchase_price (type int) and the method print_info() that outputs the car's information.

# Ex: If the input is:

# 2011
# 18000
# 2018

# where 2011 is the car's model year, 18000 is the purchase price, and 2018 is the current year, then print_info() outputs:

# Car's information:
#   Model year: 2011
#   Purchase price: $18000
#   Current value: $5770

# Note: print_info() should use two spaces for indentation.


class Car:
    def __init__(self):
        self.model_year = 0
        self.purchase_price = 0
        self.current_value = 0

    def calc_current_value(self, current_year):
        self.current_value = round(self.purchase_price * (1 - 0.15) ** (current_year - self.model_year))

    def print_info(self):
        print("Car's information:")
        print("  Model year:",self.model_year)

        print(f"  Purchase price: ${self.purchase_price}")
        print(f"  Current value: ${self.current_value}")

if __name__ == "__main__":
    
    car = Car()
    car.model_year = int(input())
    car.purchase_price = int(input())
    car.calc_current_value(int(input()))
    car.print_info()


