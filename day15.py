# Example: Student data
student = {
  "name": "JK",
  "days_completed": 14,
  "goal": "AI Engineer"
}

print(student["name"])
print(student["days_completed"])

# Add new
student["streak"] = "14 days"

profile ={
    "name":"vasudha",
    "age":19,
    "profession":"AI Engineer"
}
print(profile["name"])
print(profile["profession"])

profile["skills"]="python"

# Nee AI journey ni dict ga marchu
my_journey = {
  "day": 15,
  "topic": "Dictionary",
  "completed": ["python basics", "list", "tuple", "set"],
  "next": "functions"
}

for key, value in my_journey.items():
    print(f"{key} -> {value}")
