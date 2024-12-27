
# 8.29 LAB: Word frequencies (dictionaries)

# Implement the build_dictionary() function to build a word frequency dictionary from a list of words.

# Ex: If the words list is:

# ["hey", "hi", "Mark", "hi", "mark"]

# the dictionary returned from calling build_dictionary(words) is:

# {'hey': 1, 'hi': 2, 'Mark': 1, 'mark': 1}

# Ex: If the words list is:

# ["zyBooks", "now", "zyBooks", "later", "zyBooks", "forever"]

# the dictionary returned from calling build_dictionary(words) is:

# {'zyBooks': 3, 'now': 1, 'later': 1, 'forever': 1}

# The main code builds the word list from an input string, calls build_dictionary() to build the dictionary, and displays the dictionary sorted by key value.

# Ex: If the input is:

# hey hi Mark hi mark

# the output is:

# Mark - 1
# hey - 1
# hi - 2
# mark - 1

def build_dictionary(words):
    
    new_dict = {}
    
    for curr_word in words:
        
        if curr_word in new_dict:
            new_dict[curr_word] += 1
        
        else:
            new_dict[curr_word] = 1
    

    return new_dict

if __name__ == '__main__':
    words = input().split()
    your_dictionary = build_dictionary(words)
    sorted_keys = sorted(your_dictionary.keys())
    for key in sorted_keys:
        print(key + ' - ' + str(your_dictionary[key]))
