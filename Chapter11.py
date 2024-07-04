### TUPLES ###

# Tuples are like lists
t = "l", "u", "p", "i", "n"
print(type(t))
print(t)

t = tuple("lupin")
print(t)

t = tuple("lup") + ("i", "n")
print(t)

t = tuple("spam") * 2
print(t)

t = sorted(tuple("lupin"))
print(t)

t = tuple(reversed(tuple("lupin")))
print(t)

# But tuples are immutable
d = {}
d[1, 2] = 3
d[3, 4] = 7

print(d[1, 2])

t = (3, 4)
print(d[t])

t = tuple("abc")
s = [1, 2, 3]
d = {t: s}
print(d)

d = {"one": 1, "two": 2}

for item in d.items():
    key, value = item
    print(key, "->", value)

# Argument packing
def mean(*args):
    return sum(args) / len(args)

print(mean(1, 2, 3))

t = (7, 3)
print(divmod(*t))

# Zip
scores1 = [1, 2, 4, 5, 1, 5, 2]
scores2 = [5, 5, 2, 2, 5, 2, 3]

for pair in zip(scores1, scores2):
    print(pair)

for team1, team2 in zip(scores1, scores2):
    print(team1, team2)

t = list(zip(scores1, scores2))
print(t)

for index, element in enumerate('abc'):
    print(index, element)

# Comparing and sorting
print((0, 1, 2) < (0, 3, 4))
print((0, 1, 200000) < (0, 3, 4))

### Exercise 1 ###

# In this chapter I said that tuples can be used as keys in dictionaries
# because they are hashable, and they are hashable because they are
# immutable. But that is not always true.

# If a tuple contains a mutable value, like a list or a dictionary, the
# tuple is no longer hashable because it contains elements that are not
# hashable. As an example, here's a tuple that contains two lists of integers.

list0 = [1, 2, 3]
list1 = [4, 5]

t = (list0, list1)
print(t)

print("Solution 1")
t[1].append(6)
print(t)
print("")

### Exercise 2 ###

# In this chapter we made a dictionary that maps from each letter to
# its index in the alphabet.

letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = range(len(letters))
letter_map = dict(zip(letters, numbers))

# We can use letter_map and letters to encode and decode words using
# a Caesar cipher.

# A Caesar cipher is a weak form of encryption that involves shifting
# each letter by a fixed number of places in the alphabet, wrapping
# around to the beginning if necessary. For example, 'a' shifted by 2
# is 'c' and 'z' shifted by 1 is 'a'.

# Write a function called shift_word that takes as parameters a string
# and an integer, and returns a new string that contains the letters
# from the string shifted by the given number of places.

# To test your function, confirm that "cheer" shifted by 7 is "jolly"
# and "melon" shifted by 16 is "cubed".

# Hints: Use the modulus operator to wrap around from 'z' back to 'a'.
# Loop through the letters of the word, shift each one, and append the
# result to a list of letters. Then use join to concatenate the letters
# into a string.

print("Solution 2")
def shift_word(word, n):
    N = len(letters)
    
    new = ""
    for w in word:
        m = letter_map[w]
        nnew, mnew = divmod(n + m, N)
        new += letters[mnew]

    return new

print(shift_word('cheer', 7))  # 'jolly'
print(shift_word('melon', 16)) # 'cubed'
print(shift_word('abc', 26))   # 'abc'
print(shift_word('abc', 26*6)) # 'abc'
print("")

### Exercise 3 ###

def second_element(t):
    return t[1]

def most_frequent_letters(string):
    d = {}
    for s in string:
        d[s] = d.get(s, 0) + 1

    d = sorted(d.items(), key=second_element, reverse=True)
    
    for di in d:
        print(di[0])

print("Solution 3")
most_frequent_letters('brontosaurus')
string = open('pg345.txt', encoding="utf-8").read()
most_frequent_letters(string)
print("")

### Exercise 4 ###

print("Solution 4: Missing")
print("")

### Exercise 5 ###

# Write a function called word_distance that takes two words with the
# same length and returns the number of places where the two words differ.

# Hint: Use zip to loop through the corresponding letters of the words.

def word_distance(word1, word2):
    total = 0
    for (w1, w2) in zip(word1, word2):
        if not w1 == w2:
            total += 1
    
    return total

print("Solution 5")
print(word_distance("hello", "hxllo"))      # 1
print(word_distance("ample", "apply"))      # 2
print(word_distance("kitten", "mutton"))    # 3
print("")

### Exercise 6 ###

print("Solution 6: Missing")
print("")

### Exercise 7 ###

print("Solution 7: Missing")
print("")