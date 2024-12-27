
# 6.19 LAB: Max magnitude

# Write a function max_magnitude() with three integer parameters that returns the largest magnitude value. Use the function in the main program that takes three integer inputs and outputs the largest magnitude value.

# Ex: If the inputs are:

# 5
# 7
# 9

# function max_magnitude() returns and the main program outputs:

# 9

# Ex: If the inputs are:

# -17
# -8
# -2

# function max_magnitude() returns and the main program outputs:

# -17

# Note: The function does not just return the largest value, which for -17 -8 -2 would be -2. Though not necessary, you may use the built-in absolute value function to determine the max magnitude, but you must still output the input number (Ex: Output -17, not 17).

# Your program must define and call the following function:
# def max_magnitude(user_val1, user_val2, user_val3)

def max_magnitude(user_val1, user_val2, user_val3):

    magnitude1 = abs(user_val1)
    magnitude2 = abs(user_val2)
    magnitude3 = abs(user_val3)


    max_mag = max(magnitude1, magnitude2, magnitude3)

    if (max_mag==magnitude1):
        return user_val1
    elif (max_mag==magnitude2):
        return user_val2
    else:
        return user_val3
#main program
if __name__ == "__main__":
    #get user input for three integers
    user_val1 = int(input())
    user_val2 = int(input())
    user_val3 = int(input())

    result = max_magnitude(user_val1, user_val2, user_val3)

    print(result)