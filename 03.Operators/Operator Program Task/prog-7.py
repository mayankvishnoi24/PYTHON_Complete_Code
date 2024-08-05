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