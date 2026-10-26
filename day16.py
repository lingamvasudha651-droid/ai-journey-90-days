def ai_progress(days):
    percent = (days / 90) * 100
    return f"You completed {percent:.1f}%"

def next_goal(current_day):
    if current_day < 30:
        return "Focus: Python Mastery"
    elif current_day < 60:
        return "Focus: ML Core"
    else:
        return "Focus: Build & Deploy"

print(ai_progress(15))
print(next_goal(15))


# Without function - bad
print("Hi JK")
print("Hi JK")
print("Hi JK")

# With function - Pro
def greet(name):
    return f"Hi {name}, Day 16 Done!"

print(greet("JK"))