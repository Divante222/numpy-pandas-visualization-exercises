import pandas as pd
import scipy
import numpy as np
from pydataset import data
import random
import matplotlib.pyplot as plt

fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", 
          "honeycrisp apple", "tomato", "watermelon", "honeydew", 
          "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry",
          "gooseberry", "papaya"]

# fruits = pd.Series(fruits)

# # Determine the number of elements in fruits.
# print('\nthe number of elements in fruits is', fruits.count(),'\n')

# # Output only the index from fruits.

# print(list(fruits.index))

# # Output only the values from fruits.
# for i in fruits.values:
#     print(i)

# # Confirm the data type of the values in fruits.
# for i in fruits.values:
#     print(type(i))

# fruits.dtype


# # Output only the first five values from fruits. 
# print(fruits.head(5))
# print()

# # Output the last three values. 
# print(fruits.tail(5))
# print()

# # Output two random values from fruits.
# for i in range(2):  
#     print(random.choice(fruits))
# print()


# # Run the .describe() on fruits to see what information 
# # it returns when called on a Series with string values.
# print('when I use describe:')
# print(fruits.describe())

# # Run the code necessary to produce only the unique string values from fruits
# print()
# for i in fruits.unique():
#     print(i)
# print()

# # Determine how many times each unique string value occurs in fruits.
# print(fruits.value_counts())
# print()



# # Determine the string value that occurs most frequently in fruits.


# print(fruits.mode())
# print()




# # Determine the string value that occurs least frequently in fruits.
# print(fruits.value_counts().nsmallest(keep='all'))

# print('largest:', fruits.value_counts().nlargest(n=1, keep='first'),'\n')

# print(fruits.value_counts())

# ###################################


# # 5. Exercises Part II

# # Explore more attributes and methods while you continue to work with the fruits Series.

# # Capitalize all the string values in fruits.
# print('\n\n\n')
# print(fruits.str.upper())
# fruits.str.capitalize()

# # Count the letter "a" in all the string values (use string vectorization).
# print('\n')
# print(sum(fruits.str.count('a')))
# print('\n')
# # Output the number of vowels in each and every string value.
# count = 0
# the_dict = {}
# print(fruits)
# for lines in fruits:
    
#     for char in lines:
#         if char in ['a','e','i','o','u']:
#             count +=1
#     the_dict[lines] = count
#     count = 0


# print(the_dict)
# for keys, values in the_dict.items():
#     print(keys, values, 'Vowels')
    
    
# # print(i.count('a' or 'e' or 'i' or 'o' or 'u'))
# # print(fruits.str.count('a' or 'e' or 'i' or 'o' or 'u'))



# # Write the code to get the longest string value from fruits.
# print('\n')

print(max(fruits, key=len))



# # Write the code to get the string values with 5 or more letters in the name.

# print('\n')
# the_list = []

# for i in fruits:
#      if len(i) >= 5:
#          print(i)

# # Find the fruit(s) containing the letter "o" two or more times.
# print('\n')
# the_list = []
# count = 0
# for i in fruits:
#     for j in i:
#         if j == 'o':
#             count += 1
#     if count >= 2:
#         the_list.append(i)
#     count = 0

# for i in the_list:
#     print(i)


# # Write the code to get only the string values containing the substring "berry".
# print('\n\n')
# for i in fruits:
#     if 'berry' in i:
#         print(i)

# # Write the code to get only the string values containing the substring "apple".
# print('\n\n')
# for i in fruits:
#     if 'apple' in i:
#         print(i)

# # Which string value contains the most vowels?
# print('\n\n')
# count = 0
# the_dict = {}
# for i in fruits:
    
#     for j in i:
#         if j in ['a','e','i','o','u']:
#             count +=1
#     the_dict[i] = count
#     count = 0

# highest = 0
# for i in the_dict.values():
#     if i > highest:
#         highest= i

# for i in the_dict.keys():
#     if the_dict[i] == highest:
#         print(i, highest)

# ################################################

# start = '''hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrab
# tjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqpl
# arokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'''

# the_list = []
# for i in start:
#     the_list.append(i)


# letters = pd.Series(the_list)


# print('\n\n')
# # Which letter occurs the most frequently in the letters Series?
# print(letters.value_counts().nlargest(n=1, keep='all'))

# # Which letter occurs the Least frequently?
# print('\n\n')
# print()
# print(letters.value_counts().nsmallest(n=1, keep='all'))
# # How many vowels are in the Series?
# count = 0
# for i in letters:
#     if i in ['a','e','i','o','u']:
#         count += 1

# print('there are', count, 'vowels in letters')
# print('\n\n')
# # How many consonants are in the Series?
# count = 0
# for i in letters:
#     if i not in ['a','e','i','o','u']:
#         count += 1

# print('there are', count, 'consonants in letters')

# # eCreate a Series that has all of the same letters but uppercasd.
# new_series = letters.str.upper()
# print(new_series)

# # Create a bar plot of the frequencies of the 6 most commonly occuring letters.


# # the_bar = pd.Series(letters.value_counts().nlargest(n=6)).plot(kind='bar')
# print('\n')

# # plt.bar(pd.Series(letters.value_counts().nlargest(n=6)), 20)

# # plt.show()

# the_list = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', 
#  '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', 
#  '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', 
#  '$769,681.94', '$452,650.23']

# numbers = pd.Series(the_list)

# # What is the data type of the numbers Series?
# print(numbers.dtype)
# print('\n')
# # How many elements are in the number Series?
# count = 0
# for i in numbers:
#     count += 1

# print('number of elements', count)
# print('\n')
# # Perform the necessary manipulations by accessing Series attributes and methods to convert the numbers Series to a numeric data type.
# new_list = []

# for i in numbers:
#     new_item = i
#     if '$' in i:
#         new_item = new_item.replace('$', '')
#     if ',' in new_item:
#         new_item = new_item.replace(',', '')
#     new_list.append(new_item)

# numbers = pd.Series(new_list)
# numbers = numbers.astype(float)
# print('the data type of numbers is', numbers.dtype)
        
        

# # Run the code to discover the maximum value from the Series.
# print('\n')
# print(numbers.max())
# # Run the code to discover the minimum value from the Series.
# print('\n')
# print(numbers.min())

# # What is the range of the values in the Series?
# print('\n')
# print(numbers.max() - numbers.min())

# # Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.
# print('\n')
# numbers_bins = pd.cut(numbers, 4)
# print(numbers_bins.value_counts())


# # Plot the binned data in a meaningful way. Be sure to include a title and axis labels.
# # numbers_bins.value_counts().plot()
# # plt.show()

# # Use pandas to create a Series named exam_scores from the following list:

the_list = [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
exam_scores = pd.Series(the_list)

print(exam_scores)

# How many elements are in the exam_scores Series?
print('\n')
print(exam_scores.count())
# Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.
print('\n')
print(exam_scores.describe())
# Plot the Series in a meaningful way and make sure your chart has a title and axis labels.

# ax = exam_scores.plot.bar(exam_scores, 100)
# ax.set_xlabel("Student number")
# ax.set_ylabel("Grade score")
# plt.show()


# Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades. 
# Add the necessary points to the highest grade to make it 100, 
# and add the same number of points to every other score in the Series as well.
the_new_list = []
print(exam_scores.max())
for i in exam_scores:
    the_new_list.append(i+4)

print(the_new_list)
exam_scores = pd.Series(the_new_list)

# ax = exam_scores.plot.bar(exam_scores, 100)
# ax.set_xlabel("Student number")
# ax.set_ylabel("Grade score")
# plt.show()

# Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of letter grades. For example, 86 should be a 'B' and 95 should  an 'A'. 
# Save this as a Series named letter_grades.be

s = pd.cut(exam_scores, bins=[0,59, 69, 79, 89, 100], labels=['F','D','C','B','A'])
print(s)




s2_bins2 = pd.cut(exam_scores, bins=[0,59, 69, 79, 89, 100], labels=['F','D','C','B','A'])
print(s2_bins2.value_counts())



# Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.

bx = s2_bins2.value_counts().plot(kind='bar', ylim=[0, 10])

bx.set_xlabel("Grade")
bx.set_ylabel("Number of grades")
plt.show()
