from math import sqrt

def solve_quadratic(a,b,c):
    disc = b**2 - 4*a*c
    if (disc < 0):
        x = "No solution"
    elif (disc == 0):
        x = -b / (2*a)
    else:
        x = ((-b + sqrt(disc))/(2*a), (-b - sqrt(disc))/(2*a))
    print(x)
