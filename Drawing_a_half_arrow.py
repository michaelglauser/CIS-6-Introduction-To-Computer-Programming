
# 5.25 LAB*: Program: Drawing a half arrow

# Write a program that outputs a downwards facing arrow composed of a rectangle and a right triangle. Arrow dimensions are defined by user specified arrow base height, arrow base width, and arrow head width.

# Note: this program is designed for incremental development. Complete each step and submit for grading before starting the next step. Only a portion of tests pass after each step but confirm progress.

# Step 1 (3 pts). Input the arrow base height (int) and width (int). Draw a rectangle using asterisks (height x width). Hint: use a nested loop in which the inner loop draws one row of *s, and the outer loop iterates a number of times equal to the height. Submit for grading to confirm two tests pass.

# Ex: If input is:

# 6
# 4

# Sample output is:

# ****
# ****
# ****
# ****
# ****
# ****

# Step 2 (3 pts). Input the arrow head width and draw a right triangle. Hint: use a nested loop. Submit for grading to confirm four tests pass.

# Ex: If input is:

# 4
# 3
# 4

# Sample output is:

# ***
# ***
# ***
# ***
# ****
# ***
# **
# *

# Step 3 (4 pts). Modify the program to only accept an arrow head width that is larger than the arrow base width. Use a loop to continue inputting the arrow head width until the value is larger than the arrow base width. Submit for grading to confirm all tests pass.

# Ex: If input is:

# 4
# 3
# 3
# 2
# 4

# Sample output is:

# ***
# ***
# ***
# ***
# ****
# ***
# **
# *



height = int(input())

# Read the width of the rectangle from the user
width = int(input())

# Loop to read head width which is greater than base width
while True:

    # Read the head width of the of the arrow 
    head_width = int(input())
    
    # If the head width is greater than base width 
    if head_width > width:
        
        # Exit from loop 
        break 

# Loop through each row i from 1 to height 
for i in range(1, height+1):

    # Loop through each column j from 1 to width
    for j in range(1, width+1):

        # Print an asterisk (*) for each column without moving to the next line
        print("*", end='')

    # Move to the next line after printing all columns for the current row
    print()
    
# Loop through each row i from 1 to head width 
for i in range(1, head_width+1):
    
    # Loop through each column j from head width to i-1 
    for j in range(head_width, i-1, -1):
        
        # Print an asterisk (*) for each column without moving to the next line
        print("*", end='')
        
    # Move to the next line after printing all columns for the current row
    print()