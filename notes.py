import numpy as np

np.array([1,2,3,4,5])

my_array= np.array([1,2,3,4,5])



my_list = [1,2,3,4,5]

my_list[0]



list_of_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(list_of_list[0][1])

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

###access n.arrays differently

print(matrix[0,1])
print(matrix)

my_list[:]

print(matrix[1:])

print(list_of_list[1:])

mask = [False, True, False, True, False]

print(my_array[mask])


# my_list + 1 doesn't work
list_plus_one = []
for i in my_list:
    list_plus_one.append(i+1)
    
print(list_plus_one)


# my_array + 1 doesnt save

my_array = my_array +1
print(my_array)
my_array * 5

my_array % 2


my_array > 2
my_array[(my_array > 7) & (my_array < 10)] ##gets back the values in my array over 7
## can string together but needs to use &


my_array[my_array % 2 == 0]## all even numbers

my_array % 2

my_array[my_array % 2 == 1]

##look up bellcurve
a = np.random.randn(100)

import seaborn as sns
sns.distplot(a)##ask teacher about this

np.random.randn(3,3)

np.zeros((3,3))

np.ones((3,3))


data = 9
np.full((3,3), data)

np.arange(10) ## creates array zero to nine

np.arange(1, 10, 2)

np.arange(1,5,.5)

np.linspace(1, 4, 5)### used to split data into bins

my_array = np.array([1,2,3,4,5])

my_array.mean()
my_array.std()


matrix.mean()

# value_counts().sort_index() use this to sort index


#adding the h at the end of kind='barh' gives a horizontal chart

