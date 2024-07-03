### Exercise 1 ###

# Use incremental development to write a function called hypot that
# returns the length of the hypotenuse of a right triangle given the
# lengths of the other two legs as arguments.

# Note: There's a function in the math module called hypot that does
# the same thing, but you should not use it for this exercise!

# Even if you can write the function correctly on the first try,
# start with a function that always returns 0 and practice making
# small changes, testing as you go. When you are done, the function
# should only return a value -- it should not display anything.

print("Solution 1")

import math

def hypot(s1, s2):
    return 0.0

print(hypot(5, 8))

def hypot(s1, s2):
    s1 = math.pow(s1, 2)
    s2 = math.pow(s2, 2)
    return s1 + s2

print(hypot(5, 8))

def hypot(s1, s2):
    return math.sqrt(math.pow(s1, 2) + math.pow(s2, 2))

print(hypot(5, 8))

print("Check:", math.hypot(5, 8))
print("")

### Exercise 2 ###

# Write a boolean function, is_between(x, y, z),
# that returns True if x < y < z or if  z < y < x, and False otherwise.

print("Solution 2")

def is_between(x, y, z):
    if y > x and z > y:
        return True
    elif y > z and x > y:
        return True
    else:
        return False

print(is_between(1, 2, 3)) # Should be True
print(is_between(3, 2, 1)) # Should be True
print(is_between(1, 3, 2)) # Should be False
print(is_between(2, 3, 1)) # Should be False
print("")

### Exercise 3 ###

def Ackermann(m, n):
    if m < 0 or n < 0:
        ValueError("m and n must be positive values")
    elif m == 0:
        x = n + 1
    elif m > 0 and n == 0:
        x = Ackermann(m-1, 1)
    else:
        x = Ackermann(m-1, Ackermann(m, n-1))
    return x

print("Solution 3")
#print(Ackermann(5, 5)) # Recursion error
print(Ackermann(3, 2)) # Should be 29
print(Ackermann(3, 3)) # Should be 61
print(Ackermann(3, 4)) # Should be 125
print("")

### Exercise 4 ###

# A number, a, is a power of b if it is divisible by b and a/b
# is a power of b. Write a function called is_power that takes
# parameters a and b and returns True if a is a power of b.
# Note: you will have to think about the base case.

def is_power(a, b):
    if a <= 0 or b <= 0:
        return False
    if a == 1:
        return True
    if b == 1:
        return a == 1
    if a % b == 0:
        return is_power(a // b, b)
    else:
        return False

print("Solution 4")
print(is_power(65536, 2))   # Should be True
print(is_power(27, 3))      # Should be True
print(is_power(24, 2))      # Should be False
print(is_power(1, 17))      # Should be True
print("")

### Exercise 5 ###

# The greatest common divisor (GCD) of a and b is the largest number
# that divides both of them with no remainder.

# One way to find the GCD of two numbers is based on the observation
# that if r is the remainder when a is divided by b, then
# gcd(a,b) = gcd(b,r). As a base case, we can use gcd(a,0) = a.

# Write a function called gcd that takes parameters a and b and
# returns their greatest common divisor.

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print("Solution 5")
print("gcd(12, 8) =", gcd(12, 8))
print("gcd(13, 17) =", gcd(13, 17))
print("gcd(25, 45) =", gcd(25, 45))