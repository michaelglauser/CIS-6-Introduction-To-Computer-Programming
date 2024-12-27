
# 8.20 LAB: Filter and sort a list

# Write a program that gets a list of integers from input, and outputs negative integers in descending order (highest to lowest).

# Ex: If the input is:

# 10 -7 4 -39 -6 12 -2

# the output is:

# -2 -6 -7 -39 

# For coding simplicity, follow every output value by a space. Do not end with newline.

numbers = list(map(int, input().split()))
negative_numbers = sorted([x for x in numbers if x < 0], reverse=True)
for num in negative_numbers:
    print(num, end=" ")