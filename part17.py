# sort() method = used with lists
# sort() function = used with iterables

students = ["Squidward","Sandy","Patrick","Spongebob","Mr. Krabs"]

students.sort()  # sorts alphabetical order
for i in students:
    print(i)

print()

students.sort(reverse=True) # sorts reverse alphabetical order

for i in students:
    print(i)


print()

sorted_students = sorted(students) # sorts alphabetical order with sort func

for i in sorted_students:
    print(i)


print()

sorted_students = sorted(students,reverse=True) # sorts reverse order
for i in sorted_students:
    print (i)

#-----------------------------------------------------------------------

students2 = [("Squidward", "F", 60),
             ("Sandy", "A", 33),
             ("Patrick", "D", 36),
             ("Spongebob", "B", 20),
             ("Mr.Krabs", "C", 78)]
grade = lambda grades : grades[1] # sort based on second column
students2.sort(key=grade,reverse = True)

for i in students2:
    print(i)


print()
