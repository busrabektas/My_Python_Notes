import os

#file detection
path = "C:\\Users\\Büşra\\Desktop\\folder"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exists!")

print()

#read a file---------------------------------------------

try:
    with open('test.txt') as file:
         print(file.read())
except FileNotFoundError:
    print("That file was not found :(")

#write a file--------------------------------------------

text = "Yooooooo\nThis is some text\nHave a good one!\n"
text2 = "Have a nice day! See ya"
with open('test2.txt','w') as file:
    file.write(text)

with open('test2.txt','a') as file: # a = append a file
    file.write(text2)

#copy a file----------------------------------------------

import shutil

shutil.copyfile('test2.txt','copy.txt') #sourc,destination
print()

#move a file----------------------------------------------

source = "newText.txt"
destination = "C:\\Users\\Büşra\\Desktop\\newText.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+ " was moved ")
except FileNotFoundError:
    print(source + " was not found")

#delete a file----------------------------------------------

# create a text file called test3
try:
    os.remove('test3.txt')
except FileNotFoundError:
    print("That file was not found")


