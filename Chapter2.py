# Import statement
import math

print("Pi:", math.pi)
print("Square root of 25:", math.sqrt(25))
print("5 squared:", math.pow(5, 2))

### Exercise 1 ###

# The volume of a sphere with radius  r  is  43πr3 .
# What is the volume of a sphere with radius 5?
# Start with a variable named radius and then assign
# the result to a variable named volume.
# Display the result.
# Add comments to indicate that radius is in centimeters and
# volume in cubic centimeters.

print("Solution 1")
radius = 5
print("Radius:", radius, "cm")
volume = math.pow(radius, 3) * math.pi * 4/3
print("Volume:", round(volume, 1), "cm3")

### Exercise 2 ###

# A rule of trigonometry says that for any value of x, (cosx)^2 + (sinx)^2 = 1.
# Let's see if it's true for a specific value of x like 42.

# Create a variable named x with this value.
# Then use math.cos and math.sin to compute the sine and cosine of x,
# and the sum of their squared.

# The result should be close to 1.
# It might not be exactly 1 because floating-point arithmetic
# is not exact---it is only approximately correct.

x = 42
x = math.cos(x)**2 + math.sin(x)**2
print("Solution 2")
print("cos(x)^2 + sin(x)^2 =", x)

### Exercise 1 ###

# In addition to pi, the other variable defined in the math module is e,
# which represents the base of the natural logarithm,
# written in math notation as e.
# If you are not familiar with this value, ask a virtual assistant
# "What is math.e?" Now let's compute e^2 three ways:

# Use math.e and the exponentiation operator (**).

# Use math.pow to raise math.e to the power 2.

# Use math.exp, which takes as an argument a value, x, and computes e^x.

# You might notice that the last result is slightly different from
# the other two. See if you can find out which is correct.

print("Solution 3")
print("math.e ** 2:", math.e**2)
print("math.pow:   ", math.pow(math.e, 2))
print("math.exp:   ", math.exp(2))