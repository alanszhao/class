# Filename: _P09_Arrays_azha4978.py
# Author: Alan Zhao
# Date: 01/25/2016
# Purpose: Use arrays in Python

# Import module:
import random

# Two lists
list_string_fruits = ["Apple", "Banana", "Cantaloupe", "Durian", "Eggfruit", "Fig", "Grapefruit", "Honeydew", "Ita Palm",
                      "Jujube"]
list_string_animals = ["Ape", "Bear", "Caribou", "Dugong", "Emu", "Fox", "Giraffe", "Hawk", "Ibis", "Jackal"]

# Print contents of lists
print("Original contents of list_string_fruits:")
for a in range(0, 10):   # Loop through lists
    print(list_string_fruits[a])
print()   # Separation
print("Original contents of list_string_animals:")
for b in range(0, 10):   # Loop through lists
    print(list_string_animals[b])
print()   # Separation

# Slicing:
a = random.randint(0, 10)     # Generate random value
b = random.randint(2, 8)      # Generate random value
print("Slice of list_string fruits (sliced randomly):")
print(list_string_fruits[a : b])
print()
print("Slice of list_string_animals (sliced randomly):")
print(list_string_animals[a : b])
print()

# Modify two elements in lists (Using inputs and random functions)
w = random.randint(0, 10)     # Generate random value
x = random.randint(0, 10)     # Generate random value
y = random.randint(0, 10)     # Generate random value
z = random.randint(0, 10)     # Generate random value
FruitItem = input("Enter a fruit to replace one in the fruits list: ")
FruitItem1 = input("Enter another fruit to replace one in the fruits list: ")
list_string_fruits[w] = FruitItem        # Replace one index with first input answer
list_string_fruits[x] = FruitItem1  # Replace one index with second input answer
AnimalName = input("Enter an animal name to replace one in the animals list: ")
AnimalName1 = input("Enter another animal name to replace one in the animals list: ")
list_string_animals[y] = AnimalName      # Replace one index with third input answer
list_string_animals[z] = AnimalName1     # Replace one index with fourth input answer

# Print modified lists
print()           # Separation
print("Note: The fruits and animals you entered were replaced in random positions in their respective lists.")
print("MODIFIED LISTS:")
print("New contents of list_string_fruits:")
print(list_string_fruits)
print()    # Separation
print("New contents of list_string_animals:")
print(list_string_animals)

# Remove two unmodified elements:
for y in range(0, 10):
    # Check for modified elements
    if list_string_fruits[y] == FruitItem or list_string_fruits[y] == FruitItem1:
        continue
    # Remove elements
    elif list_string_fruits[y] != FruitItem and list_string_fruits[y] != FruitItem1:
        list_string_fruits.remove(list_string_fruits[y])
        if len(list_string_fruits) == 8:     # Check for 2 removed elements
            break       # Loop escape
for z in range(0, 10):
    # Check for modified elements
    if list_string_animals[z] == AnimalName or list_string_animals[z] == AnimalName1:
        continue
    # Remove elements
    elif list_string_animals[z] != AnimalName and list_string_animals[z] != AnimalName1:
        list_string_animals.remove(list_string_animals[z])
        if len(list_string_animals) == 8:      # Check for 2 removed elements
            break    # Loop escape
print()    # Separation
print("Note: The removed lists were generated at random.")
print("REMOVED ITEMS LISTS:")
print("Contents of list_string_fruits:")
print(list_string_fruits)
print()   # Separation
print("Contents of list_string_animals:")
print(list_string_animals)
print()   # Separation

# Append Elements (Input Statements):
FruitAppend1 = input("What fruit would you like to append into list_string_fruit? ")
FruitAppend2 = input("Enter another fruit you would like to append into list_string_fruit: ")
AnimalAppend1 = input("What animal would you like to append into list_string_animals? ")
AnimalAppend2 = input("Enter another animal you would like to append into list_string_animals: ")

# Append inputs to their respective lists
list_string_fruits.append(FruitAppend1)
list_string_fruits.append(FruitAppend2)
list_string_animals.append(AnimalAppend1)
list_string_animals.append(AnimalAppend2)

# Print appended lists
print()
print("Note: The items you entered above were appended at the end of the list.")
print("APPENDED LISTS:")
print("New contents of list_string_fruits:")
print(list_string_fruits)
print()   # Separation
print("New contents of list_string_animals:")
print(list_string_animals)
print("--------------------------------------------------------------------------------")   # Separation

# New list
StatesList = ["Wyoming", "New Mexico", "Utah", "Oregon", "Colorado", "Arizona", "Idaho", "California"]

# Print original contents
print()
print("Contents of StatesList:")
for num in range(0, 8):
    print(StatesList[num])
print()    # Separation

# Print sorted list contents
print("SORTED LIST CONTENTS:")
StatesList.sort()
for number in range(0, 8):
    print(StatesList[number])








