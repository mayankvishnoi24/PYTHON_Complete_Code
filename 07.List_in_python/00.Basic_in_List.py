## Collection
    # List
    # Tuple
    # Set
    # Dict

## List important Points:
    # Collect any type (Primitive and non-primitive) of data
    # You can repete the data elements
    # list is indexed collection
    # list is mutable collection
    # list can be copied

# l = [2,3,6.7,"Python",[6,3,"Ducat"],"Python"]
# print(l)

## Indexing the List 
# print(l[0])
# print(l[1])
# print(l[2])
# print(l[3])

# print(l[4])
# print(l[4][0])
# print(l[4][1])
# print(l[4][2])

# print(l[5])

## Slicing in List
# l = [2,3,6.7,"Python",[6,3,"Ducat"],"Python"]

# print(l[1:4:1])
# print(l[1:4])

# print(l[0:5])
# print(l[:5])

# print(l[3:6])
# print(l[3:])

# print(l[-3:])


## Operation is List
# l = [2,3,6.7,"Python",[6,3,"Ducat"],"Python"]
# l1 = [7,6+5j,True]
# print(l+l1)
# print(l*3)

# print(l>l1)
# print(l<l1)
# print(l==l1)

## Looping in list
l = [2,3,6.7,"Python",[6,3,"Ducat"],"Python"]
# for i in l:
#     print(i)

## List Method 
# l.append(5)
# print(l)

# l.insert(3,"ducat")
# print(l)

# l.extend("ducat")
# print(l)

# l.remove("ducat")
# l.remove("Python")

# l.pop(2)
# print(l.count("python"))
print(l.index(6,7))
l.clear()
l.reverse()
l2 = [3,2.8,6,9,4,2]
# l1 = []
l.sort(reverse=True)
l1=l.copy()
print(l1)