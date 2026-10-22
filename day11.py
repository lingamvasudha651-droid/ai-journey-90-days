# Day 11 - Lists intro

tasks = []

# Tasks add cheyadam
tasks.append("Learn Python")
tasks.append("Build AI Project")
tasks.append("Push to GitHub")
tasks.append("Gym ki vellali")
tasks.append("diet follow avvali")

print("Nee tasks:", tasks)
print("First task:", tasks[0])
print("Total tasks:", len(tasks))


# Loop tho chupinchadam - idi AI lo daily use chestam
for t in tasks:
    print(f"- {t}")