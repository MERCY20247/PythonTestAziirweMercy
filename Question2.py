# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F
# Function to determine the grade based on the mark scored
#SOLUTION
def determine_grade(mark):
    if mark >= 90:
        return 'Grade A'
    elif mark >= 80:
        return 'Grade B'
    elif mark >= 70:
        return 'Grade C'
    elif mark >= 60:
        return 'Grade D'
    elif mark >= 40:
        return 'Grade E'
    else:
        return 'Grade F'
    
def main():
    try:
        mark = float(input("Enter the mark scored (out of 100): "))
        
        if 0 <= mark <= 100:
    
            grade = determine_grade(mark)
            print(f"The obtained grade is: {grade}")
        else:
            print("Please enter a mark between 0 and 100.")
    
    except ValueError:
        print("Invalid input! Please enter a collect value.")

if __name__ == "__main__":
    main()
