task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a {priority} priority task "
    case "medium":
        reminder = f"Note: '{task}' is a {priority} priority task. "
    case "low":
        reminder = f"Note: '{task}' is a {priority} priority task. "

if time_bound == "yes":
    print("that requires immediate attention today!")
elif time_bound == "no":
    print(reminder)
    
