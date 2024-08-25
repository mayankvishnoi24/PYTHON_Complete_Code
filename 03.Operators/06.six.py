#Identity operator : (is,is not)
## is 
# i = 5
# j = 5
# print(i == j)
# print(i is j)
# #  id()is a function to showing the  same value then same memory but value change then address will be change
# print(id(i),id(j)) ## 140712802743208 140712802743208 addressing same 

# i = [5]
# j = 5
# print(i == j)
# print(i is j)
# print(id(i),id(j)) ## 3234631487424 140712802743208 addressing was change the bulk data

## not in 
# i = [5]
# j = 5
# print(i is not j)
# print(id(i),id(j)) ## 1368843587520 140712378856360





# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is z)

# # returns True because z is the same object as x

# print(x is y)

# # returns False because x is not the same object as y, even if they have the same content

# print(x == y)

# # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

# # ----------------------------------------------------------------------------------------------------------------

# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is not z)

# # returns False because z is the same object as x

# print(x is not y)

# # returns True because x is not the same object as y, even if they have the same content

# print(x != y)

# # to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y
