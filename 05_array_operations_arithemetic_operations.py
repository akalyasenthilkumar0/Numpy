#------------------------------------------------------------------------------------------------
# NUMPY ARRAY OPERATIONS 
# NUMPY ARITHEMETIC OPERATIONS 
#------------------------------------------------------------------------------------------------

#1. Array Addition 

sales_week1 = np.array([120, 150, 180, 200, 170])
sales_week2 = np.array([130, 160, 175, 210, 190])
print("Combined Sales:")
print(sales_week1 + sales_week2)

#------------------------------------------------------------------------------------------------

#2. Array Subtraction 

sales_week1 = np.array([120, 150, 180, 200, 170])
sales_week2 = np.array([130, 160, 175, 210, 190])
print("Difference in Sales:")
print(sales_week2 - sales_week1)

#------------------------------------------------------------------------------------------------

#3. Scalar Multiplication 

# Assume the sales are expected to be double next month 
# find the projected sales by multiplying every value by 2

sales = np.array([100, 200, 150, 300, 250])
print("Predicted Sales for next month:")
print(sales*2)

#-------------------------------------------------------------------------------------------------

#4. Scalar Addition

salary = np.array([25000, 30000, 35000, 40000])
print("Salary of employees after receiving their increment:")
print(salary + 5000)

#-------------------------------------------------------------------------------------------------

#5. Scalar Subtraction 

expenses = np.array([5000, 7500, 6000, 9000, 4500])
print("Reducing every expenses by 1000:")
print(expenses - 1000)

#---------------------------------------------------------------------------------------------------

#6. 
