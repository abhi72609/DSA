runs = [62,34,67,89,26,80,145,67,90]
print(runs[:])
# All value from 0 index to before 5th
print(runs[0:5])

# All value from -5 index (negative indexing)
print(runs[-5:])

# All value from 0 index to before 5th index (Indexing start from 0)
print(runs[:5])

# All value of list (it's like range)
print(runs[:])

# All value after 3rd index (Indexing start from 0)
print(runs[3:])

new_runs = []
for i in range(1,6):
    new_runs.append(runs[-i])
print(new_runs)


print(runs[::1])
print(runs[::-1])

print(runs[::2])
print(runs[::-2])

print(runs[-1:-6:-1])



# 1ST APPROACH
numbers = [1,2,3,4,5]
new_list = []

for i in range(0,len(numbers),1):
    if i < len(numbers)-1:
        new_list.append(numbers[i])
    else :
        new_list.insert(0,numbers[i])

print(new_list)

# 2ND APPROACH
print([numbers[-1]]+numbers[0:4])



# list Reversal
new_value = [1,2,3,4,5]
new_value.reverse()
print(new_value)

y = [1,2,3,4,5]
print(list(reversed(y)))
print(y)