numb = int(input("Enter the Number : "))
dup = numb
while(dup > 0):
    lastdigit = dup % 10
    print(lastdigit) 
    dup //= 10