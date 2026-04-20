#Switch Case
# Take the day number and print the corresponding day
# for 1 Print Monday
# for 2 Print Tuseday

# 1sy Way ( Basic )
num = int(input("Enter Number : "))
if(num == 1):
    print("Monday")
elif(num == 2):
    print("Tuesday")
elif(num == 3):
    print("Wednesday")
elif(num == 4):
    print("Thrusday")
elif(num == 5):
    print("Friday")
elif(num == 6):
    print("Saturaday")
else:
    print("sunday")


# 2nd Way (     best Way    )
day = int(input("Enter day number: "))

days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

print(days.get(day, "Invalid day"))