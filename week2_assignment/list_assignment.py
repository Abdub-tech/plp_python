# Week 2 Assignment - List Operations

# 1. Create an empty list called my_list
my_list = []

# 2. Append elements: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# 3. Insert the value 15 at the second position (index 1)
my_list.insert(1, 15)

# 4. Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# 5. Remove the last element
my_list.pop()

# 6. Sort my_list in ascending order
my_list.sort()

# 7. Find and print the index of the value 30
index_of_30 = my_list.index(30)
print("The index of 30 is:", index_of_30)

# Print final list for clarity
print("Final my_list:", my_list)
