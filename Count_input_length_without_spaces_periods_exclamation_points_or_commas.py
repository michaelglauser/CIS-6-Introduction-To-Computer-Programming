
# 5.15 LAB: Count input length without spaces, periods, exclamation points, or commas

# Given a line of text as input, output the number of characters excluding spaces, periods, exclamation points, or commas.

# Ex: If the input is:

# Listen, Mr. Jones, calm down.

# the output is:

# 21

# Note: Account for all characters that aren't spaces, periods, exclamation points, or commas (Ex: "r", "2", "?").


inputString=input()#"Enter string : "

number_of_characters = 0

for char in inputString:
  if char!=" " and char!="." and char!="," and char!="!":
    number_of_characters=number_of_characters+1

print(number_of_characters)#"Number of characters : ",

