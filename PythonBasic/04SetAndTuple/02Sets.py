s1 = {7,7,7,1,2,3,5,5}
print(s1)

s2 = {"mangoes","apple","Apple","Orange","apple"}
print(s2)

s1.pop()
print(s1)

s1.remove(3)
print(s1)

s1.add(100)
print(s1)

s1.add(-1)
print(s1)

s1.add(4)
print(s1)

## update
s1.update([4,7,9,11,13])
print(s1)

#  Unique_Char using sets
def unique_Char(name):
    return set(name)

print(unique_Char("tttttttdddddddddcccccccccc"))


#   intersection
# Meaning: Combine both sets and REMOVE duplicate elements.
s1 = {2, 3, 4, 5}
s2 = {1, 3, 4, 6, 7, 8}
print(s1.intersection(s2))
#       OR
print(s1 & s2)


#   union
# Meaning: Elements present in FIRST set but NOT in SECOND set.
print(s1.union(s2))
#       OR
print(s1 | s2)


#   difference
# Meaning: Elements present in SECOND set but NOT in FIRST set.
# s2 - s1  ==> "Remove s1 from s2"
print(s2.difference(s1))
#       OR
print(s2 - s1)


#   symmetric_difference
# Meaning: Elements present in ONLY ONE set.
# Common elements are removed.
print(s1.symmetric_difference(s2))
#       OR
print(s1 ^ s2)