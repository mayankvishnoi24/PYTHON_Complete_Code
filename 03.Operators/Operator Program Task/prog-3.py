# 3. write a program to calulate the total marks and percentage(out of 300) of student input test marks in English,math and Science.

Eng = int(input("Enter the english marks: "))
math = int(input("Enter the math marks: "))
sci = int(input("Enter the science marks: "))

mark = Eng + math + sci

percentage = mark/300*100
print("Student Marks:",mark)
print("Student Percentage:",percentage)