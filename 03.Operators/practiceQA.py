# 1. write a program to covert an input distance in meter to feet .  

# 1 meter= 3.28 feet

distance = float(input("Distance in meter: "))
print("meter to",distance*3.28,"feet")

# 2. write a program to covert an input temprature in celcius to farenheit .    

#  F = ( C × 9/5 ) + 32.

c = float(input("Enter the calcius: "))

f = (c * 9 / 5) + 32

print("Farenheit is :",f)

# print("temprature in celcius to",(c*9/5)+32,"farenheit")

# 3. write a program to calulate the total marks and percentage(out of 300) of student input test marks in English,math and Science.

engl = int(input("Enter the english marks: "))
math = int(input("Enter the math marks: "))
sci = int(input("Enter the science marks: "))

mark = engl + math + sci
percentage = mark/300*100

print("Student Marks:",mark)
print("Student Percentage:",percentage)

# 4. write a program to find an input number is even result is in True and False.

n1 = int(input("Enter the value: "))

res = bool(n1%2==0)

print("even or odd",res)

# 5. Write a program to calculate the area and perimeter of circle with user input radius.

# pi=3.14

# area of circle: pi*r*r

# perimeter of circle: 2*pi*r


radius = float(input("Enter the radius value: "))

circle = 3.14 * radius * radius
perimeter = 2 * 3.14 * radius

print("Area of Circle:",circle)
print("Perimeter of Circle:",perimeter)

# 6. Write a program to calculate the area and perimeter of rectangle with user input length and breadth.

# Rectangle  Area: length*breadth

# Perimeter rectangle: 2*(l+b)

leng = int(input("Enter an length value: "))
brea = int(input("Enter an breadth value: "))

area = leng * brea
perimeter = 2 * (leng * brea)

print("Area of Rectangle :",area)
print("Perimeter of Rectangle :",perimeter)

# 7. Write a program to swap the numbers into the variables.

# Before swaping:  a=10
#                  b=20
# After swaping:   a=20
#                  b=10


num1 = int(input("Enter the value1:"))
num2 = int(input("Enter the value2:"))

# Condition for swapping
res = num1
num1 = num2
num2 = res

# After the swapping
print("num1 :",num1)
print("num2 :",num2)