# Write a Python program to find the largest of three numbers. 

# Test Data : 12 25 52
# Expected Output :
# 1st Number = 12,        
# 2nd Number = 25,       
# 3rd Number = 52

# The 3rd Number is the greatest among three

num1 = input("enter the value1: ")
num2 = input("enter the value2: ")
num3 = input("enter the value3: ")

res = num1 + num2 + num3

print(f"1st Number = ",{num1})
print(f"2nd Number = ",{num2})
print(f"3rd Number = ",{num3})

if num1 > num2 or num2 > num3:
    print(f"The {num3}rd Number is the greatest among three")
else:
    print("Wrong")