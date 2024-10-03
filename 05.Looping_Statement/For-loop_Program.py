### Loop Exercise

# 1. check the prime no given from the user

# n = 11
# count = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         count += 1
#         # print(count) ## This is for showing the factors

# if count == 2:
#     print(n, "is prime")
# else:
#     print(n, "is not prime")


# 2. Accept n number from user and calculate the sum of all number between 1 and n including n


# 3. Display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration


# 4. Given a number count the total number of digits in a number


# 5. Calculate the Sum of Natural Numbers


# 6. Find Factorial of a Number

# n = 13
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)


# 7. Generate Multiplication Table

# n = 2
# for i in range(1, 11, 1):
#     # print(n*i)
#     print(n, "*", i, "=", n * i)


# 8. Write a Python program to get the Fibonacci series between 0 to 50.
#    Note : The Fibonacci Sequence is the series of numbers :
#    0, 1, 1, 2, 3, 5, 8, 13, 21, ....
#   Every next number is found by adding up the two numbers before it.
#   Expected Output : 1 1 2 3 5 8 13 21 34


# 9. Find GCD of two Numbers


# 10. Find LCM of two Numbers


# 11. Display Characters from A to Z Using Loop


# 12. Reverse a Number


# 13. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).


# 14. Write a Python program to guess a number between 1 to 9.
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.


# 15. Write a Python program to construct the following pattern, using a nested for loop.

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


# 16. Write a Python program that accepts a word from the user and reverse it.


# 17. Write a Python program to count the number of even and odd numbers from a series of numbers.
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4


# 18. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5


# 19. Write a Python program that accepts a string and calculate the number of digits and letters.


# 20. Write a Python program to check the validity of password input by users.
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.


# 21. Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number.
# The numbers obtained should be printed in a comma-separated sequence.


# for i in [1,2,3,4,5,6,7,8,9,10]:
#     print(i+2,end=" ")
#     print(i-2,end=" ")
#     print(i*2,end=" ")
#     print(i/2,end=" ")

# for i in "Mayank":
#     print(i.upper())

# for i in range(0,10,1):
#     print(i)


## Series in the form of a list

# s = 0
# for i in [1, 3, 45, 6, 78, 3, 2]:
#     s = s + i
# print("Sum",s)


## find out the aggregate the multiplication of a same list

# m = 0
# for i in [1, 3, 45, 6, 78, 3, 2]:
#     m = i * m
# print("Multiplication",m)


## Break Statement -- iteration are break on the stop loop

# s=0
# for i in [1,2,3,4,0,5,6,7,8]:
#     if i == 0:
#         break
#     s=s+i
# print(s)

## Continue Statement -- skip the iteration then next value

# for i in [1,2,3,4,5,6,7,8]:
#     if i==3:
#         break
#     print(i)


## Skipping the negitive value 
# s = 0
# for i in [1, 2, 3, -4, 0, -5, 6, -7, 8]:
#     if i < 0:
#         continue
#     s = s + i
    
# print(s)


## (1,2,3,4,5,6,7,8,9,10)
# s=0
# for i in (1,2,3,4,5,6,7,8,9,10):
#     if i%2!=0:
#         continue
#     s=s+i
# print(s)


## nested for loop 

# for i in range(1,11,1):
#     for j in range(1,11,2):
#         print("i=",i,"j=",j)


## Sum of a list 
# s=0
# for i in [[1,2,3],[4,5,6],[7,8,9]]:
#     for j in i:
#         s=s+j
#         # for k in j:
# print(s)

# the End