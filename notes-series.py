import pandas as pd
import numpy as np
from pydataset import data


##pd.set_option('display.max_rows', 1000) ##set max number of columns

my_list = [2,3,4]
type(my_list)

my_array = np.array(my_list)

my_series = pd.Series(my_list)

print(my_series)

my_series = pd.Series(my_array)

print(my_series)



my_df = data('sleepstudy')

print(data())
print()
print(my_df)

print(my_df.columns) ##check the column names to have exact spelling

print(my_df.Reaction) ## get the column reaction and all its numbers

print(data().head(25)) ## chose the first 25 ids

print(my_df[['Reaction']])

print(my_df.Reaction.head(5))

print(my_df.Reaction.tail(5)) ## get the ending

print(my_df[['Reaction','Days']]) ## get multiple columns


##series datatype 

print()

print(pd.Series([True, False, True]))

print(pd.Series(['Codeup', 'is', 'awsome!']))

print(pd.Series(['5', 1, 4]))

a = pd.Series(['5', 1, 4])

print(a)

my_new_series = a[a != '5']

print(my_new_series)

print(my_new_series.astype('int'))

print(my_new_series + 1)

print(my_df.Subject.astype('str'))

s1 = pd.Series([2,3,4,6])

print(s1)

print(s1 / 2) ## changes datatype to float

print(s1 >= 5)

print(s1[s1 >5])

s1 = pd.Series([1,3,6,3,4,7,4,2])

print(s1.head(2))

print(s1.tail(3))

print(my_df.head(5))

s3 = my_df

print(s3.value_counts())

print(my_df[my_df['Subject'] == 308]) 

print((s3 > 5).any()) ##if it contains at least one in dataset

print((s3 > 5).all())


letters = list('abcdefghijklmnopqrstuvwxyz')
vowels = list('aeiou')


letters_series = pd.Series(letters)

letters_series.isin(vowels)
print()
print(letters_series.isin(vowels).value_counts())
print()
letters_series.isin(vowels).all()

letters_series.isin(vowels).any()

print(my_df.Subject.value_counts())


## methods for descriptive statistics
s2 = my_df.Reaction
print()
print(s2.count())
print()


a = {
    "count":s2.count(),
    "sum":s2.sum(),
    "mean":s2.mean(),
    "median":s2.median()
}

print(s2.describe()) ### gives all the basic information

print(my_df.columns)


def even_or_odd(n):
    if n%2 == 0:
        return'even'
    else:
        return 'odd'
        second(n)
    
print(s1.apply(even_or_odd))




print(s1.apply(lambda n: 'even' if n % 2 == 0 else 'odd'))

# vectorized string operations


s4 = pd.Series(['Andrew', 'keila', 'Brian', 'Manuel', 'Corey'])

print(s4)
print(s4.str.lower()) ## have to use str 

print(s4.str.upper())

print(s4.str.replace('Andrew', 'Instructor'))

print(s1.index)

print(s1.dtype)

print(s1.size)

print(s1.shape)

print(s1.values)
