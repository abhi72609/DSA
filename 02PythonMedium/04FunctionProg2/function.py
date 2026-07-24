x = 5
x1 = 3 * x
x2 = x1 + 1

print(x) # can't roll back mutation and waste of memory by creating variable

# Mutation :  Changing the existing value of a variable/object.

# solve above issue using functional programming
# Functional Programming Principle:
# Avoid modifying existing data directly.
# Instead, take input, perform operations, and return a new value.
def mutation(x):
    x = x * 3
    x = x + 1

    return x

print(x)
print(mutation(x))


# map function
m = [1,2,3,4,5,6]

#1st way
res = []
for i in m:
    res.append(i**2)

# 2nd way : Using List Comprehension
res1 = [i**2 for i in m]

#3rd Way (best way)
res2 = list(map(lambda x : x ** 2, m))

print(res)
print(res1)
print(res2)


