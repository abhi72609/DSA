#       LCM
c = int(input("Enter 1st number : "))
d = int(input("Enter 2st number : "))
y = max(c,d)
while True:
    if y % c == 0 and y % d == 0:
        print("LCM of c and d :",y)
        break
    y += 1