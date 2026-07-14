# class doesn't have any method/properties define then we write pass to avoid the error : IndentationError
class Student:
    pass

# isinstance - isinstance(obj, class) checks whether an object belongs to a particular class or its parent classes.
# Here, Student itself is an object of the metaclass 'type', and 'type' inherits from 'object',
print(isinstance(Student, object))

a = Student()
print(type(a))


# print(isinstance(a, object))   # True
# Why True?
# Because every class in Python implicitly inherits from object.

# 'a' is a reference variable pointing to a Student object.
# isinstance() checks the actual object referenced by 'a',
# not whether the variable itself is an object.

print(isinstance(a,object))

s1 = Student()
s1.name = "Neelesh"
s2 = Student()
s2.name = "Suraaj"
print(s1.name)
print(s2.name)



# class Student:
#     def hello():
#         print("Hello Students!")
# s3 = Student()
# s3.hello()
# Student.hello(s3)

class Student:
    def hello(self):
        print("Hello Students!")
        # id is basically a location 
        print(id(self))
s3 = Student()
s3.hello()
print(id(s3))