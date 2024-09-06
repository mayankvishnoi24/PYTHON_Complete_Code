# Write a Python program to accept the height of a person in centimeter and categorize the person according to their height. 

# Test Data : 135
# Expected Output :

# The person is Dwarf.
# <140   Dwarf
# <140  >170 Average
# >170    Tall


h = float(input("enter the height: "))

if h<=140:
    print(h,"Naatu")
elif h<=170:
    print(h,"Average")
else:
    print(h,"tall")