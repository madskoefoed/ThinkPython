# Glossary
# recursion: The process of calling the function that is currently executing.

# modulus operator: An operator, %, that works on integers and returns
# the remainder when one number is divided by another.

# boolean expression: An expression whose value is either True or False.

# relational operator: One of the operators that compares its operands:
# ==, !=, >, <, >=, and <=.

# logical operator: One of the operators that combines boolean expressions,
# including and, or, and not.

# conditional statement: A statement that controls the flow of execution
# depending on some condition.

# condition: The boolean expression in a conditional statement that
# determines which branch runs.

# block: One or more statements indented to indicate they are part of
# another statement.

# branch: One of the alternative sequences of statements in a
# conditional statement.

# chained conditional: A conditional statement with a series of
# alternative branches.

# nested conditional: A conditional statement that appears in one
# of the branches of another conditional statement.

# recursive: A function that calls itself is recursive.

# base case: A conditional branch in a recursive function that does
# not make a recursive call.

# infinite recursion: A recursion that doesn't have a base case,
# or never reaches it.
# Eventually, an infinite recursion causes a runtime error.

# newline: A character that creates a line break between two parts
# of a string.


### Exercise 1 ###

# Use floor division and the modulus operator to compute the
# number of days since January 1, 1970 and the current time
# of day in hours, minutes, and seconds.

import math
from time import time
now = time()

solution_1 = int(now // (60**2 * 24))

left = now - solution_1 * math.pow(60, 2) * 24

day_hour = left // 60**2

left = left - day_hour * 60**2

day_min = left // 60

left = round(left - day_min * 60)

print("Solution 1")
print("Number of days since Jan 1, 1970:", solution_1)
print("Current time of day:", day_hour, "hour,", day_min, "min and", left, "sec")

### Exercise 2 ###

# If you are given three sticks, you may or may not be able to arrange
# them in a triangle. For example, if one of the sticks is 12 inches long
# and the other two are one inch long, you will not be able to get the
# short sticks to meet in the middle. For any three lengths, there is a
# test to see if it is possible to form a triangle:

# If any of the three lengths is greater than the sum of the other two,
# then you cannot form a triangle. Otherwise, you can.
# (If the sum of two lengths equals the third, they form what is called
# a "degenerate" triangle.)

# Write a function named is_triangle that takes three integers as arguments,
# and that prints either "Yes" or "No", depending on whether you can or
# cannot form a triangle from sticks with the given lengths.
# Hint: Use a chained conditional.

def is_triangle(s1, s2, s3):
    if s1 > s2 + s3 or s2 > s1 + s3 or s3 > s1 + s2:
        print("No")
    else:
        print("Yes")

is_triangle(4,5,6)
is_triangle(1,2,3)
is_triangle(46,2,3)
is_triangle(1,1,12)