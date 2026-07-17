# IMPERATIVE PROGRAMMING
num = [1,2,3,4,5,6,7]
sq_num = []

for i in num:
    sq_num.append(i*i)
print(sq_num)


# FUNCTIONAL PROGRAMMING
num = [1,2,3,4,5,6,7]
sq_number = list(map(lambda x : x*x, num))
print(sq_number)

square = lambda x : x ** 2
print(square(5))

print((lambda x : x ** 2)(7))

#add 2 numbers
add_two = lambda x,y : x+y
print(add_two(5,7))

# conditions
print((lambda x : x if x > 5 else 0)(8))
print((lambda x : x if x > 5 else 0)(3)) 

#sorted 
students = [
    {"name": 'a', "marks" : 90},
    {"name": 'b', "marks" : 100},
    {"name": 'c', "marks" : 80},
    {"name": 'd', "marks" : 87},
    {"name": 'e', "marks" : 76},
]

print(sorted(students, key= lambda x: x["name"]))
print(sorted(students, key= lambda x: x["marks"]))
print(sorted(students, key= lambda x: x["marks"], reverse = True))