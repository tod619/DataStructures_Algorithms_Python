# Start: Lesson list in Python
# Create a list
my_list = [1, 5, 10, 4]

# Random indexing allows us to access the items in the list in constatn time big N (1)
print(my_list[1])

# Accessing each item in the list is done in big O (N)
for item in my_list:
    print(item)

# Delete an item from the list
del my_list[0]
print(my_list)

# End: Lesson List in Python

# Start: Lesson Advanced Operations
# Appending item at the end is big O (1)
my_list.append("New Item added to the end")
print(my_list)

# Access the end of the list using - 
# -1 index access the last item in the list
print(my_list[-1])

# Print a range of items seperate using :
# Includes the first item but excludes the second item
print(my_list[0:3])

# Prints the entire list
print(my_list[:])

# Prints everything up to the last item but does not includ the last itme
print(my_list[:-1])

# Reverses the list
print(my_list[::-1])

# Lists can be added together
list1 = ["List1", 5, 7, 10.9]
list2 = ["list2", 23, 45, 9.4]
result = list1 + list2
print(result)
# End: Lesson Advanced Operations