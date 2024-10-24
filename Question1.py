# Question 1(i)
# Write a Python program to find the distance between two coordinate points (x1, y1) and (x2, y2).
#SOLUTION
import math
def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2-x1) ** 2 + (y2 - y1) ** 2)
    return distance
if __name__ == " _main_":
    x1 = float(input("Enter x1: "))
    y1 = float(("Enter y1: "))
    x2 = float(("Enter x2: "))
    y2 = float(("Enter y2: "))
    distance = calculate_distance(x1, y1 , x2 , y2)
    print(f"The distance between points ({x1}, {y1}) and ({x2}, {y2}) is {distance:.1f}")



# Question 1(ii)
# Write a Python program to find maximum between three numbers.
# Function to find the maximum of three numbers
#SOLUTION
def find_maximum(x, y, z):
     return max(x, y, z)
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
maximum_number = find_maximum(num1, num2, num3)
print(f"The number is: {maximum_number}")




