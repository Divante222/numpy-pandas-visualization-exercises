from pydataset import data

# Copy the code from the lesson to create a dataframe full of student grades.
import pandas as pd
import numpy as np

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

type(df)

# Create a column named passing_english that indicates whether each student has a passing grade in nglish.
# 
the_df = pd.DataFrame({'Students': students,'english_grades': english_grades})
the_df['passing_english'] = english_grades > 70
the_df['math_grades'] = math_grades
the_df['reading_grades'] = reading_grades

# Sort the english grades by the passing_english column. How are duplicates handled?

passed_english = the_df[the_df.passing_english]
passed_english = passed_english.sort_values(by='english_grades')


#duplicates are sorted by the index number

# Sort the english grades first by passing_english and then by student name. 

# All the students that are failing english should be first, 
# and within the students that are failing english they should be ordered alphabetically. 
# The same should be true for the students passing english. 
# (Hint: you can pass a list to the .sort_values method)

passing_eng = the_df
passing_eng = passing_eng.sort_values(by=['passing_english','Students'])



# Sort the english grades first by passing_english, and then by the actual english grade, 
# similar to how we did in the last step.
this_problem = the_df
this_problem = this_problem.sort_values(by=['passing_english', 'english_grades'])



# Calculate each students overall grade and add it as a column on the dataframe. 
# The overall grade is the average of the math, english, and reading grades.
this_problem = the_df
this_problem['overall_grade'] = round((this_problem.english_grades + this_problem.math_grades + this_problem.reading_grades) / 3, 2)


# Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:

from pydataset import data
mpg = data('mpg')
mpg.head()
# print(mpg)


# How many rows and columns are there?
# print(mpg.shape)
#234 rows #11 columns


# What are the data types of each column?
# print(mpg.info())


# Summarize the dataframe with .info and .describe
# print(mpg.describe())
# print(mpg.info())


# Rename the cty column to city.
# print(mpg)
the_answer = mpg.rename(columns= {'cty': 'city'})
# print(the_answer)


# Rename the hwy column to highway.
# print(mpg)
the_answer = mpg.rename(columns={'hwy':'highway'})
# print(the_answer)


# Do any cars have better city mileage than highway mileage?
# print(mpg)
# print((mpg.cty > mpg.hwy).value_counts())
# print(mpg[mpg.cty > mpg.hwy])
##there are no cars with better city mileage


# Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
the_answer = mpg
the_answer['mileage_difference'] = the_answer['hwy'] - the_answer['cty']
# print(the_answer)


# Which car (or cars) has the highest mileage difference?
the_answer = the_answer.sort_values(by='mileage_difference', ascending = False)
# print(the_answer.head(2))


# Which compact class car has the lowest highway mileage? The best?
the_answer = mpg
the_answer = the_answer.sort_values(by='hwy', ascending = True)
the_answer = the_answer[the_answer['class'] == 'compact'].head(1)
# print(the_answer)



# Create a column named average_mileage that is the mean of the city and highway mileage.
the_answer = mpg

the_answer['average_mileage'] = (the_answer.cty + the_answer.hwy) / 2
# print(the_answer.sort_values(by='average_mileage', ascending = False))



# Which dodge car has the best average mileage? The worst?
the_answer = the_answer[the_answer.manufacturer == 'dodge']
# the_answer = the_answer.sort_values(by='average_mileage', ascending =True)
# print(the_answer[the_answer.average_mileage == the_answer.average_mileage.min()])
# print()
# print(the_answer[the_answer.average_mileage == the_answer.average_mileage.max()])



# Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:
mammals = data('Mammals')
# print(mammals)



# How many rows and columns are there?
# print(mammals.shape)
##107 rows 4 columns




# What are the data types?
# print(mammals.info())



# # Summarize the dataframe with .info and .describe
# print(mammals.describe())
# print(mammals.info())




# What is the the weight of the fastest animal?
the_answer = mammals[mammals.speed == mammals.speed.max()]
print(the_answer.weight)





# What is the overal percentage of specials?
mammals = data('Mammals')
# print(mammals)
total_mamals = mammals.specials.count()

total_true = mammals[mammals.specials == True]
# print(round((total_true.specials.count() * 100) / total_mamals, 2), 'Percent')




# How many animals are hoppers that are above the median speed? What percentage is this?
the_answer = mammals[mammals.hoppers == True]
hoppers_above_mean_speed = the_answer[the_answer.speed > mammals.speed.mean()]

print(hoppers_above_mean_speed.hoppers.count(),'hoppers are above the average speed of animals')

print('the percnetage of hoppers that are faster than the average overall speed', round((hoppers_above_mean_speed.hoppers.count() * 100) / mammals.speed.count(), 2), 'percent')


