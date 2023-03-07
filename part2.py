#*args= parameter that will pack all arguments into a tuple
#       useful so that a function can accept a varying amount of arguments


def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6))

def add(*stuff):
    sum=0
    stuff = list(stuff) #turn the tuple to list
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5,6))

# **kwargs = parameter that will pack all arguments into a dictionary----------------------
#            useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs):
    # print("Hello" + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end = " ")
    for key, value in kwargs.items():
        print(value,end=" ")

hello(title ="Mr.",first="Bro",middle="Dude",last="Code")
print()

# str.format() = optional method that gives users-----------------------------------------
#                more control when displaying output

animal = "cow"
item = "moon"

#print("The " + "animal" + "jumped over the " + item)

print("The {} jumped over the {} ".format(animal,item))
print("The {1} jumped over the {1} ".format(animal,item))
print("The {animal} jumped over the {animal} ".format(animal="cow",item="moon"))

text = "The {} jumped over the {}"
print(text.format(animal,item))

name = "Büşra"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}.Nice to meet you".format(name)) # 10 spaces after the name
print("Hello, my name is {:<10}.Nice to meet you".format(name)) # left aligned
print("Hello, my name is {:>10}.Nice to meet you".format(name)) # right aligned
print("Hello, my name is {:^10}.Nice to meet you".format(name)) # center aligned


number = 3.14159

print("The number pi is {:.2f}".format(number)) # only first two digits after the decimal number

number2 = 1000

print("The number is {:,}".format(number2))
print("The number is {:b}".format(number2)) # binary representation of the number
print("The number pi is {:o}".format(number2)) # octal
print("The number pi is {:X}".format(number2)) # hexadecimal
print("The number pi is {:E}".format(number2)) # scientific notation


# random module-------------------------------------------------------------------

import random

x = random.randint(1,6)
y = random.random() #float number
print(x)
print(y)

myList = ['rock','paper','scissors']
z = random.choice(myList) #return random element from a list
print(z)

cards = [1,2,3,4,5,6,7,8,9,"J","K","A"]
random.shuffle(cards) #takes a sequence, like a list, and reorganize the order of the items
print(cards)

#exception = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by 0 idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
except Exception as e:
    print(e)
    print("something went wrong :( ")
else:
    print(result)
finally:
    print("This will always execute")


























