
# 4.15 LAB: Smallest number

# Write a program whose inputs are three integers, and whose output is the smallest of the three values.

# Ex: If the input is:

# 7
# 15
# 3

# the output is:

# 3

num1 = int(input())
num2 = int(input())
num3 = int(input())

smallest_num = min(num1, num2, num3)
if (num1 < num2):
    if (num1 < num3):
        smallest_num = num1
elif (num2 < num1):
    if (num2 < num3):
        smallest_num = num2
elif (num3 < num2):
    if (num3 < num1):
        smallest_num = num3

print(smallest_num)