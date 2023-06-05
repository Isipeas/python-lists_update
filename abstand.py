import math

point_a = [3,8]
point_b = [7,13]

def abstand (a, b):
    ergebnis = math.sqrt(a[0]-b[0])**2+(a[1]- b[1])**2
    return ergebnis

print (abstand(point_a, point_b))
