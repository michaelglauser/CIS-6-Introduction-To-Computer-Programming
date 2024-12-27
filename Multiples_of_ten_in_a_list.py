
# 6.27 LAB: Multiples of ten in a list

# Write a program that reads a list of integers, and outputs whether the list contains all multiples of 10, no multiples of 10, or mixed values. Define a function named is_list_mult10 that takes a list as a parameter, and returns a boolean that represents whether the list contains all multiples of ten. Define a function named is_list_no_mult10 that takes a list as a parameter and returns a boolean that represents whether the list contains no multiples of ten.

# Then, write a main program that takes an integer, representing the size of the list, followed by the list values. The first integer is not in the list.

# Ex: If the input is:

# 5
# 20
# 40
# 60
# 80
# 100

# the output is:

# all multiples of 10

# Ex: If the input is:

# 5
# 11
# -32
# 53
# -74
# 95

# the output is:

# no multiples of 10

# Ex: If the input is:

# 5
# 10
# 25
# 30
# 40
# 55

# the output is:

# mixed values

# The program must define and call the following two functions. is_list_mult10() returns true if all integers in the list are multiples of 10 and false otherwise. is_list_no_mult10() returns true if no integers in the list are multiples of 10 and false otherwise.
# def is_list_mult10(my_list)
# def is_list_no_mult10(my_list)

def is_list_mult10(my_list):

    return all(x % 10 == 0 for x in my_list)

def is_list_no_mult10(my_list):

    return all(x % 10 != 0 for x in my_list)

def main():

    size = int(input())
    

    values = [int(input()) for _ in range(size)]


    if is_list_mult10(values):
        print("all multiples of 10")
    elif is_list_no_mult10(values):
        print("no multiples of 10")
    else:
        print("mixed values")

if __name__ == "__main__":
    main()
