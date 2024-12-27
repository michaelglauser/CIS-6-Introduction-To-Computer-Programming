
# 7.5 LAB: Checker for integer string

# Forms often allow a user to enter an integer. Write a program that takes in a string representing an integer as input, and outputs Yes if every character is a digit 0-9 or No otherwise.

# Ex: If the input is:

# 1995

# the output is:

# Yes

# Ex: If the input is:

# 42,000

# or any string with a non-integer character, the output is:

# No


user_string = input()

def is_integer_string(user_string):

    for char in user_string:
        if not char.isdigit():
            return "No"
    return "Yes"


#user_input = input("Enter a string representing an integer: ")

# Check if the input string represents an integer
#result = check_integer_string(user_string)



result = is_integer_string(user_string)
print(result)
