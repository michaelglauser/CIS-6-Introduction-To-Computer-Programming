
# 6.18 LAB: Track laps to miles

# One lap around a standard high-school running track is exactly 0.25 miles. Define a function named laps_to_miles that takes a number of laps as a parameter, and returns the number of miles. Then, write a main program that takes a number of laps as an input, calls function laps_to_miles() to calculate the number of miles, and outputs the number of miles.

# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print(f'{your_value:.2f}')

# Ex: If the input is:

# 7.6

# the output is:

# 1.90

# Ex: If the input is:

# 2.2

# the output is:

# 0.55

# The program must define and call the following function:
# def laps_to_miles(user_laps)

def laps_to_miles(user_laps):
    miles = user_laps * 0.25
    return miles

def main():
    user_laps = float(input())
    miles = laps_to_miles(user_laps)
    print(f'{miles:.2f}')
    
if __name__ == '__main__':
    main()

