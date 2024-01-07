# user_prompt = " Enter a todo  :   "
# todo1 = input(user_prompt)
# todo2 = input(user_prompt)
# todo3 = input(user_prompt)

# ls = [ todo1, todo2, todo3]

# print(ls)

# optimise the given code by using the python loops.


n = int(input('How many todo elements do you have for today ! '))

ls_todo = []

for i in range(0,n):
    todo = input()
    ls_todo.append(todo)


print(ls_todo)





