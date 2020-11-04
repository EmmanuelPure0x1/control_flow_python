from datetime import date
from time import sleep

age = 26
name = "Emmanuel"
birthday = (1989,6,12)

d1 = (date.today())

print("you're born" + birthday - d1)
print("OMG {}, you are {} years old so you were born in {}".format(name, age, birthday))

sleep(1)
name = input("How old are you? > ")
sleep(1)
age = input("How old are you? > ")
sleep(1)
