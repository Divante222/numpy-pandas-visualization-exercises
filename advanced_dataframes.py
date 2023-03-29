from env import username, hostname, password
import pandas as pd


def get_db_url(username, hostname, password, db_name):
    return f'mysql+pymysql://{username}:{password}@{hostname}/{db_name}'

db_name = 'employees'


url = get_db_url(username, hostname, password, db_name)
query = '''
select * from employees
limit 10;
'''
employees = pd.read_sql(query, url)



url = get_db_url(username, hostname, password, db_name)
query2 = '''
select * from titles
limit 10;
'''
titles = pd.read_sql(query2, url)




# print(employees.head())
# print(titles.head())


##this is what I expected because I put the limit on it
print(employees.shape)
print(titles.shape)



print(employees.describe())
print(titles.describe())
print()

print(pd.crosstab(titles.title, titles.title.count()))
print()

print(titles.to_date.min())
print()

print(titles.to_date.max())


print('hello world')
print(titles.groupby('title').agg('max'))
