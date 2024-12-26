
# 4.14 LAB: Remove gray from RGB

# Summary: Given integer values for red, green, and blue, subtract the gray from each value.

# Computers represent color by combining the sub-colors red, green, and blue (rgb). Each sub-color's value can range from 0 to 255. Thus (255, 0, 0) is bright red, (130, 0, 130) is a medium purple, (0, 0, 0) is black, (255, 255, 255) is white, and (40, 40, 40) is a dark gray. (130, 50, 130) is a faded purple, due to the (50, 50, 50) gray part. (In other words, equal amounts of red, green, blue yield gray).

# Given values for red, green, and blue, remove the gray part.

# Ex: If the input is:

# 130
# 50
# 130

# the output is:

# 80 0 80

# Find the smallest value, and then subtract it from all three values, thus removing the gray. 
# Note: This page converts rgb values into colors. - https://www.mathsisfun.com/hexadecimal-decimal-colors.html

r = int(input())
g = int(input())
b = int(input())
smallest_num = 0

if (r < g) and (r < b):     
    smallest_num = r
elif (g < r) and (g < b):       
    smallest_num = g            
else:
    smallest_num = b

no_grey_r = r - smallest_num    
no_grey_g = g - smallest_num    
no_grey_b = b - smallest_num    

print(f'{no_grey_r} {no_grey_g} {no_grey_b}')