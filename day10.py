# Day 10 - Better To-Do App

def add_task():
    task = input("Add cheyalsina task: ")
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")
    print("Added ✅")

def show_tasks():
    print("\n--- Nee Tasks ---")
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.read()
            print(tasks if tasks else "No tasks yet!")
    except FileNotFoundError:
        print("No tasks yet!")

def delete_tasks():
    # File ni khali cheyadam = delete
    open("tasks.txt", "w").close()
    print("Anni tasks delete ayipoyayi ❌")




# Main code
add_task()
show_tasks()
delete_tasks()
