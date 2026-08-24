#------------------------------------------------------------------------------------------------
#4. Array Indexing and Slicing 
#------------------------------------------------------------------------------------------------

#1. Indexing in 1D array

import numpy as np 
arr = np.array([15, 25, 35, 45, 55, 65])
print(arr[0]) #Extracting the first element 
print(arr[2]) #Extracting the third element 
print(arr[-1]) #Extracting the last element of the array

#-------------------------------------------------------------------------------------------------

#2. Negative Indexing 

import numpy as np 
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[-1]) #Accessing the last element
print(arr[-2]) #Accessing the second last element
print(arr[-4]) #Accessing the fourth last element 

#--------------------------------------------------------------------------------------------------

#3. 2D Array Indexing

import numpy as np 
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(arr[1,1]) #Accessing the element 50
print(arr[2,2]) #Accessing the element 90
print(arr[0,1]) #Accessing the element 20

#-----------------------------------------------------------------------------------------------------

#4. Array Slicing 

import numpy as np
arr = np.array([
    [10, 20, 30, 40, 50],
    [60, 70, 80, 90, 100],
    [110, 120, 130, 140, 150],
    [160, 170, 180, 190, 200]
])
print(arr[1:3, 2:5])

#-----------------------------------------------------------------------------------------------------

#5. Row and Column Selection Indexing

import numpy as np 
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print("Third Row:", arr[2]) #Third Row
print("Second Row:", arr[1]) #Second Row
print("Specified Rows and Columns:" , arr[:,0])

#----------------------------------------------------------------------------------------------------

#6. 1D Slicing 

import numpy as np 
a = np.array([11,22,33,44,55,66,77])
print(arr[2:5])

#----------------------------------------------------------------------------------------------------

#7. 2D Slicing 

import numpy as np 
arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])
print([0:2])
print([0:2,2:4])

#---------------------------------------------------------------------------------------------------

#8. Step Slicing 

import numpy as np 
a = np.arraay([45,25,35,15,85,75,65])
print([1:5:2])

#--------------------------------------------------------------------------------------------------

#9. Reverse Slicing

import numpy as np 
a = np.array([10,20,30,40,50,60])
print(a[:: -1] )

#---------------------------------------------------------------------------------------------------

#10. DataSet Row & Column Extraction

import numpy as np
#Each column represents
#Student_ID | Age | Attendance | Study_Hours
data = np.array([
    [101, 25, 80, 7],
    [102, 30, 75, 6],
    [103, 22, 90, 8],
    [104, 28, 85, 9],
    [105, 35, 70, 5]
])

#a. Extracting all the Students id 
print("Students id:" , data[:,0]) 

#b. all study hours
print("Study Hours of Students:", data[:,3])

#c. Complete data of first 3 students
print("Data of first three Students:", data[0:3])

#d. Age and Attendence of all the Students
print("Age and Attendance of all:", data[:,1:3])

#----------------------------------------------------------------------------------------------------
