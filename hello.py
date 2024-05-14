# create a list with different types of fruits
fruit = ["apples", "pears", "oranges", "peaches"]

# loop through the fruits to print the fruit names and the no of fruots in the list
for i in fruit:
    print(f"{i} is the fruit number{fruit.index(i)+1}")

# the total no of fruits in the list
print(f"there are {len(fruit)}fruits in the list")
