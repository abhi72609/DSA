# Write Program that take Input of the age and print if you are adult or not
age = int(input("Enter Your Age : "))
if(age >= 18):
    print("Your Adult")
else:
    print("Your Not Adult")


# A school has following rules for grading system:
# a. Below 25-F
# b. 25 to 44-E
# c. 45 to 49-D
# d. 50 to 59 - C
# e. 60 to 79 - B
# f. 80 to 100 - A
# Ask user to enter marks and print the corresponding grade.

marks = int(input("marks : "))
if(marks < 25):
    print("F")
elif(marks <= 44):
    print("E")
elif(marks <= 49):
    print("D")
elif(marks <= 59):
    print("C")
elif(marks <= 79):
    print("B")
elif(marks <= 100):
    print("A")


# Take the age from the user and then decide accordingly
# 1. If age < 18,
# print-> not eligible for job
# 2. If age >= 18,
# | print-> "eligble for job"
# 3. If age >= 55 and age <= 57,
# | print-> "eligible for job, but retirement soon."
# 4. If age > 57
# | print-> "retirement time"

Age = int(input("Enter Age : "))

if(Age < 18):
    print("Not Eligble for job")
elif(Age <= 57):
    print("Eligble for job")
    
    if(Age >= 55):
        print("Elible for job but retrirement soon")
else:
    print("Retirement Time")