x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

distance_a = math.sqrt(x12 + y12)
distance_b = math.sqrt(x22 + y22)

if distance_a > distance_b:
print("B is further from the origin.")
elif distance_b > distance_a:
print("A is further from the origin.")
else:
print("A and B are at the same distance from the origin.") remove math.sqr

