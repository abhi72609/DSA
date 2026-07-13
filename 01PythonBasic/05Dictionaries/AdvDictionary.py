df = {'cust_id': [1, 2, 3],
 'age': [22, 23, 24],
 'location': ['Blr', 'Pune', 'Mum'],
 'status': [1, 0, 0],
 'name': ['Ram', 'shyam', 'laxam']}

# Iterate over key
for i in df:
  print(i)


# Iterate over key : value
for i in df:
  print(i,":", df[i])

for i in df:
  print(f"Column Name is {i}, values are {df[i]}")



print(df.keys())
print(df.values())
print(df.items())

# items
for key, value in df.items():
  print(key, value)

for i,j in df.items():
  print(i)

for i,j in df.items():
  print(j)

for i in df.values():
  print(i)

# df.items is not used or df.values is not used then to access value df[i] should we witten in print statement 
for i in df:
  print(df[i])

print("age" in df.keys())
print("asasaead" in df.keys())



# in e.values() searches only among the direct values of the dictionary. It does not search inside nested objects like lists, tuples, or dictionaries. Therefore, 'val2' in e.values() returns False because 'val2' is an element inside a list value, not a direct dictionary value. However, ['val2', 'val3'] in e.values() returns True because that entire list exists as one of the dictionary's values.
e ={'key1':'val1', 'key2':['val2','val3']}
print('val1' in e.values())

# e ={'key1':'val1', 'key2':['val2','val3']}
# print('val2' in e.values())

e ={'key1':'val1', 'key2':['val2','val3']}
print(['val2', 'val3'] in e.values())


# DataType Stored in Lib
random ={
    "key1": [5,6,7],
    "key2": (4,5,6),
    "set1":{4,8,9},
    "new loop":{"new_key":1},
    "a": 1,
    "b": 1.0,
    "c": "abcc",
    "d": True
}
print(type(random['new loop']))

new_random = {
    1 : [1,2,3],
    1.0:(6,7,9),
    "a": (75,44,66),
    True: [77,88]
}

#       List, set and dictionary are mutable in nature thus they can't be keys
# will_not_work ={
#     [1,2,3] :"a",
#     {7,7,7,1,2,3,5,5}   : "a"
# }
#       tuple are immutable in nature
will_work ={
    (1,2,3) :"a"
}
print(will_work)



my_dict = {'banana': 3, 'apple': 2, 'orange': 5, 'grape': 1}
my_dict

#   Sort dictionaries in incresing order of unicode
print(dict(sorted(my_dict.items())))
#   Sorted in Reverse order by using values
print(dict(sorted(my_dict.items(),key = lambda x: x[1], reverse=True )))

# help(sorted)

t = (5,8,1,2)
print(sorted(t))


random ="zzzzztttteeee"
# set(r)
print(random.count('t'))

result ={}
for i in set(random):
  result[i] =random.count(i)
print(dict(sorted(result.items())))

print(result)

print(set(random))

print(random.count('r'))