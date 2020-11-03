# Loops for loop and while loop
# for loop is used to iterate through the data
# Syntax for variable_name in name_of_data_collection_variable

shopping_list = ["eggs","milk","Supermalt"]
print(shopping_list)

for items in shopping_list:
    if items == "milk":
        print(items)
    elif items == "eggs":
        print(items)
    elif items != "milk" or "eggs":
        print(items)