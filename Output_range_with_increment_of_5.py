
# 5.17 LAB: Output range with increment of 5

# Write a program whose input is two integers. Output the first integer and subsequent increments of 5 as long as the value is less than or equal to the second integer.

# Ex: If the input is:

# -15
# 10

# the output is:

# -15 -10 -5 0 5 10 

# Ex: If the second integer is less than the first as in:

# 20
# 5

# the output is:

# Second integer can't be less than the first.

# For coding simplicity, output a space after every integer, including the last. End the output with a newline.


first_integer, second_integer = int(input()),  int(input())  #map(int, input().split())

#x, y = int(input()),  int(input())

if second_integer < first_integer:
    print("Second integer can't be less than the first.")
else:
    current_value = first_integer
    
    while current_value <= second_integer:
        print(current_value, end=' ')  
        current_value += 5  
    
    print()  


