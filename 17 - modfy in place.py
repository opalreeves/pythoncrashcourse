
# what is the difference between these two functions?

list_1 = [5,8,4,3,2,5]
list_2 = [5,8,4,3,2,5]

sorted(list_1)
list_2.sort()

print("list_1", list_1)
print("list_2", list_2)

# if you run this, you'll see that list_1 is not sorted, but list_2 is!

# this is because .sort() modifies the list in place, meaning it changes the value of the original list_2.

# sort(list_1) does not modify list_1 in any way. It returns a sorted list, meaning we have to assign the returned value to a new variable

# for example:

list_3 = sorted(list_1)
print("list_3", list_3)


# .sort() actually returns nothing

list_4 = list_1.sort()
print("list_4",list_4)

# this is why list_4 prints None
# but, hey, now if I print list_1, It'll be sorted!

print("list_1 (again)", list_1)


# but so what? if I want, I can just reassign the sorted list back to itself in Python, right?

list_5 = [2,5,1,0,8]
list_5 = sorted(list_5)
print("list_5", list_5)

# This is true, so most of the time it doesn't matter. However, it DOES matter this week, because your leetcode problem: Merge Sorted Array requires you to modify the list in place:
# "Do not return anything, modify nums1 in-place instead."

# this means that if we reassign, nums1 to something else, the original nums1 that was passed will be unmodified. It's kind of weird, but that's part of programming.
# you'll learn a lot more about this when you learn Object Oriented Programming as well as memory and pointers.
# For now, just remember that when something asks you to modify a variable in place, it's important to only use specific functions that modify in place.

# There are several other functions that modify lists in place which may be helpful for solving this week's problem.

# For example, we can add a new value to a list using .append()

list_6 = [1,2,3,4]
list_6.append(5)

print("list_6", list_6)

# If we want to append one list to another one, we need to use extend().

list_7 = [0,1,2,3]
list_8 = [4,5,6]
list_7.extend(list_8)
print("list_7", list_7)

# this actually does nothing to list_8

print("list_8", list_8)

# another thing we can do is pop() the last element from a list.
# pop() actually returns the value that was popped off.

list_9 = ["The","quick","brown","fox","jumps","over","the","lazy","dog"]
last_word = list_9.pop()
second_to_last_word = list_9.pop()

print("list_9", list_9)
print("last_word:", last_word)
print("second_to_last_word:", second_to_last_word)

# if we don't need to know what value was popped, we can simply pop() without assigning it to anything

list_9.pop()

print("list_9 again", list_9)


# pop(), and extend() should be enough to solve this week's problem, however, python has a hack that allows you to reassign a list in place
# by putting [:] after the list, it overwrites all of the values in the list in place.

list_10 = [4,5,8,9]
 
list_10 = sorted(list_10) # this does not modify the list in place

list_10[:] = sorted(list_10) # this does modify the list in place

# once again, the difference between the two is not super relevant in most cases, but a lot of leetcode problems require you to modify variables in place, so having several different tools available to do so will help you solve a lot of these problems.
# always look out for the terms "modify in-place" to know when you need to rethink the problem and use in-place modification functions

# BREAK IT!
# What happens if you use append() instead of extend() when combining two lists? It shouldn't throw an error, but the results are ugly...