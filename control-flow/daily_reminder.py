task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
reminder = ""
match priority:
    case "high":
        reminder += f""
    case "medium":
        reminder += f""
    case "low":
        reminder += f""

if time_bound == "yes":
    reminder = "that requires immediate attention today!"
elif time_bound == "no":
    reminder = ". Consider completing it when you have free time."

print(reminder)