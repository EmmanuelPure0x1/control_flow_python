# Control Flow

## if, elif, else statements

### For loops and while loops

- A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
- With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

### While Loops

- while loops are a ```continuous``` loop until a target or a mission is achieved.
- Until a condition is met it will keep running.
- Used for ```monitoring```.
- It is not regularly used.
- ```break``` and ```continue``` assist with the flow of while loops

```python
number = 0

while number < 10:
     print(f"it's working -> {number}")
     if number == 5:
         break
     number += 1
```
- While-loop taking user input
```python
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
```