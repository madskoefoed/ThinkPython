# https://colab.research.google.com/github/AllenDowney/ThinkPython/blob/v3/chapters/chap01.ipynb#scrollTo=3b4a1f57

### Exercise 1 ###

# How many seconds are there in 42 minutes and 42 seconds?
solution_1 = 60 * 42 + 42
print("Solution 1:", solution_1)

### Exercise 2 ###

# How many miles are there in 10 kilometres? (hint: 1.61 km = 1 mile)
solution_2 = 10 / 1.61
print("Solution 2:", round(solution_2, 1))

### Exercise 3 ###

# If you run 10 kilometer race in 42 minutes and 42 seonds,
# what is your average pace in seconds per mile?
solution_3 = solution_1 / solution_2
print("Solution 3:", round(solution_3))

### Exercise 4 ###

# What is your average pace in minutes and seconds per mile?
tmp_4_1 = solution_3 // 60
tmp_4_2 = solution_3 - 60 * tmp_4_1
print("Solution 4:", tmp_4_1, "minutes and", round(tmp_4_2), "seconds")

### Exercise 5 ##

# What is your average speed in miles per hour?

# solution_3 = seconds / mile
# 1 / solution_3 = mile / seconds
# solution_5 = 1/ * solution_3 * seconds / hour
# solution_5 = seconds / hour * mile / seconds = mile / hour
solution_5 = 60**2 / solution_3
print("Solution 5:", round(solution_5, 1))