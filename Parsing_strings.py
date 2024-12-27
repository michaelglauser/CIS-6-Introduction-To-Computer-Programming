
# 7.12 LAB: Warm up: Parsing strings

# (1) Prompt the user for a string that contains two strings separated by a comma. (1 pt)
# 
#     Examples of strings that can be accepted:
#         Jill, Allen
#         Jill , Allen
#         Jill,Allen

# Ex:

# Enter input string:
# Jill, Allen


# (2) Report an error if the input string does not contain a comma. Continue to prompt until a valid string is entered. Note: If the input contains a comma, then assume that the input also contains two strings. (2 pts)
# 
# Ex:
# 
# Enter input string:
# Jill Allen
# Error: No comma in string.
# 
# Enter input string: Jill, Allen
# 
# 
# (3) Using string splitting, extract the two words from the input string and then remove any spaces. Output the two words. (2 pts)
# 
# Ex:
# 
# Enter input string:
# Jill, Allen
# First word: Jill
# Second word: Allen
# 
# 
# (4) Using a loop, extend the program to handle multiple lines of input. Continue until the user enters q to quit. (2 pts)
# 
# Ex:
# 
# Enter input string:
# Jill, Allen
# First word: Jill
# Second word: Allen

# Enter input string:
# Golden , Monkey
# First word: Golden
# Second word: Monkey

# Enter input string:
# Washington,DC
# First word: Washington
# Second word: DC
# 
# Enter input string:
# q

strInput=""
while(strInput!="q"):
    strInput = input('Enter input string:\n')
    if"," in strInput:
        words = strInput.split(",")
        FW = words[0].split()
        SW = words[1].split()
        print("First word:",FW[0])
        print("Second word:",SW[0])
        print("")
    elif(strInput=="q"):
        break
    else:
        print("Error: No comma in string.\n")