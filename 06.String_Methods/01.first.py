### String Methods

d1 = "Python Program"

print(d1.capitalize())  # First letter is capital
print(d1.casefold())  # all the letters are small
print(d1.center(100, "*"))  # In the add the set width value
print(d1.count("p", 0, 10))  # is the count of the same character
print(d1.encode())
print(d1.endswith("M"))
print(d1.startswith("p"))

print(d1.replace("python", "C++"))
print(d1.split("-"))

d1 = """python is open source
Java  is open source
c  is open source
c++  is open source
php  is open source"""

print(d1.splitlines())
print(d1.split())


d = ["python", "is", "best"]

print(" ".join(d))

d1 = "     python       "

print(d1.lstrip()) # Remove the left space
print(d1.rstrip()) # Remove the right space
print(d1.strip()) # Remove the space

d1 = "12345"
d1 = "Abvcdsjscj123\n"

print(d1.isalnum())  # Check the string is alphanumeric or not
print(d1.isalpha())  # Check the string is alphabet or not
print(d1.isdecimal())  # Check the string is decimal or not
print(d1.isdigit())  # Check the string is digit or not
print(d1.isidentifier())  # Check the string is identifier or not
print(d1.islower())  # Check the string is lower or not
print(d1.isnumeric())  # Check the string is numeric or not
print(d1.isprintable())  # Check the string is printable or not
print(d1.isspace())  # Check the string is space or not
print(d1.istitle())  # Check the string is title or not
print(d1.isupper())  # Check the string is upper or not
