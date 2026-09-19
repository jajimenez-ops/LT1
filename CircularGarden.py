import math


radius = float(input(f"Enter the radius of the circular garden in meters:"))

area = math.pi * pow(radius,2)

circumference = 2 * math.pi * radius

sqrt_area = math.sqrt(area)
rounded_down_area = math.floor(area)
rounded_up_area = math.ceil(area)

print(f"Area of the garden: {area:.2f} square meters")
print(f"Circumference of the garden: {circumference:.2f} meters")
print(f"The square root of the area : {sqrt_area:.2f}")
print(f"Area rounded down: {rounded_down_area} square meters")
print(f"Area rounded up: {rounded_up_area} square meters")