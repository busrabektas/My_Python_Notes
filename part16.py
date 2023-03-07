# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time,throw-away)
#lambda parameters: expression


#without lambda
def double(x):
    return x*2

print(double(5))


#wiht lambda

double2 = lambda x : x * 2
multiply = lambda x, y: x * y
full_name = lambda first_name, last_name : first_name+ " " + last_name
age_check = lambda age:True if age >= 18 else False
print(double2(7))
print(multiply(5,6))
print(full_name("Büşra", "Bektaş"))
print(age_check(12))