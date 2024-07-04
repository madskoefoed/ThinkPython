### LISTS ###

numbers = [42, 123]
print(numbers)

cheeses = ["Cheddar", "Edam", "Gouda"]
print(cheeses)

t = ["spam", 2.0, 5, [10, 20]]
print("Nested:", t)

empty = []
print(empty)

# Lists operations
t1 = [1, 2]
t2 = [3, 4]
t3 = t1 + t2
print(t3)

print(["spam"] * 4)

print(sum(t1))
print(min(t1))
print(max(t1))

# List methods
letters = ["a", "b", "c", "d"]
letters.append("e")
print(letters)

letters.extend(["f", "g"])
print(letters)

letters.pop(0)
print(letters)

letters.remove("d")
print(letters)

# Lists and strings
s = "spam"
t = list(s)
print(t)

s = "pining for the fjords"
t = s.split() # Could also be s.split(" ")
print(t)

delimiter = " "
t = ["pining", "for", "the", "fjords"]
s = delimiter.join(t)
print(s)

word_list = []

for line in open('words.txt'):
    word = line.strip()
    word_list.append(word)
    
print("Length of word list:", len(word_list))

string = open('words.txt').read()
print("Length of word list:", len(string))

word_list = string.split()
print("Length of word list:", len(word_list))

print("Is demotic in word_list:", "demotic" in word_list)
print("Is contrafibularities in word_list:", "contrafibularities" in word_list)

### Exercise 1 ###

# Two words are anagrams if you can rearrange the letters from one to
# spell the other. For example, tops is an anagram of stop.

# One way to check whether two words are anagrams is to sort the
# letters in both words. If the lists of sorted letters are the same,
# the words are anagrams.

# Write a function called is_anagram that takes two strings and
# returns True if they are anagrams.

def is_anagram(word1, word2):
    word1 = list(word1)
    word2 = list(word2)
    
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False

print("Solution 1")
print(is_anagram('tops', 'stop'))   # True
print(is_anagram('skate', 'takes')) # True
print(is_anagram('tops', 'takes'))  # False
print(is_anagram('skate', 'stop'))  # False
print("")

### Exercise 2 ###

# Python provides a built-in function called reversed that takes as
# an argument a sequence of elements -- like a list or string -- and
# returns a reversed object that contains the elements in reverse order.

# A palindrome is a word that is spelled the same backward and forward,
# like "noon" and "rotator". Write a function called is_palindrome that
# takes a string argument and returns True if it is a palindrome
# and False otherwise.

def is_palindrome(word):
    rev = ''.join(reversed(word))

    if word == rev:
        return True
    else:
        return False

print("Solution 2")
print(is_palindrome('bob'))     # True
print(is_palindrome('alice'))   # False
print(is_palindrome('a'))       # True
print(is_palindrome(''))        # True
print("")

### Exercise 3 ###

# Write a function called reverse_sentence that takes as an argument
# a string that contains any number of words separated by spaces.
# It should return a new string that contains the same words in
# reverse order. For example, if the argument is "Reverse this sentence",
# the result should be "Sentence this reverse".

# Hint: You can use the capitalize methods to capitalize the first word
# and convert the other words to lowercase.

def reverse_sentence(input_string):
    words = input_string.split()
    words = ' '.join(reversed(words))
    words = words.capitalize()
    return words

print("Solution 3")
print(reverse_sentence('Reverse this sentence'))        # 'Sentence this reverse'
print(reverse_sentence('Python'))                       # 'Python'
print(reverse_sentence(''))                             # ''
print(reverse_sentence('One for all and all for one'))  # 'One for all and all for one'
print("")

### Exercise 4 ###

# Write a function called total_length that takes a list of strings
# and returns the total length of the strings.
# The total length of the words in word_list should be 902,728.

def total_length(list_of_strings):
    string = ''.join(list_of_strings)
    return len(string)

print("Solution 4")
print(total_length(word_list))  # Should be 902,728
print("")