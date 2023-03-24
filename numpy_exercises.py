import numpy as np
# import scipy.stats as stats
import pandas as pd
import scipy


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# How many negative numbers are there?
print(a < 0)
count = 0
for i in a < 0:
    if i == True:
        count +=1
print('\nthere are ', count, 'negative numbers\n')


# How many positive numbers are there?
count = 0
for i in a > 0:
    if i == True:
        count +=1
print('\nthere are ', count, 'positive numbers\n')

# How many even positive numbers are there?
count = 0
for i in (a > 0) & (a % 2 == 0):
    if i == True:
        count +=1
print('\nthere are ', count, 'positive even numbers\n')

# If you were to add 3 to each 
# data point, how many positive numbers would there be?


count = 0
for i in ((a + 3) > 0):
    if i == True:
        count +=1
print(a + 3)
print('\nthere are ', count, 'positive numbers when I add three\n')

# If you squared each number, what would the new 
# mean and standard deviation be?


print('the new standard deviation would be', round((a * a).std(), 2))
print()
print('the new mean would be', round((a * a).mean(), 2))
print()

# A common statistical operation on a dataset is centering. 
# This means to adjust the data such that the mean of the data is 0. 
# This is done by subtracting the mean from each data point. 
# Center the data set. See this link for more on centering.

print('when I center the data it comes out as', (a - a.mean()).mean())

# Calculate the z-score for each data point. 
# Recall that the z-score is given by:
print()
print(scipy.stats.zscore(a))
print()
# ======================================================================================================================================================================


## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = np.array(a)

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = a.sum()
print('the sum of a is', sum_of_a)


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = a.min()
print('\nthe min of a is', min_of_a, '\n')

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = a.max()
print('the max of a is', max_of_a, '\n')

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = a.mean()
print('the mean of a is', mean_of_a, '\n')


# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = a.prod()
print('the product of a is', product_of_a, '\n')


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = a * a
print('if i square all the numbers I get', squares_of_a, '\n')

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
mask = a % 2 == 1
odds_in_a = a[mask]
print('odds in a', odds_in_a)
print()

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
mask = a % 2 == 0
evens_in_a = a[mask]
print('evens in a',evens_in_a)


## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**

# sum_of_b = 0

b = np.array(b)
print('\nthe some of b is', b.sum())

# for row in b:
#     sum_of_b += sum(row)
   

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
print('\nthe mininum of b is', b.min())

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
print('\nthe maximum of b is', b.max())



# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
print('\nthe mean of b is', b.mean())

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
print('\nthe product of all the numbers in b is', b.prod())

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
print('\nthe list of squares in b are as follows', b*b)



# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
            
mask = b % 2 == 1
print('\nthe odds in b are', b[mask])



# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

mask = b % 2 == 0
print('\nthe odds in b are', b[mask])

# Exercise 9 - print out the shape of the array b.
print(b)
print()


# Exercise 10 - transpose the array b.
print(np.transpose(b))

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

print()
print(np.reshape(b,(1,6)))

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
print()
print(np.reshape(b,(6,1)))
## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
c = np.array(c)

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
print()
print('min:', c.min(),'max:', c.max(),'sum:', c.sum(), 'product:', c.prod())
print()

# Exercise 2 - Determine the standard deviation of c.
print('stddev:', round(c.std(),2))
print()

# Exercise 3 - Determine the variance of c.
print("varience:", round(c.var(), 2))
print()

# Exercise 4 - Print out the shape of the array c
print(c)
print()
# Exercise 5 - Transpose c and print out transposed result.
print(np.transpose(c))

# Exercise 6 - Get the dot product of the array c with c. 
cc = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print('\n',np.dot(c, cc))

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
print()
print('sum:',
    (c * np.transpose(c)).sum()
      )
print()
# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
print('product:',
    (c * np.transpose(c)).prod()
    ,
      '\n')

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
d = np.array(d)
# Exercise 1 - Find the sine of all the numbers in d
print('The Sine:',)
print(np.sin(d))
print()
# Exercise 2 - Find the cosine of all the numbers in d
print('The cosine:',)
print(np.cos(d))
# Exercise 3 - Find the tangent of all the numbers in d
print('\nTan:\n', np.tan(d))

# Exercise 4 - Find all the negative numbers in d
mask = d < 0
print('\nNegative:\n',d[mask])
# Exercise 5 - Find all the positive numbers in d
mask = d > 0
print('\nPositive:\n',d[mask])
# Exercise 6 - Return an array of only the unique numbers in d.
print('\n',d)
print('\n', np.unique(d))
# Exercise 7 - Determine how many unique numbers there are in d.
print('\nUnique numbers:', len(np.unique(d)), '\n')
# Exercise 8 - Print out the shape of d.
print(d)
# Exercise 9 - Transpose and then print out the shape of d.
print('\n',np.transpose(d))
# Exercise 10 - Reshape d into an array of 9 x 2
print()
print(np.reshape(d, (9,2)))