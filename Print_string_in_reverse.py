
# 5.18 LAB: Print string in reverse

# Write a program that takes in a line of text as input, and outputs that line of text in reverse. The program repeats, ending when the user enters "Done", "done", or "d" for the line of text.

# Ex: If the input is:

# Hello there
# Hey
# done

# then the output is:

# ereht olleH
# yeH

reversed_lines = []

while True:
    line = input()

    if line.lower() in ["Done", "done", "d"]:
        break  # Exit the loop and proceed to the next step

    reversed_line = line[::-1]

    reversed_lines.append(reversed_line)

for reversed_line in reversed_lines:
    print(reversed_line)
