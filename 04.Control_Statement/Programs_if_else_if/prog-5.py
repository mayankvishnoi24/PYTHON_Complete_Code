# Write a Python program to read the value of an integer m and display the value of n is 1 when m is larger than 0, 0 when m is 0 and -1 when m is less than 0. 
# Test Data : -5
# Expected Output :
# The value of n = -1

m = int(input("Enter an integer value for m: "))

if m > 0:
    n = 1
elif m == 0:
    n = 0
else:
    n = -1

print(f"The value of n is: {n}")
