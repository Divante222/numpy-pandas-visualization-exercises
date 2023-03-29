import pandas as pd
import numpy as np

ls = [1,34,23,-1]

df = pd.DataFrame(ls)

print(df)

matrix = [[1,2,3],[2,3,45],[435,12,333]]

df = pd.DataFrame(matrix)

print(df)

column_names = ['first','second','third']

df = pd.DataFrame(matrix, columns=column_names)

print(df)

matrix_array = np.array(matrix)

print(matrix_array)

df = pd.DataFrame(matrix_array)

print(df)

new_dt = {'A':[1,2,3], 'B':[4,5,6]}

df = pd.DataFrame(new_dt)

print(df)

the_number = np.random.randint(low=60,high=100, size=len(new_dt))

print(the_number)

the_choice = np.random.choice(['a','b'], len(new_dt))

print(the_choice)
print(type(the_choice))