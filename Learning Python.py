author = "Shprqness"
version = 1.0
beta = True

todos = 5

# TODO List
todo1 = "fake todo"
todo2 = "fake todo"
todo3 = "fake todo"
todo4 = "fake todo"
todo5 = "fake todo"



print("Learning Python")
print("               ")
print("Developed by ", author)
print("       ")





# if else

if beta == True:
    print("MODE: Program is currently in beta!")
else:
    print("MODE: Program is currently running full throttle =)")

if todos == 5:
    print(todo1)
    print(todo2)
    print(todo3)
    print(todo4)
    print(todo5)
else:
    if todos > 5:
        print("To many todos, cannot continue.")
    if todos < 5:
        print("Less then 5 todos, system success")