# Create a shopping list
shopping_items = ["Milk", "Bread", "Eggs", "Butter", "Cheese", "Tomatoes", "Lettuce", "Chicken"]

# Unpack the first four items in the list and display them
item1, item2, item3, item4 = shopping_items[:4]
print("First four items:")
print(item1)
print(item2)
print(item3)
print(item4)

# Sort the list in alphabetical order and display it (without modifying the original list)
sorted_items = sorted(shopping_items)
print("Sorted in alphabetical order (without modifying the original list):")
print(sorted_items)

# Sort the list in alphabetical order and display it (modifying the original list)
shopping_items.sort()
print("Sorted in alphabetical order (modifying the original list):")
print(shopping_items)

# Use list comprehension to display the length of each item in the list
item_lengths = [len(item) for item in shopping_items]
print("Length of each item:")
print(item_lengths)

# Use list comprehension to create and display a new list containing only items with names that are 5 characters or less
short_items = [item for item in shopping_items if len(item) <= 5]
print("Items with names 5 characters or less:")
print(short_items)
