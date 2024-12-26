
# 4.18 LAB: Exact change

# Write a program with total change amount as an integer input, and output the change using the fewest coins, one coin type per line. The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies. Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.

# Ex: If the input is:

# 0 

# (or less than 0), the output is:

# No change 

# Ex: If the input is:

# 45

# the output is:

# 1 Quarter
# 2 Dimes 

def exact_change(change):
    if change <= 0:
        print("No change")
        return

    dollars = change // 100
    change %= 100
    quarters = change // 25
    change %= 25
    dimes = change // 10
    change %= 10
    nickels = change // 5
    pennies = change % 5

    if dollars > 0:
        if dollars == 1:
            print(f"{dollars} Dollar")
        else:
            print(f"{dollars} Dollars")

    if quarters > 0:
        if quarters == 1:
            print(f"{quarters} Quarter")
        else:
            print(f"{quarters} Quarters")

    if dimes > 0:
        if dimes == 1:
            print(f"{dimes} Dime")
        else:
            print(f"{dimes} Dimes")

    if nickels > 0:
        if nickels == 1:
            print(f"{nickels} Nickel")
        else:
            print(f"{nickels} Nickels")

    if pennies > 0:
        if pennies == 1:
            print(f"{pennies} Penny")
        else:
            print(f"{pennies} Pennies")


# Example usage:
if __name__ == "__main__":
    input_change = int(input())
    exact_change(input_change)
