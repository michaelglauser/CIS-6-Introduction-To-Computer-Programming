
# 7.9 LAB: Palindrome

# A palindrome is a word or a phrase that is the same when read both forward and backward. Examples are: "bob," "sees," or "never odd or even" (ignoring spaces). Write a program whose input is a word or phrase, and that outputs whether the input is a palindrome.

# Ex: If the input is:

# bob

# the output is:

# palindrome: bob

# Ex: If the input is:

# bobby

# the output is:

# not a palindrome: bobby

# Hint: Start by removing spaces. Then check if the string equals itself in reverse.

def is_palindrome(word):
    word = word.replace(" ", "").lower()
    
    if word == word[::-1]:
        return True
    else:
        return False

def main():
    input_word = input()

    if is_palindrome(input_word):
        print("palindrome:", input_word)
    else:
        print("not a palindrome:", input_word) #[::-1]

if __name__ == "__main__":
    main()