task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        print(f"Reminder: '{task}' is a {priority} priority task ", end ="")
    case "medium":
        print(f"Note: '{task}' is a {priority} priority task. ", end ="")
    case "low":
        print(f"Note: '{task}' is a {priority} priority task. ", end ="")

if time_bound == "yes":
    print("that requires immediate attention today!")
elif time_bound == "no":
    print("Consider completing it when you have free time.")
    
