# Pandas Class
import pandas as pd 
import numpy as np


# Creating a series from a list
nums = [1, 2, 3, 4, 5, 6, 7]
# ps = pd.Series(nums)
# print("Here's a Pandas Series: ")
# print(ps)

# print(ps.size)
# print(ps.shape)

# ps= pd.Series(nums, index=["a", "b", "c", "d", "e", "f", "g"]) # Editing our index with letters
# print(ps)

# Accessing elements using index label (the one created)
# print(ps['c'])
# Accessing elements using integer location(the original index)
# print(ps[0:4])

# Operations on Pandas Series
# seriesmultiplication = ps * 2
# print(seriesmultiplication)

# series1 = pd.Series([1,2,3,4], index=[1,2,3,4])
# series2 = pd.Series([4,3,7,4], index=[1,2,3,4])
# print(series1 + series2)

series3 = pd.Series([2,3,4,5,np.nan,23,5,78,np.nan,4], index=['a','b','c','d','e','f','g','h','i','j'])
# print(series3)
# print(series3.info())
# print(series3.isnull())
# print(series3.fillna(0))
# print(series3.dropna())

# Convert series to list
# list_series = series3.to_list()
# print(list_series)

# Convert series to dict
# dict_series = series3.to_dict()
# print(dict_series)

# # Creating a dataframe
# data = {'Name': ['John', 'Anna', 'Peter'], 
#         'Age': [28, 23, 56],
#         'Occupation': ['Engineer', 'Artist', 'Writer']}
# df = pd.DataFrame(data, index= ['a','b', 'c'])
# print(df)
# print(df.shape)
# print(df.columns)
# print(df.index)
# print(df.dtypes)
# print(df.ndim)
# print(df.values)

index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
students = {'Name': ['Caleb', 'Amara', 'Destiny', 'Nonye', 'Uzo', 'Cyril', 'Amaka', 'Loveth', 'Allwell', 'Emeka'],
            'Age': [23, 19, 18, 22, 21, 26, 20, 22, 19, 21],
            'Gender':['M', 'F', 'M', 'F', 'M', 'M', 'F', 'F', 'M', 'M'],
            'Level': [100, 100, 200, 400, 300, 400, 500, 300, 100, 200],
            'Departments': ['Microbiology', 'Physics', 'Dentistry', 'Anatomy', 'Medicine', 'Computer Science', 'Geology', 'Soil Science', 'Economics', 'Agriculture']
            }
# stud_index = pd.DataFrame(students, index = index)
# print(stud_index.head(7))
# print(stud_index.info())
# print(stud_index.tail())
# print(stud_index.columns)

df = pd.read_csv("RewardsData.csv")
# print(df.columns[2])
# print(df.loc[1:3])
# pd.options.display.max_rows = 85
# print(pd.options.display.max_rows)
# print(df.head(15))
# print(df.info())
# print(df.isnull().sum())