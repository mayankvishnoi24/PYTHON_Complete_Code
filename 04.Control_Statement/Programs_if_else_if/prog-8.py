# Write a Python program to accept a coordinate point in a XY coordinate system and determine in which quadrant the coordinate point lies. 

# Test Data : 7 9

# Expected Output :
# The coordinate point (7,9) lies in the First quadrant.

import math
x1, y1 = 2, 3

# Coordinates of the second point
x2, y2 = 5, 7

# Calculate the distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"Distance between points ({x1}, {y1}) and ({x2}, {y2}) is {distance}")