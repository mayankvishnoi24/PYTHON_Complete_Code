# # DataTypes in python
# # int
# i = 30
# print(i)
# print(type(i))

# # float
# i = 30.5
# print(i)
# print(type(i))

# Complex (imaginery No.)
# i = 30+5j
# print(i)
# print(type(i))

# num1 = float(input("Enter the num1 : "))
# num2 = float(input("Enter the num2 : "))

# result = (num1+num2)
# print(result,"%")
# print(type(result))

# boolean Data (True/False)
# i = True
# print(type(i))
# i = False
# print(type(i))
# i = 0         #False it is 0 
# j = 1         # true it is positive 1
# print(bool(j))

# Byte Data 
# i = "Mayank"    # Character type data 
# print(type(i))

# i = b"Mayank"       # Byte Type data ,ASCII Code provided in any letter symbole or number
# print(type(i))

# print("",i)

# None type             # i don't know the defing the data 

# i = None
# print(i)

# Non primitive datatype ,Collection Type

# l1 = [1,2,3,4,5]
# print("List1",l1)
# print("List1",type(l1))
# print(l1[4])        # List index out of range

# # list is used a CRUD operation
# l1[3] = "Python"       ## Update value
# print(l1)
# l1.append(45)           ## adding value
# print(l1)
# l1.remove("Python")     ## Removing value
# print(l1)

# Tuple 

# t1 = (1,2,3,4,5)
# print(t1)
# print(type(t1))
# print(t1[2])

# tuple is Do not use a CRUD operation
# t1[3] = "Python"       ## Update value
# print(t1)
# t1.append(45)           ## adding value
# print(t1)
# t1.remove("Python")     ## Removing value
# print(t1)

# Set 
# s1 = {1,2.44,3+4j,False} ## Un arranged data not follow the sequencing
# print(s1)
# print(type(s1))
# print(s1[2])          # Don't access through the index value in set

# set is Do not use a CRUD operation only use create ,read or Delete
# s1.remove(2.44)     ## Removing value
# print(s1)
# s1.add("Mayank")       ## add value
# print(s1)

# Frozenset or set will be same 
# f1 = {1,2.44,3+4j,False} ## Un arranged data not follow the sequencing
# print(frozenset(f1))
# print(type(f1))
# print(f1[2])          # Don't access through the index value in set
# set is Do not use a CRUD operation only use create ,read or Delete


# Range 
            # Start #end #step    
# print(list(range(1,11,1)), "list")
# print(tuple(range(1,11,1)), "tuple")
# print(set(range(1,11,1)), "set")
# print(frozenset(range(1,11,1)), "frozenset")

# print(list(range(11)))

# Reverse the counting
# r = range(11,0,-1)
# you can type cast the range data any formate like list tuple set
# print(list(r))

# Don't change the data 
# print(r[6])


# # Dictionery ('Key' : 'Value')

# dic = {
#     'name' : "Mayank",
#     'class' : "5th",
#     'roll_no' : 2682483894,
#     'school' : 'Summer Field Public School'
# }
# print(dic)
# print(type(dic))

# data1 = {
#     'a' : ['apple','airplane','alpha'],1:2.5,3:3+5j,4:False}
# print(data1)
# print(type(data1))

# ### you can use CRUD operation

# data1[1]=300        ## Updating the data 
# print(data1)

# data1['b']='Name'   ## Adding the data
# print(data1)

# print(data1['a'][1])    ## you can access the data / reading

# data1.pop(3)                ## can we delete the key automatic data deleted
# print(data1)



# data1 = {'menu': ['Pizza','Maggi','Pasta','Chill Patato','Bargar']}
# print(data1)
# print(type(data1))
