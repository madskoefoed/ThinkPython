### DICTIONARIES ###

lst = ["zero", "one", "two"]
print(lst)
print(lst[1])

numbers = {}
print(numbers)

numbers["zero"] = 0
print(numbers)

numbers["one"] = 1
numbers["two"] = 2
print(numbers)

print("Length of numbers:", len(numbers))

# Creating dictionaries
numbers = {"zero": 0, "one": 1, "two": 2}
print(numbers)

numbers_copy = dict(numbers)
print(numbers_copy)

# The 'in' operator
print("one" in numbers) # Checks keys
print(1 in numbers)     # Does not check values
print(1 in numbers.values())

word_list = open('words.txt').read().split()
len(word_list)

def reverse_word(word):
    return ''.join(reversed(word))

def too_slow():
    count = 0
    for word in word_list:
        if reverse_word(word) in word_list:
            count += 1
    return count
#print(too_slow())

word_dict = {}
for word in word_list:
    word_dict[word] = 1

def much_faster():
    count = 0
    for word in word_dict:
        if reverse_word(word) in word_dict:
            count += 1
    return count

print(much_faster())

# A collection of counters
counter = {}
counter['a'] = 1
counter['a'] += 1
print(counter)

def value_counts(string):
    counter = {}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter

counter = value_counts('brontosaurus')
print(counter)

# Looping and dictionaries
counter = value_counts("banana")
print(counter)

for key in counter:
    print(key)

for value in counter.values():
    print(value)

for key in counter:
    value = counter[key]
    print(key, value)

# Lists and dictionaries
d = {4: ["r", "o", "u", "s"]}
print(d)

### Exercise 1 ###

# Dictionaries have a method called get that takes a key and a
# default value. If the key appears in the dictionary, get returns
# the corresponding value; otherwise it returns the default value.
# For example, here's a dictionary that maps from the letters in a
# string to the number of times they appear.

print("Solution 1")

counter = value_counts("brontosaurus")
print(counter.get("b", 0))
print(counter.get("c", 0))
print(counter.get("o", 0))

def value_counts(string):
    counter = {}
    for letter in string:
        counter[letter] = counter.get(letter, 0) + 1
    return counter

counter = value_counts("brontosaurus")
print(counter.get("b", 0))
print(counter.get("c", 0))
print(counter.get("o", 0))
print("")

### Exercise 2 ###

# What is the longest word you can think of where each letter appears
# only once? Let's see if we can find one longer than unpredictably.

# Write a function named has_duplicates that takes a sequence -- like
# a list or string -- as a parameter and returns True if there is any
# element that appears in the sequence more than once.

def has_duplicates(t):
    d = value_counts(t)
    return (not max(d.values()) == 1)

print("Solution 2")
print(has_duplicates('banana'))         # True
print(has_duplicates('ambidextrously')) # False
print(has_duplicates([1, 2, 2]))        # True
print(has_duplicates([1, 2, 3]))        # False
print("")

no_repeats = []

for word in word_list:
    if len(word) > 12 and not has_duplicates(word):
        no_repeats.append(word)
        
print(no_repeats)

### Exercise 3 ###

# Write function called find_repeats that takes a dictionary that maps
# from each key to a counter, like the result from value_counts. It should
# loop through the dictionary and return a list of keys that have counts
# greater than 1. You can use the following outline to get started.

def find_repeats(counter):
    l = []
    for key in counter:
        if counter[key] > 1:
            l.append(key)

    return l

print("Solution 3")
counter1 = value_counts("banana")
print(find_repeats(counter1))
counter1 = value_counts([1, 2, 3, 2, 1])
print(find_repeats(counter1))
print("")

### Exercise 4 ###

# Suppose you run value_counts with two different words and
# save the results in two dictionaries.

counter1 = value_counts('brontosaurus')
counter2 = value_counts('apatosaurus')

print("Counter 1:", counter1)
print("Counter 2:", counter2)

# Each dictionary maps from a set of letters to the number of times
# they appear. Write a function called add_counters that takes two
# dictionaries like this and returns a new dictionary that contains all
# of the letters and the total number of times they appear in either word.

def add_counters(dict1, dict2):
    ds = dict()
    ks = dict1.keys() | dict2.keys()
    for k in ks:
        ds[k] = dict1.get(k, 0) + dict2.get(k, 0)

    return ds

print("Solution 4")
print(add_counters(counter1, counter2))
print("")

### Exercise 5 ###

# A word is "interlocking" if we can split it into two words by taking
# alternating letters. For example, "schooled" is an interlocking word
# because it can be split into "shoe" and "cold".

# To select alternating letters from a string, you can use a slice
# operator with three components that indicate where to start, where
# to stop, and the "step size" between the letters.

# In the following slice, the first component is 0, so we start with
# the first letter. The second component is None, which means we should
# go all the way to the end of the string. And the third component is 2,
# so there are two steps between the letters we select.

word = 'schooled'
first = word[0:None:2]
print(first)

# Instead of providing None as the second component, we can get the same
# effect by leaving it out altogether. For example, the following slice
# selects alternating letters, starting with the second letter.

second = word[1::2]
print(second)

# Write a function called is_interlocking that takes a word as an argument
# and returns True if it can be split into two interlocking words.

def is_interlocking(word, word_list):

    if len(word) == 1:
        return False

    word = word.lower()
    word_list = [w.lower() for w in word_list]

    w1 = word[0::2]
    w2 = word[1::2]

    if w1 in word_list and w2 in word_list:
        return True
    else:
        return False

print("Solution 5")
print("Is interlocking?", is_interlocking("schooled", word_list))

def count_interlocking(word_list):
    total = 0
    for w in word_list:
        total += is_interlocking(w, word_list)
    
    return total

print("Total number of interlocking words:", count_interlocking(word_list[0:1000]))
print("")