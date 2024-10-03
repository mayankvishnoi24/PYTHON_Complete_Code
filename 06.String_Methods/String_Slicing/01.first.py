# String Formatting in Python

name = input("Enter name:")
course = input("Enter course:")
fee = int(input("Enter fee paid:"))
s = "My name is %s I am enrolled in %s course. I have paid %.2f INR"

print(s % (name, course, fee))

name = input("Enter name:")
course = input("Enter course:")
fee = int(input("Enter fee paid:"))
s = "My name is {} I am enrolled in {} course. I have paid {} INR"

print(s.format(name, course, fee))

name = input("Enter name:")
course = input("Enter course:")
fee = int(input("Enter fee paid:"))
s = f"My name is {name} I am enrolled in {course} course. I have paid {fee} INR"

print(s)
