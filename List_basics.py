
# 3.19 LAB: List basics

# Given the user inputs, complete a program that does the following tasks:

#     Define a list, my_list, containing the user inputs: my_flower1, my_flower2, and my_flower3 in the same order.
#     Define a list, your_list, containing the user inputs, your_flower1 and your_flower2, in the same order.
#     Define a list, our_list, by concatenating my_list and your_list.
#     Append the user input, their_flower, to the end of our_list.
#     Replace my_flower2 in our_list with their_flower.
#     Remove the first occurrence of their_flower from our_list without using index().
#     Remove the second element of our_list.

# Observe the output of each print statement carefully to understand what was done by each task of the program.

# Ex: If the input is:

# rose
# peony
# lily
# rose
# daisy
# aster

# the output is:

# ['rose', 'peony', 'lily', 'rose', 'daisy']
# ['rose', 'peony', 'lily', 'rose', 'daisy', 'aster']
# ['rose', 'aster', 'lily', 'rose', 'daisy', 'aster']
# ['rose', 'lily', 'rose', 'daisy', 'aster']
# ['rose', 'rose', 'daisy', 'aster']


my_flower1 = input()
my_flower2 = input()
my_flower3 = input()

your_flower1 = input()
your_flower2 = input()

their_flower = input()

# 1. Define my_list containing my_flower1, my_flower2, and my_flower3
my_list = [my_flower1, my_flower2, my_flower3]

# 2. Define your_list containing your_flower1 and your_flower2
your_list = [your_flower1, your_flower2]

# 3. Define our_list by concatenating my_list and your_list
our_list = my_list + your_list
print(our_list)

# 4. Append their_flower to the end of our_list
our_list.append(their_flower)
print(our_list)

# 5. Replace my_flower2 in our_list with their_flower
index_to_replace = our_list.index(my_flower2)
our_list[index_to_replace] = their_flower
print(our_list)

# 6. Remove the first occurrence of their_flower from our_list
our_list.remove(their_flower)
print(our_list)
# 7. Remove the second element of our_list
del our_list[1]

# Print the lists at each stage
print(our_list)