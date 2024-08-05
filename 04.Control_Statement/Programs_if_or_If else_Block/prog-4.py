# Display the check condition eligibility in a college.

phy = int(input("Enter the physics no. : "))
chem = int(input("Enter the chemistry no. : "))
math = int(input("Enter the math no. : "))

if phy>=60 and chem >= 55 and math >= 65:
    print("You are Eligible")
else:
    print("You are not Eligible")