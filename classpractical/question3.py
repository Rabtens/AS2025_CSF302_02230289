import math

# Q3: Areas and Volumes

# Circle Area
def circle_area(r):
    return math.pi * r * r

# Sphere Volume
def sphere_volume(r):
    return (4/3) * math.pi * r**3

# Cone Volume
def cone_volume(r, h):
    return (1/3) * math.pi * r**2 * h

# Pyramid Volume (Square base)
def pyramid_volume(base, h):
    return (1/3) * base * base * h

# Cylinder Volume
def cylinder_volume(r, h):
    return math.pi * r**2 * h

# Rectangle Area
def rectangle_area(l, w):
    return l * w

# Regular Polygon Area (n sides, side length a)
def polygon_area(n, a):
    return (n * a**2) / (4 * math.tan(math.pi / n))

# Example
print("Circle Area (r=5):", circle_area(5))
print("Sphere Volume (r=5):", sphere_volume(5))
print("Cone Volume (r=3, h=7):", cone_volume(3,7))
print("Pyramid Volume (base=4, h=6):", pyramid_volume(4,6))
print("Cylinder Volume (r=3, h=7):", cylinder_volume(3,7))
print("Rectangle Area (l=4, w=6):", rectangle_area(4,6))
print("Polygon Area (n=6, side=4):", polygon_area(6,4))
