#------------------------------------------------------------------------------------------------
# NUMPY ARRAY OPERATIONS 
# NUMPY ARITHEMETIC OPERATIONS 
#------------------------------------------------------------------------------------------------

#1. Array Addition 

import numpy as np 
sales_week1 = np.array([120, 150, 180, 200, 170])
sales_week2 = np.array([130, 160, 175, 210, 190])
print("Combined Sales:")
print(sales_week1 + sales_week2)

#------------------------------------------------------------------------------------------------

#2. Array Subtraction 

import numpy as np
sales_week1 = np.array([120, 150, 180, 200, 170])
sales_week2 = np.array([130, 160, 175, 210, 190])
print("Difference in Sales:")
print(sales_week2 - sales_week1)

#------------------------------------------------------------------------------------------------

#3. Scalar Multiplication 

# Assume the sales are expected to be double next month 
# find the projected sales by multiplying every value by 2

import numpy as np
sales = np.array([100, 200, 150, 300, 250])
print("Predicted Sales for next month:")
print(sales*2)

#-------------------------------------------------------------------------------------------------

#4. Scalar Addition

import numpy as np 
salary = np.array([25000, 30000, 35000, 40000])
print("Salary of employees after receiving their increment:")
print(salary + 5000)

#-------------------------------------------------------------------------------------------------

#5. Scalar Subtraction 

import numpy as np
expenses = np.array([5000, 7500, 6000, 9000, 4500])
print("Reducing every expenses by 1000:")
print(expenses - 1000)

#---------------------------------------------------------------------------------------------------

#6. Scalar Subtraction 

import numpy as np 
expenses = np.array([5000, 7500, 6000, 9000, 4500])
print("Reducing every expenses by 1000:")
print(expenses - 1000)

#---------------------------------------------------------------------------------------------------

#7. Scalar Division 

import numpy as np 
sales = np.array([1000, 2000, 3000, 4000])
avg_weekly_sales = sales // 4 
print("Average Weekly Sales :" , avg_weekly_sales , sep ="\n" )

#----------------------------------------------------------------------------------------------------

#8. Comparison Operation 

import numpy as np 
marks = np.array([45, 67, 32, 89, 56, 74])
mask = marks > 60
print(mask)
print(marks[mask])

#----------------------------------------------------------------------------------------------------

#9. Boolean Filtering 

import numpy as np 
greater_salaries = salary > 40000
print(greater_salaries)
print(salary[greater_salaries])

#----------------------------------------------------------------------------------------------------

#10. Boolean Filtering with range

import numpy as np 
temperatures = np.array([22,35,28,41,19,33,45,26,38,30])
print(temperatures[temperatures > 30])  #single condition(temperatures greater than 30)
print(temperatures[(temperatures>=25 ) & (temperatures<=35)])  #with range (Temperatures between 25 and 35)
print(temperatures[(temperatures > 40) | (temperatures < 20)]) #with range (Temperatures between 40 OR less than 20)
mask = temperatures > 40
print(mask)
print(temperatures[mask])
temperatures[mask] = 40   #replacing temperaatures greater than 40 with 40
print(temperatures[mask])
print(temperatures)

