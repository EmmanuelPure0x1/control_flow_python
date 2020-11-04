# While loop creation
# break and continue are key words that we can use to control the flow of our program
# Syntax: while variable_name condition value:

# number = 0
#
# while number < 10:
#     print(f"it's working -> {number}")
#     if number == 5:
#         break
#     number += 1

# take user input with while loop

user_prompt = True

while user_prompt:
    age = input("Please enter your age > ")
# Note this user input is within our while loop therefore it'll keep prompting the uer until we get a number under 117
    if age.isdigit() and int(age) < 117:
    #isdigits() checks if the input is all digits
        user_prompt = False
    else:
        print("Please provide age in digits")

print(f"Your age is {age}")


# isdigit() checks if the input is all digits
