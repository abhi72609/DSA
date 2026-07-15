class Car:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage
    
c1 = Car("Nexon", 12)
c2 = Car("Venue", 15)
print(c1)
# output - <__main__.Car object at 0x0000020407D3C6E0>

#changing the default behaviour of print () function
class Car:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def __str__(self):
        return f"Suraaj car is great but the mileage is {self.mileage} for {self.name}"
    
    def __add__(self, other):
        return self.mileage + other.mileage
    
    def __lt__(self, other):
        return self.mileage < other.mileage
    
    
c1 = Car("Nexon", 12)
c2 = Car("Venue", 15)
print(c1)
print(c1 + c2)
print(c1<c2)