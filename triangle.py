import math

class Triangle():
    def __init__(self,a,b,c):
        self.length1 = a
        self.length2 = b
        self.length3 = c 

    def perimeter(self):
        return self.length1 + self.length2 + self.length3

    def scale(self, scale_factor):
        return Triangle(scale_factor * self.length1, scale_factor * self.length2, scale_factor * self.length3)

    def area(self):
        semi_perimeter = (self.length1 + self.length2 + self.length3) / 2 
        return (math.sqrt(semi_perimeter * (semi_perimeter - self.length1) * (semi_perimeter - self.length2) * (semi_perimeter - self.length3)))

    def is_valid(self):
        if (self.length1 + self.length2) > self.length3 and (self.length2 + self.length3) > self.length1 and (self.length1 + self.length3) > self.length2:
            return True
        else:
            return False

    def is_right(self):
        if self.length1**2 + self.length2**2 == self.length3**2:
            return True
        else:
            return False



t = Triangle(3,4,5)

q = t.scale(3)
print (q.length1, q.length2, q.length3)
print(t.area())
print(t.is_valid())
print(t.is_right())