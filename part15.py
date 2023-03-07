# Higher Order Functions = a function that either:
#                          1. accepts a function as an argument
#                          or
#                          2.returns a function
#                          (In python,functions are also treated as objects)


#1.

def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello(func):  # higher order func because accepts a function as an argument
    text = func("Hello")
    print(text)


hello(loud)
hello(quiet)


#2.

def divisor(x): # higher order func because returns dividend func
    def dividend(y):
        return y / x
    return dividend


divide = divisor(2)
print(divide(10))