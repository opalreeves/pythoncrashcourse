# Complete this before the LeetCode assignment # 3
# Linked Lists seem fairly complex, but the concept is actually quite simple.
# Linked Lists consists of nodes. Each node has a value or data property as well as a next property.
# The "next" property points to another node.
# When the list reaches it's end, the "next" property is None
# Let's look at how we can make a Node object (with python classes)

class Node:
    def __init__(self, x):
        # when a node is created, a value must be assigned
        self.val = x
        # by default, the "next property is 'None'. This can be reassigned if the linked list is continuing
        self.next = None


# the first node in a linked list is often called a 'head'
# The head has a value of 10
head = Node(10)

# to add a new node, simply assign head.next to a new node
head.next = Node(5)

# we can continue adding more nodes with more nexts!
head.next.next = Node(2)
head.next.next.next = Node(-5)
head.next.next.next.next = head

# Everything from the head node to the final node is now connected

# to iterate through a linked list, a "while" loop is often used.
# the "while" loop will continue until the end of the linked list is reached

current_node = head # start by setting the current node to the first node in the linked list (the head)

# this loop will continue until it reaches the end of the linked list
while current_node is not None:
    print(current_node.val) # print the value of the node
    current_node = current_node.next # reassign the current node to the next node

# try running this, and see what prints 

# You know know what a linked list looks like, what a basic node object looks like, how to add more nodes to a linked list, and how to iterate through a linked list.


# BREAK IT!

# NOTE: Make sure you know how to stop a script if it is infinitely looping
# You can press ctrl+c in the output terminal, or press the stop sign (the red box near where the play button was)

# after head.next.next.next = Node(-5) add a new line that says:
# head.next.next.next.next = head
# What do you think will happen when you run the script now?
# Try running the script.
# Pretty cool right? Why did that happen?

