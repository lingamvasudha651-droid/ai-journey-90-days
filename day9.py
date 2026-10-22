# Day 9 - My To-Do App
task = input("Nee task enti?: ")

# 1. Save cheyadam
with open("tasks.txt", "a") as f:
    f.write(task + "\n")

print("Task saved! ✅")

# 2. Chupinchadam
print("\nNee motham tasks:")
with open("tasks.txt", "r") as f:
    print(f.read())