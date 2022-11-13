def area_triangle(height, base):
    return height*base/2

h = int(input("Enter height: "))
b = int(input("Enter base: "))
area1 = area_triangle(3,4)
area2 = area_triangle(h,b)
print(area1)
print(area2)