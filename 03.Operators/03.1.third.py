# String Data use on the operators 
## airthmetic
## assignment
## comparision

i = "python"
j = "Programming"

# print(i,""+"",j)      ## Working two data ko conicate
# print(i,""-"",j)        ## TypeError: unsupported operand type(s) for -: 'str' and 'str'
# print(i*2,j*2)            ##  working data (pythonpython ProgrammingProgramming)
# print(i,""/"",j)            ## TypeError: unsupported operand type(s) for /: 'str' and 'str'
# print(i,""//"",j)             ## TypeError: unsupported operand type(s) for //: 'str' and 'str'
# print(i,""**"",j)              ## TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'
# print(i,""%"",j)                    ## TypeError: not all arguments converted during string formatting

# Same as assignment operator 
# (+=,*=) only these operator working

# Comparision operator  using string data 

# ASCII Code was provide the any string perform the comparision using ascii code

i = "python"
j = "Programming"

print(i>j)
print(i<j)
print(i>=j)
print(i<=j)
print(i!=j)
print(i==j)