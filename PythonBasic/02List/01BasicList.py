virat_k = [39,40,0,65,100]
# Runs in last match
print(virat_k [len(virat_k)-1])

# Runs in 2nd last match
print(virat_k[-2])

# Runs in first match without using  +ive indexing
print(virat_k [-(len(virat_k))])

# Runs in 2nd match without using  +ive indexing
print(virat_k [-(len(virat_k))+1])

#hardcoded way, add runs from even index no
virat_k[0] + virat_k[2] + virat_k[4]

# appends - adds the value at the every end of the list
virat_k.append(71) 
print(virat_k)

# insert - adds the value at the starting of the list
virat_k.insert(3,100)
print(virat_k)

# Extends -adds the value at the every end of the list
new_runs = [45,67,77]
virat_k.extend(new_runs)
print(virat_k)


value = 67
for i in virat_k:
    if i == value:
        virat_k.remove(i)
print(virat_k)


# for i in range(len(virat_k)):
#     if virat_k[i] == 67:
#         virat_k[i].pop()
# print(virat_k)

 
for i in virat_k:
    print(i)

sum = 0
for i in range(len(virat_k)):
    sum += virat_k[i]
print("Sum of Virat Score is  :",sum)

avg = (sum/len(virat_k))
print(avg)

avgRouundOff = round(sum/len(virat_k),2)
print(avgRouundOff)

EvenIndexSum = 0
for i in range(len(virat_k)):
    if i % 2 == 0:
        EvenIndexSum += virat_k[i]

print(EvenIndexSum)