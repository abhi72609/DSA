#       GCD

a = int(input("ENter 1st Number : "))
b = int(input("ENter 2st Number : "))
x = min(a,b)
for i in range(x,0,-1):
    if a % i == 0 and b % i == 0:
        print("GCD of A and B is :",i)
        break

