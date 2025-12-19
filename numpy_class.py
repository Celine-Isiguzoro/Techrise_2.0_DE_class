# """Numpy = Numerical Python"""

import numpy as np
# list1 = [1,2,3,4,5]
# # print(type(list1))

# # # Creating NumPy arrays
# array1 = np.array([list1]) # Convert python list to NumPy array and it is a one-dimensional array
# array2 = np.zeros((3,3)) # An array filled with zeros
# array3 = np.ones((2,4)) # An array filled with ones(1s)
# array4 = np.arange(0, 11, 2)# Create an array with values from 0 to 10 exclusive with step 2
# array5 = np.linspace(0, 2, 5) # an array with 5 evenly spaced numbers between 0 and 1
# print(array5)
# #print(array2)ay4.ndim)

# array6 = np.array([[[5, 8, 13, 15, 2],
#                     [2, 4, 6,8, 10],
#                     [2, 4, 6,8, 10]],

#                     [[5, 8, 13, 15, 2],
#                     [2, 4, 6,8, 10],
#                     [2, 4, 6,8, 10]],
                    
#                     [[5, 8, 13, 15, 2],
#                     [2, 4, 6,8, 10],
#                     [2, 4, 6,8, 10]],

#                     [[5, 8, 13, 15, 2],
#                     [2, 4, 6,8, 10],
#                     [2, 4, 6,8, 10]]])
# # attributes of arrays
# print(array6)
# print(array6.ndim)
# print(array6.shape)
# print(array6.size)

# array_1d = np.array([2,3,4,5,6,4,5])
# print(array_1d[1:5])

# array_2d = np.array([[3,4,5,3,2], #index 0
#                     [2,8,9,4,2], # index 1
#                     [8,6,4,3,2], # index 2
#                     [4,4,3,2,6]]) # index 3

# print(array_2d[0:,1:9]) #row and column

# array_3d = np.array([[[5, 8, 13, 15, 2],
#                     [2, 4, 6,8, 10],
#                     [2, 4, 6,8, 10]],

#                     [[5, 8, 13, 15, 2],
#                     [2, 4, 6,8, 10],
#                     [2, 4, 6,8, 10]],
                    
#                     [[5, 8, 13, 15, 2],
#                     [2, 4, 6,8, 10],
#                     [2, 4, 6,8, 10]],

#                     [[5, 8, 13, 15, 2],
#                     [2, 4, 6,8, 10],
#                     [2, 4, 6,8, 10]]])
# print(array_3d[:,:,-1]) #stack, row, column

# Arithmetic Equations
# array1 = np.array([2,3,4,5])
# array2 = np.array([4,5,6,7])
# add_array = array1 * array2 # Element wise operations
# subtract_array = array2 - array1
# print(subtract_array) 

# Using ufuncs to perform element wise operations
# print(np.add(array1, array2))
# print(np.subtract(array2, array1))
# print(np.mod(array2, array1))
# print(np.floor_divide(array2, array1))
# print(np.divide(array2, array1))
# print(np.multiply(array1, array2))

# BroadCasting in NumPy
# array1 = np.array([2,3,4,5])
# num = np.array([4]) # Scaler
# print(array1 + num)

# array1 = np.array([[[5, 8, 13, 15, 2],
#                     [2, 4, 6,8, 10]],

#                     [[5, 8, 13, 15, 2],
#                     [2, 4, 6,8, 10]]])
# array_2 = np.array([[5, 8, 13, 15, 2],
#                     [2, 4, 6,8, 10]])
# print(array1 + array_2)
# for i in  array1:
#     for j in array_2:
#         add = i + j
#         print(add)

# ARRAY MANIPULATION
# array1 = np.array([[5, 0, 13, 15],
#                   [2, 4, 6, 9]])
# print(np.reshape(array1, (4, 3))) #must be within the size 8 elements
# print(np.resize(array1, (3, 2))) # will resize to fit in the 8 in 12

# FLATTENING OF ARRAYS
# print(array1.flatten()) # Flattens to one dimension
# print(array1.ravel()) # Same as flatten

# ARRAY TRANSPOSE
# print(array1.transpose())
# print(array1.T)

# CONCATENATION OF ARRAYS
# array2 = np.array([[5, 0, 13, 15],
#                   [2, 4, 6, 9]])
# array3 = np.array([[5, 8, 4, 17],
#                   [7, 4, 1, 8]])
# array4 = np.concatenate((array2, array3), axis = 1)
# print(array4)
                    