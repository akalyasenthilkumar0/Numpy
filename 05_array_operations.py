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

#10. Boolean Filtering with Range(AND, OR) and Value Replacement 

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

#-----------------------------------------------------------------------------------------------------

#11. Arithemetic and Boolean Filtering

import numpy as np
sales = np.array([100, 200, 300, 400, 500])
new_sales = sales * 1.10            #100% original + 10% increase = 110%   #110 / 100 = 1.10
print("Original Sales:", sales)
print("Sales after 10% increase:", new_sales)

#-----------------------------------------------------------------------------------------------------

#12. Product Price Analysis with Percentage Discount

import numpy as np
prices = np.array([1000, 1500, 2000, 2500, 3000])
discount = 20 / 100
final_prices = prices * (1 - discount)
print("Original Prices:", prices)
print("Final Prices after 20% discount:", final_prices)

#----------------------------------------------------------------------------------------------------

#13. Array aggregation 

import numpy as np
sales = np.array([120, 150, 180, 200, 170])
print("Total Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))
print("Minimum Sales:", np.min(sales))
print("Maximum Sales:", np.max(sales))

#----------------------------------------------------------------------------------------------------

#14. Array Aggregatio in 2D array 

import numpy as np
marks = np.array([
    [80, 75, 90],
    [60, 85, 70],
    [95, 88, 92]
])
print("Total Marks:", np.sum(marks))
print("Average Marks:", np.mean(marks))
print("Highest Mark:", np.max(marks))
print("Lowest Mark:", np.min(marks))

#---------------------------------------------------------------------------------------------------

#15. Row-wise and Column-wise Aggregation  

import numpy as np

# Each row represents a student ; axis=1 
# Each column represents a subject ; axis=0

marks = np.array([
    [80, 75, 90],
    [60, 85, 70],
    [95, 88, 92]
])

# 1. Total marks of each student
student_total = np.sum(marks, axis=1)
print("Total marks of each student:", student_total)

# 2. Average marks of each student
student_average = np.mean(marks, axis=1)
print("Average marks of each student:", student_average)

# 3. Total marks in each subject
subject_total = np.sum(marks, axis=0)
print("Total marks in each subject:", subject_total)

# 4. Average marks in each subject
subject_average = np.mean(marks, axis=0)
print("Average marks in each subject:", subject_average)

#--------------------------------------------------------------------------------------------------

#16. Finding the Highest and lowest positions 

import numpy as np
marks = np.array([65, 82, 45, 91, 73])
print("Lowest Mark:", np.mix(marks))
print("Position of the lowst mark:",np.argmix(marks))
print("Highest Mark:", np.max(marks))
print("Position of the Highest mark:", np.argmax(marks))

#--------------------------------------------------------------------------------------------------

#17. Sorting

import numpy as np
marks = np.array([65, 82, 45, 91, 73])
sorted_marks = np.sort(marks)
print("Sorted Marks:", sorted_marks)

#--------------------------------------------------------------------------------------------------

#18. Array Statistics and Condition 

import numpy as np
sales = np.array([120, 180, 150, 220, 90, 300, 170, 250])
avg = np.mean(sales)
final_sales = sales[sales > avg] 
print(final_sales)

#--------------------------------------------------------------------------------------------------
