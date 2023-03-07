#functions to variables

def hello():
    print("Hello")

print(hello)

hi = hello  # assign the function(hello) to a variable
hello()
hi()

say = print # assign the function(print) to a variable
say("Whoa! I can't believe this works! :o")