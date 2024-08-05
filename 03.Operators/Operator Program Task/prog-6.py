# 6. Write a program to calculate the area and perimeter of rectangle with user input length and breadth.

# Rectangle  Area: length*breadth

# Perimeter rectangle: 2*(l+b)

leng = int(input("Enter an length value: "))
brea = int(input("Enter an breadth value: "))

area = leng * brea
perimeter = 2 * (leng * brea)

print("Area of Rectangle :",area)
print("Perimeter of Rectangle :",perimeter)