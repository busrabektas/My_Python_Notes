import math

#string methods

name = "Büşra"

print(len(name))  # length of the string
print(name.find("r")) #index of the letter
print(name.capitalize()) # capitalized
print(name.upper()) # uppercase
print(name.lower()) #lowercase
print(name.isdigit()) #if it is number true
print(name.isalpha()) #The isalpha() method returns True if all the characters are alphabet letters (a-z).
print(name.count("ü")) #how many "ü" it has
print(name.replace("ü","ö"))
print(name*3) #diplay it three times

#type casting = convert the data type of a value to another data type

x = 1 #int
y = 2.0 #float
z = "3" #str

x= str(x)

print(int(y))
print(str(x))
print(type(x))

#user input

#name = input("What is your name: ")
#print("Hello my name is " + name )
#age = int(input("How old are you?: "))
#print("I am " + age + " years old")

#math functions

pi = 3.14
print(round(pi))
print(math.ceil(pi)) #Round a number upward to its nearest integer
print(math.floor(pi)) #Round numbers down to the nearest integer
print(abs(pi)) #The Python abs() function return the absolute value and remove the negative sign of a number in Python.Jul 25, 2022
print(pow(pi,2))
print(math.sqrt(pi))
print(max(3,2))


#slicing = create a substring by extracting elements from another string indexing[] or slice [start:stop:step]


