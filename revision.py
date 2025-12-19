# # x = 25
# # def func1():
# #     global x
# #     x = 5
# #     print(x)
# # func1()
# # print(x)

# # x = 'Hello, World' 
# # print(x.replace("World", "Chinonye"))

# # string1 = input("Enter your name: ")
# # string2 = int(input("enter your age: "))
# # print(f"I am {string1} and I am {string2} years old")

# # x = 5
# # x &= 3
# # print(x)

# # locations = ['Bali','Auckland','Sydney','Bangkok','Tokyo']

# # location = 0
# # #Add any new code below this line
# # while True:
# #   for location in locations:
# #     print(location)
# #     location += 1

# # a = 456
# # b = 459
# # #print(a == b)
# # a = b
# # print(a is b)
# # print(a == b)

# # def calc_power(a, b):
# #     return a ** b
# # base = input("Enter the number for the base: ")
# # exponent = input("Enter the number for the exponent: ")
# # result = calc_power(base, exponent)
# # print("The result is " + result)

# # a = [1, 2, 3 ,4, 5]
# # b = [1, 2, 3, 4, 5]
# # a =b
# # print(a is b)
# # print(a == b)

# a = ('b', 'A', 'C', 'a')
# # a.sort(reverse=True)
# # print(a)

# # import random

# # mylist = ["apple", "banana", "cherry"]

# # print(random.choices(mylist, weights = [2, 1, 1], k = 12))
# # b = slice(1, 8, 5)
# # print(a[b])

# # Question 1
# # Create a Pandas Series from a list of temperatures: 22, 25, 30, 28, 35, 32, 33 
# # and label the indexes as Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday and specify the data type to be float32.
# # Display the series.

# import pandas as pd
# import numpy as np

# temp_list = [22, 25, 30, 28, 35, 32, 33]
# idx_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# temp_list_series = pd.Series(temp_list, idx_list)
# # print(temp_list_series)

# # Question 2
# # Construct a Pandas Series with 20 numbers from 100 to 150 and create an index from 1- 20 using the np.arange function. 
# # Specify the data type to be of float64.
# series_num = np.random.randint(100, 150, size= 20)
# indx_series = np.arange(1, 21, 1)
# series_pan = pd.Series(data= series_num, index= indx_series, dtype= 'float64')
# # print(series_pan)

# # Question 3
# # Create a pandas DataFrame with 10 rows with the following columns:
# # - Name (random names with your name being the first)
# # - State
# # - Age
# # - Weight (in kg)
# # - Gender

# data = {'Name': ['Isiguzoro Celine', 'Excel Nwachukwu', 'Uche Ohajuru', 'Ehiemere Cyril', 'Ikpeka Peace', 'Uzoma Johnson', 'Orji Anthony', 'Uzuka Henry', 'Emeka Ibekwe', 'Chukwuma Jane'],
#         'State': ['Abia', 'Imo', 'Abia', 'Imo', 'Enugu', 'Lagos', 'Anambra', 'Kebbi', 'Damaturu', 'Lagos'],
#         'Age': [24, 27, 35, 28, 26, 50, 34, 30, 33, 25 ],
#         'Weight': [51.5, 71, 60, 77, 85, 76, 68, 77, 100, 44],
#         'Gender': ['Female', 'Male', 'Male', 'Male', 'Female', 'Male', 'Male', 'Male', 'Male', 'Female']
# }
# data_df = pd.DataFrame(data= data, index=[1,2,3,4,5,6,7,8,9,10])
# # print(data_df)

# # Question 4
# # For the above DataFrame, write code to print its shape, columns, and the data type of each column.
# print(f"The shape of this dataframe is {data_df.shape}\n") # To get the shape of the dataframe
# print(f"The columns of the dataframe: \n {data_df.columns}\n")
# print(f"The datatypes of these columns are: \n {data_df.dtypes}")

# # Question 5
# # Add a new column occupation to the DataFrame you created.
# occupation = ['Software Engineer', 'Marketing Manager', 'Accountant', 'Sales Rep', 'Student', 'Doctor', 'Journalist', 'Consultant', 'Architect', 'Teacher']
# data_df['occupation'] = occupation
# # print(data_df.columns)

# # Question 6
# # Create two Series, A and B, containing the numbers 1 - 5 and 6 - 10 respectively. Compute the sum, difference (B-A), and product of A and B
# seriesA = [1, 2, 3, 4, 5]
# seriesB = [6, 7, 8, 9, 10]
# pd_seriesA = pd.Series(seriesA)
# pd_seriesB = pd.Series(seriesB)
# print(f"The sum of series is {pd_seriesA} + {pd_seriesB}\n")
# print(f"The difference of both series is {pd_seriesB} - {pd_seriesA}\n")
# print(f"The product of the series is {pd_seriesA} * {pd_seriesB}")

import keyword
print(keyword.kwlist)