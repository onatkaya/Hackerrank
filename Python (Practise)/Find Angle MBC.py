import math

degree_sign= u'\N{DEGREE SIGN}'

side_1 = int(input()) # side AB
side_2 = int(input()) # side BC

long_side = math.sqrt(pow(side_1,2) + pow(side_2,2)) # finding the long side of the triangle, side AC

side_3 = long_side / 2  # side AM = MC = BM

# finding the cosine (cos) value of our angle
cos_val = (side_2) / (long_side) 

# finding the angle in radian using acos
acos_val = math.acos(cos_val)

# turning the radian value to angle format and printing it
final_degree = round(math.degrees(acos_val))
print(str(final_degree) + degree_sign)