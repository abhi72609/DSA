str1 = "String"
print(str1)

#       help is used to print statement written in - ''' ''' 
def sq(x):
    '''This function makes the square of the number'''
    return x*x
print(sq(5))


#  Why o/p is like this - <function sq at 0x000001D46177BB60>
# y = int(input("Enter the Number : "))
# def sq(y):
#     return y*y

# print(sq)

# y = int(input("Enter the Number : "))
# def sq(y):
#     return y*y

# print(sq(y))


#       ord function
print(ord('a'))

#       format
l = 10
b = 5
a = l*b
print("length is", l, "breath is", b, "area is",a)
                # or
print("length is {}, breath is {},area is {}".format(l,b,a))
                # or
print(f"length is {l}, breath is {b},area is {a}") 


#       splite
print("1 2 3 4".split())

str2 = "1 2 3 4"
print(str2.split())

str3 = "This_is_a_String_Lecture"
print(str3.split("_"))

print("1234,abcd".split(","))