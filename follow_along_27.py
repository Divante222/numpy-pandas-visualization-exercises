import numpy as np
import pandas as pd
from pydataset import data
import matplotlib.pyplot as plt
my_df = data('sleepstudy')


print(my_df.head())

s2 = my_df.Reaction

print(s2.head())

print(s2[1])

print(my_df)

print(my_df["Reaction"][1])

print(round(my_df.Reaction[3],2))

print(s2.describe().index)

print(s2.describe()['count'])

print(s2.describe()['75%'])

print(s2)

q3 = s2.describe()['75%']

print(s2 > q3)

print(s2[s2 > q3])

s2_desc = s2.describe()

print(s2_desc['count': 'std'])

print(s2_desc[2:5])

print(s2.apply(lambda n: 'q4' if n > q3 else 'q1-q3'))

ds_team_series = pd.Series(['Adam', 'Adam', 'amanda'])

ds_team_series.str.startswith('A') #can be used as a mask prints true false list

print(ds_team_series[ds_team_series.str.startswith('A')])

s2_minutes = s2/60

print(s2_minutes)
s2_bins = pd.cut(s2_minutes, 6)
print(s2_bins)

print(s2_bins.value_counts())

s2_minutes.min()
s2_minutes.max()

s2_bins2 = pd.cut(s2_minutes, [3,4,5,6,7,8])
### we do bins for plotting
print(s2_bins2)

print(s2_bins2.value_counts())

plt.hist(s2_minutes)
# plt.show()

s2_bins = pd.cut(s2_minutes, 10)
s2_bins_value_counts = s2_bins.value_counts(sort= False)

# print(s2_bins_value_counts)
# s2_bins_value_counts.plot()
plt.show()
