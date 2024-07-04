from os.path import basename, exists

def download(url):
    filename = basename(url)
    if not exists(filename):
        from urllib.request import urlretrieve

        local, _ = urlretrieve(url, filename)
        print("Downloaded " + str(local))
    return filename

download('https://raw.githubusercontent.com/AllenDowney/ThinkPython/v3/words.txt')

### Exercise 1 ###

# Write a function named uses_none that takes a word and a string of
# forbidden letters, and returns True if the word does not use any of
# the forbidden letters.

# Here's an outline of the function that includes two doctests.
# Fill in the function so it passes these tests, and add at least one
# more doctest.

def uses_none(word, forbidden):
    for f in forbidden:
        if f in word:
            return False
    return True

print("Solution 1")
print(uses_none('banana', 'xyz'))   # Should be True
print(uses_none('apple', 'efg'))    # Should be False
print(uses_none('fruit', 'rgt'))    # Should be False
print("")

### Exercise 2 ###

# Write a function called uses_only that takes a word and a string of
# letters, and that returns True if the word contains only letters
# in the string.

def uses_only(word, available):
    word = set(word)
    available = set(available)
    diff = word - available
    if len(diff) == 0:
        return True
    else:
        return False

print("Solution 2")
print(uses_only('banana', 'ban'))   # Should be True
print(uses_only('apple', 'apl'))    # Should be False (e)
print(uses_only('fruit', 'fru'))    # Should be False (i and t)
print("")

### Exercise 3 ###

# Write a function called uses_all that takes a word and a string
# of letters, and that returns True if the word contains all of the
# letters in the string at least once.

def uses_all(word, required):
    word = set(word)
    required = set(required)
    diff = required - word
    if len(diff) == 0:
        return True
    else:
        return False

print("Solution 3")
print(uses_all('banana', 'ban'))   # Should be True
print(uses_all('apple', 'api'))    # Should be False
print(uses_all('fruit', 'fru'))    # Should be True
print("")

### Exercise 4 ###

# The New York Times publishes a daily puzzle called "Spelling Bee"
# that challenges readers to spell as many words as possible using
# only seven letters, where one of the letters is required.
# The words must have at least four letters.

# For example, on the day I wrote this, the letters were ACDLORT,
# with R as the required letter. So "color" is an acceptable word,
# but "told" is not, because it does not use R, and "rat" is not
# because it has only three letters. Letters can be repeated, so
# "ratatat" is acceptable.

# Write a function called check_word that checks whether a given
# word is acceptable. It should take as parameters the word to check,
# a string of seven available letters, and a string containing the
# single required letter. You can use the functions you wrote in
# previous exercises.

def check_word(word, available, required):
    if len(word) < 4:
        return False
    
    word      = word.lower()
    available = available.lower()
    required  = required.lower()

    if not required in word:
        return False

    for w in word:
        if not w in available:
            return False

    return True
    
print("Solution 4")
print(check_word('color', 'ACDLORT', 'R'))     # True
print(check_word('ratatat', 'ACDLORT', 'R'))   # True
print(check_word('rat', 'ACDLORT', 'R'))       # False
print(check_word('told', 'ACDLORT', 'R'))      # False
print(check_word('bee', 'ACDLORT', 'R'))       # False
print("")

### Exercise 5 ###

# According to the "Spelling Bee" rules,
#   Four-letter words are worth 1 point each.
#   Longer words earn 1 point per letter.
#   Each puzzle includes at least one "pangram" which uses every letter.
#   These are worth 7 extra points!

# Write a function called score_word that takes a word and a string of
# available lessons and returns its score. You can assume that the word
# is acceptable.

def word_score(word, available):
    word      = word.lower()
    available = available.lower()

    # Return a score of 0 if the word is too short
    if len(word) < 4:
        return 0

    check = True
    for w in word:
            if not w in available:
                check = False

    if check:
        if len(word) == 4:
            score = 1
        else:
            score = len(word)
    else:
        return 0

    extra = (set(word) & set(available) == set(available)) * 7

    return score + extra

print("Solution 5")
print(word_score('card', 'ACDLORT'))        # 1
print(word_score('color', 'ACDLORT'))       # 5
print(word_score('cartload', 'ACDLORT'))    # 15
print(word_score('zymurgy', 'ACDLORT'))     # 1
print("")

### Exercise 6 ###
print("Solution 6")

available = 'ACDLORT'
required = 'R'
total = 0

file_object = open('words.txt')
for line in file_object:
    word = line.strip()
    if check_word(word, available, required):
        score = word_score(word, available)
        total = total + score
        print(word, score, total)
        
print("Total score", total)
print("")