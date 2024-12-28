
# 10.10 LAB: Quadratic formula

# Implement the quadratic_formula() function. The function takes 3 arguments, a, b, and c, and computes the two results of the quadratic formula:

# The quadratic_formula() function returns the tuple (x1, x2). Ex: When a = 1, b = -5, and c = 6, quadratic_formula() returns (3, 2).

# Code provided in main.py reads a single input line containing values for a, b, and c, separated by spaces. Each input is converted to a float and passed to the quadratic_formula() function.

# Ex: If the input is:

# 2 -3 -77

# the output is:

# Solutions to 2x^2 + -3x + -77 = 0
# x1 = 7
# x2 = -5.50

import math  

def quadratic_formula(a, b, c):
    discriminant = (b ** 2) - 4 * a * c
    x1 = (-b + (discriminant ** 0.5)) / (2 * a)
    x2 = (-b - (discriminant ** 0.5)) / (2 * a)
    return (x1, x2)

def print_number(number, prefix_str):
    if float(int(number)) == number:
        print("{}{:.0f}".format(prefix_str, number))
    else:
        print("{}{:.2f}".format(prefix_str, number))

if __name__ == "__main__":
    input_line = input()
    split_line = input_line.split(" ")
    a = float(split_line[0])  
    b = float(split_line[1])  
    c = float(split_line[2])  

    solutions = quadratic_formula(a, b, c)

    print("Solutions to {}x^2 + {:.0f}x + {:.0f} = 0".format(int(a) if a.is_integer() else a, b, c))
    print_number(solutions[0], "x1 = ")
    print_number(solutions[1], "x2 = ")


