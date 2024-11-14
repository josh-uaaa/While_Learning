def equilateral(sides):
    return is_triangle(sides) and len(set(sides)) == 1

def isosceles(sides):
    return is_triangle(sides) and len(set(sides)) <= 2

def scalene(sides):
    return is_triangle(sides) and len(set(sides)) == 3

def is_triangle(sides):
    a, b, c = sides[0], sides[1], sides[2]
    return (a != 0) and (b != 0) and (c != 0) and (a + b >= c) and (b + c >= a) and (a + c >= b)