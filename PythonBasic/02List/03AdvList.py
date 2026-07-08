#       2D List
a = [[1,2,3],[4,5,6],[7,8,9]]

for i in a:
    print(i)


for i in a:
    for j in i:
        print(j, end =" ")
    print()


random = [[1, 2, 3], ["a", "b", "c", "d", "e"], [4.5, 6.7]]
for i in random:
    for j in i:
        print(j, end=" ")
    print()

#user to give me the values and we want to create a list
##enter the no of elements in the list
num_elements = int(input("Enter the no of elements"))

# my_list = []
# for i in range(num_elements):
#     elements = input()
#     my_list.append(elements)
# print(my_list)




#Take a 3X3 matrix as an input from the user.
#Given this matrix -

a = []
for i in range(3):
    inner_list = []
    for i in range(3):
        inner_list.append(int(input()))
a.append(inner_list)


#Calculate the sum of all the elements in the matrix.
SumOfAll = 0
for i in a:
    for j in i:
        SumOfAll += j
print(SumOfAll)


#Calculate the sum of elements in each row.
