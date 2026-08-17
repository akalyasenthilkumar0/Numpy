#1. Array Creation 

import numpy as np 
arr = np.array([12, 32, 42])
print(arr)


#2. Create an array with 5 zeros

import numpy as np
z_1 = np.zeros(5)
print(z)

z_2 = np.zeros(5, dtype=int)
print("Here the data type is specified as an integer type.")
print(z_2)

#3. Create an array with 7 ones 

import numpy as np 
arr = np.ones(7)
print("Array wiht all ones:", arr , end = "\n")

#4. Create a 3*4 matrix that contains all ones

import numpy as np 
a = np.ones((3,4), dtype = int)
print(a)

#5. Create a 5*5 matrix which contains all zeros

import numpy as np 
arr = np.zeros((5,5), dtype = int)
print(arr)

#6. Create a 2*3 matrix where 100 is the only value

import numpy as np 
matrix_2_3 = np.full((2,3),100)
print("Matrix where every value is 100:")
print(matrix_2_3)

#7. Create a 1D array with values as first 10 multiples of 1000 starting from 1000

import numpy as np 
arr = np.arange(1000,11000,1000)
print("First 10 multiples of 1000:")
print(arr)

#8. Create an array where you need exactly 5 equally spaced values from 0 to 20 

import numpy as np 
a_p = np.linspace(0,20,5)
print("Equally sapced Values:")
print(a_p)

#9. Feature matrix representing 100 samples with 5 numerical features

import numpy as np 
samples = np.zeros((100,5),dtype = int)
print("Random samples of size 100 with 5 features:", samples, sep = " \n ")

#10. Constant feature matrix with 20*4 matrix along with the value 50

import numpy as np 
matrix = np.full((20,4),50)
print("Constant Feature Matrix:" , matrix)

#11. Synthetic ML dataset - contains of Sample IDs, equally spaced values, feature matrix, and target representation

import numpy as np 

#Creating 10 sample IDs
id = np.arange(1,11,1)

#Creating 10 equally spaced values between 0 and 1
values = np.linspace(0,1,10)

#Creating a 10*2 feature matrix with zeros as initial values
fea_mat = np.zeros((10,2), dtype = int)

#Creating a 10*1 ones matrix as an initial target representation
tar_mat = np.ones(10,dtype = int)
