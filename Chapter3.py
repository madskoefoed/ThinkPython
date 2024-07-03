### Exercise 1 ###

# Write a function named print_right that takes a string named text
# as a parameter and prints the string with enough leading spaces
# that the last letter of the string is in the 40th column of the display.

def repeat(word, n):
    return word * n

def print_right(text):
    x = len(text)
    if x > 40:
        print("Error: Length of string > 40")
    elif x == 40:
        print(text)
    else:
        text = repeat(" ", 40-x) + text
        print(text)

print("Solution 1")
print_right("Monty")
print_right("Python's")
print_right("Flying Circus")
print_right("Flying Circus Flying Circus Flying Circus Flying Circus")
print("")

### Exercise 2 ###

# Write a function called triangle that takes a string and an integer and
# draws a pyramid with the given height, made up using copies of the string.
# Here's an example of a pyramid with 5 levels, using the string 'L'.

def triangle(text, n):
    for i in range(n):
        x = 2*i+1
        print(repeat(" ", (n-i)*len(text)) + repeat(text, x) + repeat(" ", n-i))

print("Solution 2")
triangle("Hi", 5)
print("")

### Exercise 3 ###

# Write a function called rectangle that takes a string and two integers
# and draws a rectangle with the given width and height, made up using
# copies of the string. Here's an example of a rectangle with width 5
# and height 4, made up of the string 'H'.

def rectangle(text, n, m):
    for i in range(n):
        print(repeat(text, m))

print("Solution 3")
rectangle("Hi", 5, 3)
print("")

### Exercise 4 ###

# Write a function called bottle_verse that takes a number as a parameter
# and displays the verse that starts with the given number of bottles.

# Hint: Consider starting with a function that can print the first,
# second, or last line of the verse, and then use it to write bottle_verse.

print("Solution 4")

def bottle_line_1(n):
    return str(n) + " bottles of beer on the wall. \n"

def bottle_line_2(n):
    return str(n) + " bottles of beer. \n"

def bottle_line_3():
    return "Take one down, pass it around. \n"

def bottle_verse(n):
    if n > 0:
        for i in range(n, 0, -1):
            x1 = bottle_line_1(i) + \
                bottle_line_2(i) + \
                bottle_line_3() + \
                bottle_line_1(i-1)
            print(x1)
    else:
        print("0 bottles of beer on the wall")

bottle_verse(3)
print("")

### Exercise 4 ###

