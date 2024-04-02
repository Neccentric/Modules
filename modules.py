# classes are a way to organize data and functionality together.
# We can add more organization to our code with something called a Module.

import math
print("The value of Pie is: ", math.pi)
# Module groups related classes and data and make them accessible from one place.
print("The square root of 16 is: ", math.sqrt(16)) 
# Python has a lot of built-in modules.
# We can find out the functionality a module has by using the "help()" instruction with the name of the module between the parentheses.
# help(math)
print(math.ceil(34.89))


# From.
    # Statistics is another built-in module. It helps out with statistic functions like the mean of a list.
        # we're able to use multiple different modules in thesame file by adding a comma between the module we're importing.

import statistics,math

scores = [4,4,3,6,1,2,8,4]
mean = statistics.mean(scores)
print(f"Mean score is {mean}")
print(f"Value of pi is: {math.pi}")

# Sometimes we want to use just parts of a module, and not the whole functionalityp, In that case, we can use the Keyword
# "From" to extract only the functionality we want to use.

# import re
from math import pi

print("Value of Pi is: ", pi)

from statistics import mean

test_scores = [33,28,30,25]
result = mean(test_scores)
print(f" Mean result is: {result}")
# help(re)

# Alias.

    # We can modify the name of module we're importing. 
import statistics as stats

sales = [23, 45,32,45,43,26,46,18,19,30]
median = stats.median(sales)
print(median)

# Giving a new name to a module we're importing is known as "aliasing".

import math as math_constants

math = "SSS3 or Grade 12 constants"

print(math)

print("pi:")
print(math_constants.pi)

print("Euler's number:")
print(math_constants.e)
print(math_constants.floor(34.63))