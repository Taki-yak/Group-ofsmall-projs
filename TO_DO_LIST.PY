import time 

input_tasks = """
What do you want to do:
"A" => add instruction 
"R" => remove instruction
"U" => Update instruction
"S" => show my tasks 
"Q" => to quit 
"""

command_list = ["A", "R", "U", "Q", "S"]
task = []

def add_task():
    number = int(input("How many tasks are you going to add: "))
    for i in range(number):
        task_app = input("What is your task: ")
        task.append(task_app)
        print(f"Task number {i + 1} => '{task_app}' has been added")
    show_tasks() 

def update_task():
    number = int(input("Which task number do you want to update? "))
    if 0 < number <= len(task):
        task_app = input("What is your updated task? ")
        task[number - 1] = task_app
        print(f"Task number {number} => '{task_app}' has been updated")
    else:
        print("Task does not exist")
    show_tasks()  

def remove_task():
    if not task:
        print("No tasks to remove.")
        return
    task_rem = int(input("Which task number do you want to remove? ")) - 1
    if 0 <= task_rem < len(task):
        removed_task = task.pop(task_rem)
        print(f"Task '{removed_task}' has been removed.")
    else:
        print("Invalid task number.")
    show_tasks()  

def quit_app():
    print("Quitting...")
    time.sleep(2)
    exit()  

def show_tasks():
    if not task:
        print("You have no tasks.")
    else:
        print("Your tasks are:")
        for i, t in enumerate(task):
            print(f"{i + 1} => {t}")


while True:
    input_ins = str(input(f"{input_tasks}")).strip().capitalize()
    if input_ins in command_list:
        if input_ins == "A":
            add_task()
        elif input_ins == "U":
            update_task()
        elif input_ins == "R":
            remove_task()
        elif input_ins == "Q":
            quit_app()  # calling the quit function
        elif input_ins == "S":
            show_tasks()
    else:
        print("Invalid input")