
# 8.21 LAB: Middle item

# Given a sorted list of integers, output "Middle item: " followed by the middle integer. Assume the number of integers is always odd.

# Ex: If the input is:

# 2 3 4 8 11

# the output is:

# Middle item: 4

# The maximum number of inputs for any test case should not exceed 9. If exceeded, output "Too many inputs".

# Hint: First read the data into a list. Then, based on the list's size, find the middle item.

numbers_string = input()

numbers_list_strings = numbers_string.split()

numbers_list = [int(num) for num in numbers_list_strings]

if len(numbers_list) > 9:
    
    # Then, display an error message
    print("Too many inputs")
else:
    # Else, dividing the length of the list by 2 and ignoring the post decimal value
    middle_num_index = len(numbers_list) // 2
    
    # Displaying the element at the middle index in the list
    print("Middle item:", numbers_list[middle_num_index])
