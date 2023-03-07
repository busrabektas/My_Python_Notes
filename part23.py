# zip(*iterables) = aggregate elements from two or more iterables (list, tuples,sets,etc.)
#                   creates a zip object with paired elements stored in tuples for each element

usernames= ("Dude", "Bro", "Mister")
passwords = ("p@ssword", "abc123", "guest")


users = dict(zip(usernames, passwords))

print(type(users))

for key,value in users.items():
    print(key+" : "+value)