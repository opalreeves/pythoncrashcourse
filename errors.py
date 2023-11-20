# In this module, you will learn how to read and troubleshoot errors.

# One important thing to note is that when your script encounters and error, it will stop the script at the error
# This means that even if there are other errors in your code, you won't see those errors until the previous ones are resolved

# Let's look at some common errors in Python





# ---------------------------------------------------------------------------------------------- #

# PROBLEM 1: IndentationError

# One of the most common errors in Python is an IndentationError
# unlike other programming languages, indentation matters in python
# look at the following code:

x = 1
    y = 2

# VSCode is able to notify you of indentation issues with your code, and it is represented with the red squiggly line

# Run the code and read through the error carefully

# Fix the error by deleting the indent before the y, and move on.


# Indentation errors can also occur if python expects an indentation and one is not provided
# when you use conditional statements (if), loops (for/while), functions, classes, and many other procedures, you will need to indent the next content
# this indicates that the content below is part of the procedure above

if x < y:
print("hello")


# Run the code and read through the error carefully

# as you can see, the print statement should be inside of the conditional, but because it's not indented, it isn't indicated that way
# fix this by putting an indent (tab) in front of print(), and move on.







# ---------------------------------------------------------------------------------------------- #


# PROBLEM 2: SyntaxError

# Syntax errors occur when you use the wrong operators in the wrong contexts
# One of the most common examples is when you want to compare two values for equality
# This is supposed to be done with ==, however, we sometimes forget and use = instead

if x = y:
    print("they are equal")


# Run the code and read through the error carefully

# This one is easy to resolve. Simply change = to == and move on.







# ---------------------------------------------------------------------------------------------- #

# PROBLEM 3: NameError

# Name errors occur when you try to use a variable without defining it.

# This often occurs when you make a typo while referencing the variable

my_variable = 5

my_variable += 1

# Run the code and read through the error carefully

# Fix the error and move on!







# ---------------------------------------------------------------------------------------------- #

# PROBLEM 4: TypeError

# Type errors occur when you use a data type in a way that is not allowed.

# This often occurs when you try to perform math on a string number

x = "20" # this looks like an integer (number), but it's actually a string because of the "" around it

y = x / 5

# Run the code and read through the error carefully

# There are two ways we can fix this.
# Either change x = "20" to x = 20 (so it's an integer)
# Or you can cast x as an integer before performing division with it: y = int(x) / 5







# ---------------------------------------------------------------------------------------------- #

# PROBLEM 5: IndexError

# Index errors occur when you try to access an item in a list using an index that does not exist.

my_list = ["D", "A", "N"]

print(my_list[3])

# Remember that indexing of items starts at zero, so my_list[0] is "D", my_list[1] is "A", and my_list[2] is "N"
# This means that my_list[3] doesn't exist!

# Run the code and read through the error carefully

# Fix the error by changing the 3 to an index that is within range and move on








# ---------------------------------------------------------------------------------------------- #

# PROBLEM 6: ZeroDivisionError

# This is less common, but it can occur when you are programming to solve math problems or analyzing numerical data

# just like in math class, you are not allowed to divide by zero

x = 0
y = 5

z = y / x

# Run the code and read through the error carefully

# Fix the error by changing the value of x to a non zero








# ---------------------------------------------------------------------------------------------- #

# Problem 7: ValueError

# A value error occurs when you use the proper data type, but with a wrong value

# For example, as we know, int() can cast a string as an integer, so it does allow strings
# however, the string must be a numerical value. There is no way to change a word into a number using int()

int("Hello World!")

# Run this code and read through the error carefully

# Fix this error by changing "hello" to a number wrapped in quotes







# ---------------------------------------------------------------------------------------------- #


# Raising Errors

# There are sometimes situations where we may want to force an error to occur even if the code doesn't automatically find one.

# For example, let's say we have a number that is supposed to be between 1 and 100.
# If the number is lower than 1 or greater than 100, this won't cause any errors, as python handles integers much smaller and much larger

# In this case we can raise an error to force our program to crash if the number is outside of our expected values

# you can raise any error you like and add a message with it.
# In this case ValueError seems the most appropriate, so I chose that

x = 105

if x < 1 or x > 100:
    raise ValueError("The number must be between 1 and 100")

# Run the code and read through the error carefully

# Fix the error by changing x to be between 1 and 100







# ---------------------------------------------------------------------------------------------- #

# Handling Errors

# There are some situations where you actually know an error may occur and you don't want that to break your code.

# For example, let's say we have a program that gets user input doubles it.

# code: 
# user_number = input("Type a number and I'll double it: ")

# Remember that user input is always a string even if they type a number.
# This means we need to cast the user_number as an integer to perform math on it.

# code:
# user_number_as_integer = int(user_number)

# code:
# print("your number doubled is:", user_number_as_integer*2)

# okay, but what happens if the user types something that isn't a number: We'll get the same ValueError that occurred in Problem 7

# This is bad because this crashes our program.

# Instead of crashing our program, we can handle the error and allow the program to continue to run.

# we handle the error by using try: / except: clauses

# try tries to run the code inside
# if an error occurs, the code in except runs and the program continues
# we can also add an else: clause which will run if no error occurs


user_number = input("Type a number and I'll double it: ")


try: # try to run the code
    user_number_as_integer = int(user_number)
except: # if there's an error, run this code
    print("Sorry that's not a number!")
else: # if there's not an error, run this code
    print("Your number doubled is:", user_number_as_integer*2)

# test this code two different ways:
# first type hello and see what happens
# run the program again and type 7 to see what happens

# There's no error to fix for this part





# ---------------------------------------------------------------------------------------------- #


# KEY TAKEAWAYS:
# 1. Learning how to read errors is vital as a programmer, because you will always have errors in your code that need to be resolved
# 2. Sometimes errors can be raised intentionally to ensure that our program is being run correctly
# 3. Sometimes we can handle errors in order to work around them and keep the program running.




# ---------------------------------------------------------------------------------------------- #

# SUBMISSION:
# After you've fixed all of the errors, go to the assignment on Canvas and upload the file: errors.py



