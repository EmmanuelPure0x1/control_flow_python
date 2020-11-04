# Loops for loop and while loop
# for loop is used to iterate through the data
# Syntax for variable_name in name_of_data_collection_variable

# Here we are declaring the the variable as a list and adding attributes to it.
shopping_list = ["eggs","milk","Supermalt"]

# This step is where we verify and check what the list holds.
print(shopping_list)

# Iterating over each item in the list.
for items in shopping_list:
# Checking if the "item" is equal to product and if it is we are printing it.
    if items == "milk":
        print(items)
    elif items == "eggs":
        print(items)
# Checking if the item is not equal to either of the suggested items and if it isn't, it prints it.
    elif items != "milk" or "eggs":
        print(items)

print("\n")

# User Dictionary created
user_dict = {
    "name":"emmanuel",
    "surname":"Ade",
    "proffesion":"trainee DevOps Engineer"
}

# Iterating over the dictionary's values using values attribute.
for values in user_dict.values():
    print(values.title())

# Iterating over the dictionary's keys and values using the items attribute.
for keys, values in user_dict.items():
    print(keys + ':', values)