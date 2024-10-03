## String - Data type contains text values
##        -- sequence of characters

# s = "Mayank"
# s1 = "Mayank_Vishnoi"

# print(s)
# print(s1)

# s2 = '"python" is best'
# print(s2)

# # But won't this text

# s3 = "This is a 'justify' paragraph2"
# print(s3)

# You can use three time inverted coma
# Multiline string write

# s4 = '''Python is a best language'''
# print(s4)

# s5 = """This is a para certified.
#         Java is a scripting language.
#         python is a programming language."""
# print(s5)


#  Indexing process

# s = "Python"
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])
# print(s[5])
# print(s[6]) ## IndexError: string index out of range

#  Negetive Indexing process

# s = "Python"
# print(s[-1])
# print(s[-2])
# print(s[-3])
# print(s[-4])
# print(s[-5])
# print(s[-6])

# Example of indexing

# s1 = """This is a
# python programming
# language."""

# print(s1[-1])

## String Slicing

### Positive indexing

s1 = "Python"
# print(s1[1:4])  ## yth
# print(s1[1:4:1]) ## yth
# print(s1[0:4]) ## Pyth
# print(s1[:4]) ## Pyth
# print(s1[2:6]) ## thon
# print(s1[2:]) ## thon
# print(s1[:]) ## Python

### negetive indexing

print(s1[-4:-1])  ## tho
print(s1[-4:-7:-1])  ## typ
print(s1[-4:])  ## thon
print(s1[-4::-1])  ## tyP
print(s1[:-3:-1])  ## no
print(s1[::-1])  ## nohtyP

### Positive or negetive indexing mixing

print(s1[1:-3])  ## yt
print(s1[:-1])  ## Pytho
print(s1[-1:])  ## n
