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

#------------------------------------------------------------------------------------------------------------

#7. Array Reshaping

import numpy as np 
arr = np.array([54,74,85,25,36,45,96,69,])
print("Original Array:", arr)
print("Dimension of the Array:", arr.ndim)
print("Size of the given Array:", arr.size)
print("The given array can be reshaped as follows")
new_arr_1 = arr.reshape(2,4)
print("First Array : ", new_arr_1)
print("Dimension of the First Array:", new_arr_1.ndim)
print("Size of the First Array:", new_arr_1.size)
new_arr_2 = arr.reshape(4,2)
print("Second Array :", new_arr_2)
print("Dimension of the Second Array:", new_arr_2.ndim)
print("Size of the Second Array:", new_arr_2.size)

#------------------------------------------------------------------------------------------------------------

#8. Default Array Reshape

import numpy as np 
arr = np.arange(1,37)
print("\nOriginal Array\n " ,arr)
a = arr.reshape(12,-1) #Column assigned automatically
b = arr.reshape(-1, 3) #Row assigned automatically
c = arr.reshape(6,-1)  #Column assigned automatically
print("First reshaped array:\n",a)
print("Dimension:", a.ndim) #determining the dimension of the reshaped array
print("Shape:", a.shape) #determing the shape of the reshaped array
print("Size:",a.size)  #determining the size of the reshaped array 
print("Second reshaped array:\n",b)
print("Dimension:", b.ndim)
print("Shape:", b.shape)
print("Size:", b.size)
print("Third reshaped array:\n",c)
print("Dimension:", c.ndim)
print("Shape:", c.shape)
print("Size:", c.size)

