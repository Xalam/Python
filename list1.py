#LIST
numbers = [10, 5, 7, 2, 1]
print("List content ", numbers)

numbers[0] = 111
print("List new content ", numbers)

numbers[2] = numbers[4]
print("List new content ", numbers)

print("\nList Length ", len(numbers))

del numbers[2]
print("New List Length ", len(numbers))
print("\nContent ", numbers)
