def perimeter_area(r,h):
    chuvi = 2*r*h
    dientich=3.14*r**2
    return chuvi,dientich
r = int(input("Enter radius of circle:"))
h = int(input("Enter tall of circle:"))
print(perimeter_area(r,h))