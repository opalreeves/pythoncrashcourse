# make sure todos.txt exists
# read to-dos from todos.txt as a list of strings. Each line should have its own element in the list. 
try:
    with open("todos.txt", "r") as f:
        content = f.read()
        todo_list = content.split("\n")
except FileNotFoundError:
    with open("todos.txt", "w") as f:
        f.write("")

remaining_todo_list = []

for todo in todo_list:
    print(todo)
    user_input = input("Completed? (y/n)")
    if user_input != "y":
        remaining_todo_list.append(todo)

while True:
    new_todo = input("Add todo (q to quit): ")
    if new_todo == "q":
        break
    else:
        remaining_todo_list.append(new_todo)

with open("todos.txt", "w") as f:
    output = "\n".join(remaining_todo_list)
    f.write(output)

# for loop through the list (read each element one at a time)
    # print the to-do
    # ask the user if they completed this
        # yes: remove
        # no: keep it

# ask if they want to add more to the to-do list:
# while loop
    # ask for more todos
    # if they input "q",
        # quit out with "break"
    # else
        # add to the to-do list

# write new to-dos to file