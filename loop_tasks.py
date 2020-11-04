# This loop is using a range of 10 to keep printing hello until hello has been prionted 10 times.
# for i in range(10):
#     print('hello')

# An empty list has been created and the for look is using a range of 10 to keep asking for names and appending the name given to the list.
list_names = []
for i in range(10):
    answer = input("Give me a name? \n > ")
    list_names.append(answer)

print(list_names)

# This for loop iterates over the prvious list and lower's the value and appends it to a new list.
list_name_lower = []
for i in list_names:
    print("A name in the list: ", i.lower(), "- Lower case.")
    list_name_lower.append(i.lower())

print(list_name_lower)


# The for look below checks to see whether the value in list_name_lower is also in list_names
for i in list_name_lower:
    if i in list_names:
        print(i, "is in other list")
    else:
        break