#-----------------------------------------------------------------------------------------------------------------
# ARRAY ATTRIBUTES
#-----------------------------------------------------------------------------------------------------------------

#1. 1D Array with verfication that is 1D array 
# ndim is used 

import numpy as np
arr = np.array([23,46,69,92,125,89,76,54,110,99])
print("Array:", arr)
print("Number of Dimensions:", arr.ndim)

#-----------------------------------------------------------------------------------------------------------------

#2. 2D Array and shape attribute is used to find its dimenisons

import numpy as np 
b = np.array([[44,67,89,23],[11,54,77,99]])
print("Array:", b)
print("Rows and Columns:" , b.shape)

#----------------------------------------------------------------------------------------------------------------

#3. Create a matrix of 5*8 with values zeros and compute it's dimension and shape

import numpy as np 
arr = np.zeros((5,8), dtype = int )
print(arr)
print("It is a", arr.ndim , "dimensional array")
print("Rows and Columns:", arr.shape)

#----------------------------------------------------------------------------------------------------------------

#4. Finding the number of bytes 

import numpy as np
a = np.array([45,89,67])
print(a)
print("Bytes occupied by each element:", a.itemsize)

#----------------------------------------------------------------------------------------------------------------

#5. Finding  the bytes of an array created with random size and values

import numpy as np 
arr = np.array([10,20,30,40,50,60,70,80,90,100])
print(arr)
print("Type of Array is ", arr.dtype)
print("Dimension : ", arr.ndim)
print("Shape of the given array : ", arr.shape)
print("Size of array : ", arr.size)
print("Number of bytes occupied by each element in the array : ", arr.itemsize)
print("Total bytes occupied by the array:", arr.nbytes)

#----------------------------------------------------------------------------------------------------------------

#6. Array Inspection 

import numpy as np 
arr = np.full((6,4),25)
print(arr)
print("Type of the Array is " , arr.dtype)
print("Dimension : ", arr.ndim)
print("Rows and Columns : ", arr.shape)
print("Size of the", arr.shape ,"array : ", arr.size)
print("Bytes occupied by each element : ", arr.itemsize)
print("Total number of bytes occupied by the array : ", arr.nbytes)

