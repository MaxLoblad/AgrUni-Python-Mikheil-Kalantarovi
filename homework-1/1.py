
sides = input("Enter sides of the triangle: ")
sides = list(map(float, sides.split()))
tr_perimeter = sides[0] + sides[1] + sides[2]
s = tr_perimeter / 2
tr_area = (s*(s-sides[0])*(s-sides[1])*(s-sides[2])) ** 0.5
print("The area of the triangle is:", tr_area)
print("The perimeter of the triangle is:", tr_perimeter)

