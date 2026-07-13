x = "1 1 1 1 1"
y = x.split()
print(y)

print("-".join(y))
#       or
j="-".join(y)
print(j)



#       find - if ture then o/p index of value/ if false then o/p will be -1
print("this is totally random".find("randoms"))

#       replace
random1 = "This is a random string that I have created i know this totaly random"
print(random1.replace("random", "Super Random"))
# Original String won't replace
print(random1)

#       replace
x = '10,00,000'
print(float(x.replace(",","")))

#       count
print(random1.count('random'))

#       isdigit
print("abc".isdigit())

#       isalpha
print("abc1".isalpha())

#       isalnum
print("abc1".isalnum())

#       isupper
print("A".isupper())

#       islower
print("A".islower())

#       upper
print("a".upper())


#       Palindrome
n ="NAMAN"
def check_palindrome(a):
  a =a.lower()
  return "is palindrome" if a == a[::-1] else "not palindrome"
print(check_palindrome(n))

# everytime we store object it will give a new location
a = "aaaa"
print(id(a))
a = "bbbbb"
print(id(a))


b =[1,2,3]
print(id(b))

x = "Amit"
print(id(x))

x = "hari"
print(id(x))


x1 =['Amit']
print(id(x1))


x1[0] ='Hari'
print(x1)
print(id(x1))

#       String doesn't support the append function
# x ="rajat"
# print(x.append("sharma"))

# String can't be change
# p = "Hello"
# p[0] ="L"
# print(p)


a = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]

ans =[]
for i in range(3):
  curr_sum = 0
  for j in range(3):
    curr_sum = curr_sum+ a[j][i]
  ans.append(curr_sum)
print(ans)