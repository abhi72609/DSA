class SchoolMember:
    def __init__(self, name):
        self.name = name

class Student (SchoolMember):
    def __init__(self, name, grade):
        super().__init__(name) 
        self.grade = grade

class Staff (SchoolMember):
    def __init__(self, name, salary):
        super().__init__(name) 
        self.salary = salary

class Teacher (Staff):
    def __init__(self, name, salary, subject):
        super().__init__(name, salary)
        self.subject = subject

s1 = Student("Rahul", 'A')
print("Name :",s1.name)
print("Grade :",s1.grade)


t1 = Teacher("Manoj Sir",50000,"Hindi")
print(f"Name : {t1.name}")
print("Salary :",t1.salary)
print("Subject :",t1.subject)


# Named Mangling - private 
# name → public
# _name → protected (by convention)
# __name → private (by convention and name mangling)
class BankAccount:
    def __init__(self, balance): 
        self.__balance = balance

    def withdrawl(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

    def check_balance(self):
        return self.__balance
    
b1 = BankAccount(10000)
b1.withdrawl(2000)
b1.deposit(6000)
print(b1.check_balance())



#   Multiple Inheritance
class A:
    def __init__(self,a):
        self.a = a
    
class B:
    def __init__(self,b):
        self.b = b

class C(A,B):
    def __init__(self, a,b,c):
        # can't call super statement for 2 different class i.e, not possible - super(A,B)
        A.__init__(self,a)
        B.__init__(self,b)
        self.c = c


c1 = C(1,2,3)
print(c1.a) 

# Method Resolution Order
# 1.  Left to Right
# 2.  We go to parent only when all children are   considered

class A:
    x = 10

class B(A):
    pass

class C(B):
    pass

class D(A):
    x = 5

class E(C, D):
    pass

e1 = E()
print(e1.x)

print(E.__mro__)


