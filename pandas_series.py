import pandas as pd
import scipy
import numpy as np
from pydataset import data
import random

fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", 
          "honeycrisp apple", "tomato", "watermelon", "honeydew", 
          "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry",
          "gooseberry", "papaya"]

fruits = pd.Series(fruits)

# Determine the number of elements in fruits.
print('\nthe number of elements in fruits is', fruits.count(),'\n')

# Output only the index from fruits.

print(list(fruits.index))

# Output only the values from fruits.
for i in fruits.values:
    print(i)

# Confirm the data type of the values in fruits.
for i in fruits.values:
    print(type(i))


# Output only the first five values from fruits. 
print(fruits.head(5))
print()

# Output the last three values. 
print(fruits.tail(5))
print()

# Output two random values from fruits.
for i in range(2):  
    print(random.choice(fruits))
print()


# Run the .describe() on fruits to see what information 
# it returns when called on a Series with string values.
print('when I use describe:')
print(fruits.describe())

# Run the code necessary to produce only the unique string values from fruits
print()
for i in fruits.unique():
    print(i)
print()

# Determine how many times each unique string value occurs in fruits.
print(fruits.value_counts())
print()



# Determine the string value that occurs most frequently in fruits.
# print(fruits.value_counts().max())
# print(fruits.mode())
# print()
print('largest:', fruits.value_counts().nlargest(keep='first'),'\n')
print()


# Determine the string value that occurs least frequently in fruits.
print(fruits.value_counts().nsmallest(keep='all'))

