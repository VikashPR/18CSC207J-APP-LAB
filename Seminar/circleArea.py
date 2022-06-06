def areaCircle(r):
    return 3.14159 * r * r

def perimeterCircle(r):
    return 3.14159 * r * 2

radius = float(input("Enter the radius of the circle: "))  # input() returns a string

areaCircle = areaCircle(radius)

perimeterCircle  = perimeterCircle(radius)

print("The area of the circle is: ", areaCircle)
print("The perimeter of the circle is: ", perimeterCircle)