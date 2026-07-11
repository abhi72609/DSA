s1 ={'a':1, 'b':2, 'c':3} #k,v k:v

df ={'cust_id':[1,2,3],
     'age':[21,22,23]}

print(df['age'][2])

a = {
    "random": "something which is not well defined",
    "bizzare": "something which is unusual"
}
print(type(a))
print(a['random'])

city_wise_data = {
    "Delhi": 450,
    "Mumbai": 400,
    "Bengaluru": 325
}

city_wise_data_tup = [("Delhi", 450), ("Mumbai", 400), ("Bengaluru", 325)]
print(city_wise_data_tup[0][1])


print(city_wise_data['Delhi'])
city_wise_data['Delhi'] = 500


df ={'cust_id':(1,2,3),
     'age':[21,22,23],
     'income' :{100,100,200}}

df['age'][0] = 25
print(df)
# df['cust_id'][0] = 31  tuple are immutable in nature



# list add 100 and if run once more will add one more 100 but in dictionaries thinks get updated if data is already present
# a = [5,6,7,8]
# a.append(100)
# print(a)

df ={'cust_id':[1,2,3],
     'age':[21,22,23]}
df['location'] =['Blr', 'Pune', 'Mumbai']
df['location'] =['Blr', 'Pune', 'Mum']
print(df)


# Pandas package is not instal else it would convert  the dictionaries into a table (used in backend)
# import pandas as pd
# df1 = pd.DataFrame(df)
# print(df1)
#       OUTPUT
#       cust_id  age location
#             1   21      Blr
#             2   22     Pune
#             3   23      Mum


#       update
df.update({'status': [1,0,0], 'name': ['Ram', 'shyam','laxam'], 'age':[22,23,24]})
print(df)

# if their exist duplicate key then it will update and give latest value 
c ={'a':1, 'b':2, 'a':100}
print(c)


print(df['age'])
#get
print(df.get('age'))
# print(df['Age']) without get it will throw error if that key doesn't exist
# but with get error won't occur
print(df.get('asasasas'))


a =[5,6,7,8]
print(a.pop())
a1 ={5,9,7,7,6,2}
print(a1.pop())
print(df.pop('status'))

del df['age']

df.clear()
print(df)



df = {'cust_id': [1, 2, 3],
 'age': [22, 23, 24],
 'location': ['Blr', 'Pune', 'Mum'],
 'status': [1, 0, 0],
 'name': ['Ram', 'shyam', 'laxam']}

df['name'].pop()
print(df)