#Question 3(i)
#  Write a Python program that prompts a user to enter numbers. The process will repeat until
#  the user enters 0. Finally, the program prints sum of the numbers entered by the user.
#SOLUTION
def sum_numbers() :
    sum = 0
    while True:
        number = float(input("Enter a number (or 0 to stop): "))
        if number == 0:
            break
        sum+=number
        print(f"The sum of numbers entered is:", sum)
        sum_numbers()


# Question 3(ii)
# Write a Python program to print all the numbers from 1 to 100 that are not divisible by 2 
#SOLUTION
for number in range(1,101):
    if number % 2 !=0:
        print(number)

