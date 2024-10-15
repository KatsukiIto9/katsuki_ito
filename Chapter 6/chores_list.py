# Create a chore list
chores = ["Dusting", "Vacuuming", "Laundry", "Dishes", "Mopping", "Organizing", "Shopping", "Cooking"]

# Unpack the first four chores in the list and display them
chore1, chore2, chore3, chore4 = chores[:4]
print("First four chores:")
print(chore1)
print(chore2)
print(chore3)
print(chore4)

# Sort the list in alphabetical order and display it (without modifying the original list)
sorted_chores = sorted(chores)
print("Sorted in alphabetical order (without modifying the original list):")
print(sorted_chores)

# Sort the list in alphabetical order and display it (modifying the original list)
chores.sort()
print("Sorted in alphabetical order (modifying the original list):")
print(chores)

# Use list comprehension to display the length of each chore in the list
chore_lengths = [len(chore) for chore in chores]
print("Length of each chore:")
print(chore_lengths)

# Use list comprehension to create and display a new list containing only chores with names that are 7 characters or less
short_chores = [chore for chore in chores if len(chore) <= 7]
print("Chores with names 7 characters or less:")
print(short_chores)
