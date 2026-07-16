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