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