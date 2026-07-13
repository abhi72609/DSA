



def foo():
    return 1,2,3

f = foo()
print(type(f))

#  Working with a List of Tuples (pop() and Tuple Immutability)
a = [(1, "Bipin"), (2, "Ranjan"), (3, "Shanoor"), (4, "Shital"), (5, "Tharoor")]

print(a.pop(4))
# a[3][0] = 400
# print(a)


el = [(1, "Bipin"), (2, "Ranjan"), (3, "Shanoor"), (4, "Shital"), (5, "Tharoor")]
for i,j in el:
    print(f"Roll no - {i} is {j}")
    # f - inside print(f) is used for accessing value and formatting values too



x = (1,2,3)
y = (4,5,6)
z = x+y
# Tuple is immutable in nature so it won't change it will not get added and it will not concatenate
print(z)
print(len(z))

# Swap Two Variable
#   1st Approach
a = 5
b = 10
temp = a
a = b
b = temp
print(a)
print(b)

#   2nd Approach
a = 5
b = 10
b = a + b
a = b - a
b = b - a
# Since there is no f, Python treats the string as plain text. It does not replace {a} and {b}.
print("a is {a}, b is {b}")

# Here, the f tells Python to evaluate the expressions inside {} and substitute them with their values.
print(f"a is {a}, b is {b}")


#   3rd Approach
a = 5
b = 10
a , b = b , a
print(f"a is {a}, b is {b}")