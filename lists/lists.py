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

# End Lesson List in Python