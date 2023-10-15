# Here are a few things that might help you with the "strings" leetcode assignment.

# 1. Strings can be iterated through like a list.

my_string = "The quick brown fox jumps over the lazy dog."

# we often iterate using 'c' as the variable for the iterator
# this is because c represents a character in the string
for c in my_string:
    print(c)

# another thing we can do with strings is replace characters within the string.
my_string_2 = my_string.replace("t", "s")

# When you reach this, uncomment the next line so you can see it print out
# print("my_string_2:",my_string_2)

# notice that the "T" did not get replaced, this is because character "T" is not the same as character "t" in programming.
# upper case and lower case characters are not equal to each other.

# .replace does not change the original string, so there needs to be a new string assigned.
# if we want to change the original string, we need to reassign it to the replaced value.

my_string = my_string.replace("o","a")

# When you reach this, uncomment the next line so you can see it print out
# print("my_string:", my_string)

# This replaced every instance of "o" with "a".
# What if we only one to replace one instance?
# .replace can take a third argument indicating the number that you would like to change

my_string = my_string.replace("a","e",1)

# When you reach this, uncomment the next line so you can see it print out
# print("my_string:", my_string)

# as you can see only the first instance was replaced.

# We can even replace characters with nothing, which essentially deletes them from the list.

new_string = "an assassin sins"
new_string = new_string.replace("s","") # replace all s's with nothing

# When you reach this, uncomment the next line so you can see it print out
# print("new_string:", new_string)


# BREAK IT!
# What happens when you try to replace a letter than doesn't exist in a string?
# For example, if you have a string as "hello", and you replace the letter "s" with "t"
# Does this cause an error? What happens?

