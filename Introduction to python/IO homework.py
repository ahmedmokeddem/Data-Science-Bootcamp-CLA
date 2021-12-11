import string
# 1- Read all of the content of the file in one variable.
file=open("./Introduction to python/student_names.txt")
content=file.read()
# 2- Write a list of random names to your file.
content+="""\nstudent T
student H
student P"""
file=open("./Introduction to python/student_names.txt",'w')
file.write(content)
# 3- Read the first n lines of the file.
n=10
file=open("./Introduction to python/student_names.txt")
print("first ",n," lines are ")
[print(line) for line in file.readlines()[:n]]
# 4- Read the last n lines of the file.
n=5
file=open("./Introduction to python/student_names.txt")
print("last ",n," lines are ")
[print(line) for line in file.readlines()[-n:]]
# 5- Check if the name x is in the file.
file=open("./Introduction to python/student_names.txt")
content=file.read()
x="student T"
print(x,"is in the file",x in content)
# 6- Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
[open(filename+".txt", "w") for filename in string.ascii_uppercase]
# to delete em
# import os
# [os.remove(filename+".txt") for filename in string.ascii_uppercase]