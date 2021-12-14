author = "Shprqness"
version = 1.0
beta = True

todos_list = [
    "fake todo",
    "fake todo",
    "fake todo",
    "fake todo",
    "fake todo"
]

todos = len(todos_list)

print("Learning Python\n")
print(f"Developed by {author}\n")


if beta == True:
    print("MODE: Program is currently in beta!\n")
else:
    print("MODE: Program is currently running full throttle =)")

if todos == 5:
    for x in todos_list:
        print(x)
elif todos > 5:
        print("To many todos, cannot continue.")
elif todos < 5:
        print("Less then 5 todos, system success")
