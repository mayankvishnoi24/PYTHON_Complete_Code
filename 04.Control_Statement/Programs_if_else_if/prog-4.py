# Write a Python program to read the age of a candidate and determine whether it is eligible for casting his/her own vote. 
# Test Data : 21
# Expected Output :
# Congratulation! You are eligible for casting your vote.

age = int(input("enter the age value: "))
if age >= 18 :
    print("Congratulation! You are eligible for casting your vote.")
else:
    print("Sorry! You are not eligible for casting your vote.")