# Display the passing division on percentage in a college.

percent = int(input("Enter percentage: "))

if percent >= 80:
    print("First Division")
elif percent >= 60:
    print("Second Division")
elif percent >= 40:
    print("Third Division")
else:
    print("Fail")