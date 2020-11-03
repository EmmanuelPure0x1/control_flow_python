# Control Flow
# if statements
# Syntax: if then condition

age = 16

if age >= 18:
    print("Welcome...")
elif age < 18:
    print("You will need to be accompanied by an adult. \nOr try a different movie...")
else:
    print("Something went wrong...")

# Create a program using control flow using if, elif, and else
# use operators ==, >=
# check age restrictions before selling ticket
# 18, 15, U, 12, PG
# else block should ensure to display message if other conditions do not match

age = input("How old are you? > ")

if int(age) > 18:
    print("You are fine")
elif int(age) <= 15:
    print("You will need an adult")
elif int(age) <= 12:
    print("You are under age")
else:
    print("input invalid")

