# arr = [10,20,30,40]
# print(arr[0:4])

# #   list
# arr1 = [0] * 5     
# i=0
# while i<5:
#     arr1[i] = int(input())
#     i+=1
# print(arr1)
# print(arr1[3])


# #   2D Arr
# rows = int(input("Enter No of Rows : "))
# cols = int(input("Enter No of Col : "))

# arr2 = []

# for i in range(rows):
#     rows = list(map(int, input().split()))
#     arr2.append(rows)

# print(arr2)


#   STRING

str1 = "ABHISHEK"
# TYPE
print(type(str1))
print(str1)

#Access from back
print(str1[-1])
# Str .replace
Str2 = str1.replace('I','S')
print(Str2)


i = 0
while i < len(str1):
    print(str1[i])  
    i+=1