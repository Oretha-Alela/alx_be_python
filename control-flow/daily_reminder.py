# Ask for user input"

task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ")

time_bound = input("Is it time-bound? (yes/no): ")

# React differently bassed on priority

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is a high priority task. Consider completing it when done with time-bound tasks")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task that requires attention in due time")
        else:
            print(f"Reminder: {task} is a medium priority task. Consider completing it when done with high priority tasks")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is a low priority task.Consider doing it when the time comes.")
        else:
            print(f"{task} is a low priority task. Consider completing it when you have free time.")

