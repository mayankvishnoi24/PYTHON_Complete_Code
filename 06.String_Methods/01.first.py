### String Methods

d1 = "Python Program"

print(d1.capitalize())  # First letter is capital
print(d1.casefold())    # all the letters are small
print(d1.center(100,"*")) # In the add the set width value
print(d1.count('p',0,10)) # is the count of the same character 
print(d1.encode())
print(d1.endswith('M'))
print(d1.startswith('p'))

print(d1.replace('python','C++'))
print(d1.split('-'))

d1="""python is open source
Java  is open source
c  is open source
c++  is open source
php  is open source"""

print(d1.splitlines())
print(d1.split())


d=['python','is','best']

print(" ".join(d))

d1="     python       "

print(d1.strip())
print(d1.lstrip())
print(d1.rstrip())

d1="12345"
d1="Abvcdsjscj123\n"

print(d1.isnumeric())
print(d1.isalpha())
print(d1.isalnum())
print(d1.islower())
print(d1.isupper())
print(d1.istitle())
print(d1.isprintable())