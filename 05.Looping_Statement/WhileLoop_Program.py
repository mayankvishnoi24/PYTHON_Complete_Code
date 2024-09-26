# # Display the multiplication table of a number

# n = int(input("enter the value: "))
# i = 1
# while i<=10:
#     print(n,"*",i,"=",n * i)
#     i+=1


# ## Display even table
# n = int(input("enter the value: "))
# i = 2
# while i<=10:
#     print(n,"*",i,"=",n * i)
#     i+=2

# n = int(input("enter the value: "))
# i = 1
# while i<=10:
#     if i%2==0:
#         print(n,"*",i,"=",n * i)
#     i+=1

# # Display the factors of a numbers

# n = int(input("enter the value: "))
# i = 1
# while i<=n:
#     if n%i==0:
#         print(i,end=" ")
#     i+=1

# # Display a number is prime or not

# n = int(input("enter the value: "))
# i = 1
# count = 0
# while i<=n:
#     if n%i==0:
#         count += 1
#     i+=1
# # print(count)
# if count==2:
#     print(n,"is prime")
# else:
#     print(n,"is not prime")

# # Display the sum of a series
# 1,2,3,4,5,6,7,8,9,10

# n = 10
# i = 1
# s = 0
# while i<=n:
#     s=s+i
#     i+=1
# print(s)

# 1,2,4,8,16,32,64,128

# i = 1
# s = 0
# while i<=128:
#     s=s+i
#     i=i*2

# print(s)

# # Reverse series

# i = 128
# s = 0
# while i>=1:
#     s=s+i
#     i=i/2

# print(s)

# # Multipy of a series
# 1,2,3,4,5,6

# n = 6
# i = 1
# m = 1
# while i<=n:
#     m=i*m
#     i+=1
# print(m)

# # Sum of 5 user input nos. Through Loop

# i = 1
# s = 0
# while i<=5:
#     n = int(input("enter the no.: "))
#     s = s+n
#     i+=1
# print("Total Sum:",s)

# # Break Statement

# i = 1
# while i <= 10:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# # Continue Statement

# i = 1
# while i <= 10:
#     if i == 3 or i == 5 or i == 8:
#         continue
#     print(i)
#     i += 1  This is infinite loop

# i = 0
# while i < 10:
#     i += 1
#     if i == 3 or i == 5 or i == 8:
#         continue
#     print(i)


# # Skip the -ve value in sum process of 5 input number

# i = 1
# s = 0
# while i <= 5:
#     i += 1
#     n = int(input("enter number: "))
#     if n < 0:
#         continue
#     s = s + n

# print("Sum: ", s)

# # else block with while loop

# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# else:
#     print("Alright Done")


# i = 1
# while i <= 10:
#     print(i)
#     if i == 5:
#         break
#     i += 1
# else:
#     print("Alright Done")


# # guess a number 1-9

# i = 1
# LuckyNo = 23
# while i <= 3:
#     g = int(input("enter any no.: "))
#     if g == LuckyNo:
#         print(g, "Right Guess")
#         break
#     else:
#         print(g, "Wrong Guess")
#     i += 1
# else:
#     print("Your all Attempts are Failed..")


# # nested Loop

# i = 1
# while i <= 5:
#     j = 1
#     while j <= 5:
#         print("i=", i, "j=", j)
#         j += 1
#     i += 1


