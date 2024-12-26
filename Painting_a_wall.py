
# 3.18 LAB*: Program: Painting a wall

# Program Specifications Write a program to calculate the cost to paint a wall. Amount of required paint is based on the wall area. Total cost includes paint and sales tax.

# Note: This program is designed for incremental development. Complete each step and submit for grading before starting the next step. Only a portion of tests pass after each step but confirm progress.

# Step 1 (2 pts). Read from input wall height, wall width, and cost of one paint can (floats). Calculate and output the wall's area to one decimal place using print(f"Wall area: {wall_area:.1f} sq ft");. Submit for grading to confirm 1 test passes.

# Ex: If the input is:

# 12.0
# 15.0
# 29.95

# the output is:

# Wall area: 180.0 sq ft

# Step 2 (2 pts). Calculate and output the amount of paint needed to three decimal places. One gallon of paint covers 350 square feet. Submit for grading to confirm 2 tests pass.

# Ex: If the input is:

# 12.0
# 15.0
# 29.95

# the output is:

# Wall area: 180.0 sq ft
# Paint needed: 0.514 gallons

# Step 3 (2 pts). Calculate and output the number of 1 gallon cans needed to paint the wall. Extra paint may be left over. Hint: Use ceil() from the math module to round up to the nearest gallon (int). Submit for grading to confirm 4 tests pass.

# Ex: If the input is:

# 12.0
# 15.0
# 29.95

# the output is:

# Wall area: 180.0 sq ft
# Paint needed: 0.514 gallons
# Cans needed: 1 can(s)

# Step 4 (4 pts). Calculate and output the paint cost, sales tax of 7%, and total cost. Dollar values are output with two decimal places. Submit for grading to confirm all tests pass.

# Ex: If the input is:

# 8.0
# 8.0
# 49.20

# the output is:

# Wall area: 64.0 sq ft
# Paint needed: 0.183 gallons
# Cans needed: 1 can(s)
# Paint cost: $49.20
# Sales tax: $3.44
# Total cost: $52.64

import math                     


wall_height = float(input())
wall_width = float(input())
wall_area = float(wall_height * wall_width)
print(f"Wall area: {wall_area:.1f} sq ft")

cost_of_one_paint_can = float(input())
paint_needed = float(wall_area/350)
cans_needed = math.ceil(paint_needed)
paint_cost = float(cans_needed * cost_of_one_paint_can)
sales_tax = float((cans_needed * cost_of_one_paint_can)*.07)
total_cost = float(paint_cost + sales_tax)


print(f"Paint needed: {paint_needed:.3f} gallons")
print(f"Cans needed: {cans_needed:} can(s)")
print(f"Paint cost: ${paint_cost:.2f}")
print(f"Sales tax: ${sales_tax:.2f}")
print(f"Total cost: ${total_cost:.2f}")

