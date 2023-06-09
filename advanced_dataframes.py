from env import username, hostname, password
import pandas as pd
import numpy as np
from pydataset import data

# Run python -m pip install pymysql from your terminal to install the mysql client (any folder is fine)
# cd into your exercises folder for this module and run echo env.py >> .gitignore
# Create a function named get_db_url. It should accept a username, hostname, password, and database name and return a url connection string formatted like in the example at the start of this lesson.

# Use your function to obtain a connection to the employees database.
# def get_db_url(username, hostname, password, db_name):
#     return f'mysql+pymysql://{username}:{password}@{hostname}/{db_name}'

# db_name = 'employees'






# Once you have successfully run a query:
# url = get_db_url(username, hostname, password, db_name)
# query = '''
# select * from employees
# ;
# '''
# employees = pd.read_sql(query, url)



# url = get_db_url(username, hostname, password, db_name)
# query2 = '''
# select * from titles
# ;
# '''
# titles = pd.read_sql(query2, url)







# a. Intentionally make a typo in the database url. What kind of error message do you see?

# db_name = 'emploees'






# b. Intentionally make an error in your SQL query. What does the error message look like?

# url = get_db_url(username, hostname, password, db_name)
# query2 = '''
# select  rom titles
# ;
# '''
# titles = pd.read_sql(query2, url)







# Read the employees and titles tables into two separate DataFrames.
# titles = pd.read_sql(query2, url)
# employees = pd.read_sql(query, url)





# How many rows and columns do you have in each DataFrame? Is that what you expected?
# print(employees.shape)
# print(titles.shape)




# Display the summary statistics for each DataFrame.
# print(employees.describe())
# print(titles.describe())



# How many unique titles are in the titles DataFrame?
# print(titles.title.nunique())



# What is the oldest date in the to_date column?
# print(titles.to_date.min())
# print()



# What is the most recent date in the to_date column?
# print(titles.to_date.max())

# print(titles[titles.to_date != titles.to_date.max()].max())

# # print(employees.head())
# # print(titles.head())

# ##this is what I expected because I put the limit on it

# print()

# print(pd.crosstab(titles.title, titles.title.count()))
# print()

# print('hello world')
# print(titles.groupby('title').agg('max'))

# 








###################################################################

# Copy the users and roles DataFrames from the examples above.

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})


users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})


# What is the result of using a right join on the DataFrames?
# print(pd.merge(roles, users, how='right'))


# # What is the result of using an outer join on the DataFrames?
# print(pd.merge(roles,users,how='outer'))  


# # What happens if you drop the foreign keys from the DataFrames and try to merge them?
# users = pd.DataFrame({
    
#     'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
#     'role_id': [1, 2, 3, 3, np.nan, np.nan]
# })
# print()
# print(pd.merge(roles, users, how='inner'))


# # Load the mpg dataset from PyDataset.
# mpg = data('mpg')



# Output and read the documentation for the mpg dataset.
# mpg = data('mpg', show_doc=True) 
# print(help(mpg))


# How many rows and columns are in the dataset?
# print(mpg.shape)
# 234 rows, 11 columns


# Check out your column names and perform any cleanup you may want on them.
# mpg = mpg.rename(columns ={'cyl':'cylender', 'drv':'Driver', 'cty':'city', 'trans':'transmission', 'cty':'city', 'hwy':'highway'})
# print(mpg)



# Display the summary statistics for the dataset.
# print(mpg.describe())


# # How many different manufacturers are there?
# print('the number of manufacturers:', len(mpg.groupby('manufacturer').agg('count')))
# print(mpg.groupby('manufacturer').agg('count'))


# # How many different models are there?
# # print(mpg.groupby('model').count())
# print('\n\n\n')
# print('the number of models:', len(mpg.groupby('model').count()))
# print('\n\n\n')

# # Create a column named mileage_difference like you did in the DataFrames exercises; this column should contain the difference between highway and city mileage for each car.
# mpg['mileage_difference'] = mpg.hwy - mpg.cty



# # Create a column named average_mileage like you did in the DataFrames exercises; this is the mean of the city and highway mileage.
# mpg['average_mileage'] = (mpg.cty + mpg.hwy) / 2



# # Create a new column on the mpg dataset named is_automatic that holds boolean values denoting whether the car has an automatic transmission.
# mpg['is_automatic'] = np.where(mpg.trans.str.contains('auto') , True, False)


    

# # Using the mpg dataset, find out which which manufacturer has the best miles per gallon on average?
# the_answer = mpg.groupby('manufacturer').agg('mean')
# the_answer = the_answer.sort_values(by='average_mileage', ascending=False)
# print(the_answer[['average_mileage']].round(2))



# ===================================================================
# Do automatic or manual cars have better miles per gallon?
# the_auto_mpg = mpg[mpg.trans.str.contains('auto')]

# the_manual_mpg = mpg[mpg.trans.str.contains('manual')]

# the_auto_mpg = the_auto_mpg.sort_values(by='average_mileage', ascending=False)
# print(the_auto_mpg.head())
# print('\n\n\n')
# the_manual_mpg = the_manual_mpg.sort_values(by='average_mileage', ascending=False)
# print(the_manual_mpg.head())
# print('\n\n\n')
# the_answer = mpg.groupby('is_automatic').agg('mean')
# the_answer = the_answer.sort_values(by='average_mileage', ascending = False)
# print(the_answer['average_mileage'].round(2))


# print(mpg.describe(include='all'))


# ===================================================================# ===================================================================# ===================================================================
# Use your get_db_url function to help you explore the data from the chipotle database.


def get_db_url(username, hostname, password, db_name):
    return f'mysql+pymysql://{username}:{password}@{hostname}/{db_name}'

db_name = 'chipotle'
url = get_db_url(username, hostname, password, db_name)

query = '''
select * from orders;
'''









# # What is the total price for each order?
# titles = pd.read_sql(query, url)
# titles['item_price'] = titles.item_price.str.replace('$','')
# titles.item_price = titles.item_price.astype(float)
# print(titles.groupby('order_id').agg('sum'))

# print('\n\n\n')

# # What are the most popular 3 items?
# titles = pd.read_sql(query, url)
# the_answer = titles.groupby(by='item_name').agg('sum')
# print(the_answer.sort_values('quantity', ascending=False).head(3))



# # print(titles.item_name.value_counts().head(3))


# print('\n\n\n')

# # Which item has produced the most revenue?
# titles = pd.read_sql(query, url)
# titles['item_price'] = titles.item_price.str.replace('$','')
# titles.item_price = titles.item_price.astype(float)
# the_answer = titles.groupby('item_name').agg('sum')

# print(the_answer.sort_values(by='item_price', ascending=False).head(1))


# print('\n\n\n')


# # Join the employees and titles DataFrames together.

# db_name = 'employees'
# url = get_db_url(username, hostname, password, db_name)
# query = '''
# select * from employees
# join titles using(emp_no)
# limit 20
# ;
# '''
# employees = pd.read_sql(query, url)



# print(employees)


# print('\n\n\n')



# # For each title, find the hire date of the employee that was hired most recently with that title.

# print(employees.groupby('title')['hire_date'].agg('max'))


# print('\n\n\n')
# print('hello')

# Write the code necessary to create a cross tabulation of the number of titles by department. 
# (Hint: this will involve a combination of SQL code to pull the necessary data and python/pandas code to perform the manipulations.)

db_name = 'employees'
url = get_db_url(username, hostname, password, db_name)

query = '''
select * from employees
join titles using(emp_no)
join dept_emp using(emp_no)
join departments using(dept_no)
where (employees.emp_no, titles.from_date) in (select employees.emp_no, max(titles.from_date) from employees
							join titles using(emp_no)
							join dept_emp using(emp_no)
							join departments using(dept_no)
							group by employees.emp_no)
limit 20

; 
'''
print('\n\n\n')
employees = pd.read_sql(query, url)
# print(employees)


print(pd.crosstab(employees.dept_name, employees.title))
# print()

