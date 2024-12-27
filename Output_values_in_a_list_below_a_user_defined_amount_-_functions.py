
# 6.28 LAB: Output values in a list below a user defined amount - functions

# Write a program that first gets a list of integers from input. The input begins with an integer indicating the number of integers that follows. Then, get the last value from the input, and output all integers less than or equal to that value.

# Ex: If the input is:

# 5
# 50
# 60
# 140
# 200
# 75
# 100

# the output is:

# 50
# 60
# 75

# The 5 indicates that five integers are in the list, namely 50, 60, 140, 200, and 75. The 100 indicates that the program should output all integers less than or equal to 100, so the program outputs 50, 60, and 75.

# Such functionality is common on sites like Amazon, where a user can filter results. Utilizing functions will help to make your main very clean and intuitive.

# The program must define the following two functions:
# def get_user_values() - read from input the size of the list, the integers in the list, and the threshold value. Return the list of integers and the threshold value.

# def ints_less_than_or_equal_to_threshold(user_values, upper_threshold) - create a new list that contains values in user_values that are less than or equal to upper_threshold. Return the newly created list.


def get_user_values():
    # Define a function called get_user_values() to collect user input
    num_integers = int(input())
    # Read the number of integers from user input and convert it to an integer
    values = []
    # Create an empty list called values to store the integers
    for _ in range(num_integers):
        # Iterate num_integers times to get each integer from user input
        value = int(input())
        # Read an integer from user input and convert it to an integer
        values.append(value)
        # Add the integer to the values list
    threshold = int(input())
    # Read the threshold value from user input and convert it to an integer
    return values, threshold
    # Return the list of integers and the threshold value as a tuple

def ints_less_than_or_equal_to_threshold(user_values, upper_threshold):
    # Define a function called ints_less_than_or_equal_to_threshold() to filter integers
    return [value for value in user_values if value <= upper_threshold]
    # Use list comprehension to filter integers from user_values that are less than or equal to upper_threshold
    # Return the filtered list of integers

def main():
    # Define the main function to orchestrate the program
    user_values, threshold = get_user_values()
    # Call get_user_values() to get the list of integers and the threshold value
    filtered_values = ints_less_than_or_equal_to_threshold(user_values, threshold)
    # Call ints_less_than_or_equal_to_threshold() to filter integers based on the threshold
    for value in filtered_values:
        # Iterate through the filtered values
        print(value)
        # Print each filtered value

if __name__ == "__main__":
    main()
    # Call the main function if the script is executed directly