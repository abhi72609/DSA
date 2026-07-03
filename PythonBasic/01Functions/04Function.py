# Square 
def sqr(n):
    print(n*n)
sqr(5)


# Area of Reactangle
def  area(l,b):
    print(l*b)
area(4,5)

# Function with variable
def greet(name):
    print("Jai Shree Ram", name)

name = input("Enter Name : ")
greet(name)

# GCD using Function
def gcd(a,b=5):
    x = min(a,b)
    for i in range(x,0, -1):
        if a%i == 0 and b%i == 0:
            print("GCD of a and b is :",i)
            break

gcd(9,6) 
# b = 5 is override by 6


