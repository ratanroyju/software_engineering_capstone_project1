import datetime

# Constants
DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Function to register a new user


def register_user():
    print("Register User")
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    # Write user data to the user.txt file
    with open("user.txt", "a") as user_file:
        user_file.write(f"{username},{password}\n")

    print("User registered successfully.")

# Function to login a user


def login_user():
    print("Login")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Read user data from the user.txt file
    with open("user.txt", "r") as user_file:
        user_data = user_file.read().split("\n")
        user_data = [u for u in user_data if u != ""]

    for user_entry in user_data:
        saved_username, saved_password = user_entry.split(",")
        if username == saved_username and password == saved_password:
            print("Login successful.")
            return username

    return None

# Function to add a task


def add_task():
    print("Add Task")
    username = input(
        "Enter the username of the person the task is assigned to: ")
    task_title = input("Enter the task title: ")
    task_description = input("Enter the task description: ")
    due_date_str = input("Enter the due date (YYYY-MM-DD): ")

    # Write task data to the tasks.txt file
    with open("tasks.txt", "a") as task_file:
        task_file.write(
            f"{username};{task_title};{task_description};{due_date_str};No;No\n")

    print("Task added successfully.")

# Function to view all tasks


def view_all_tasks():
    print("All Tasks")
    with open("tasks.txt", "r") as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]

    for task_entry in task_data:
        username, task_title, task_description, due_date_str, completed, assigned = task_entry.split(
            ";")
        print(f"Assigned to: {username}")
        print(f"Title: {task_title}")
        print(f"Description: {task_description}")
        print(f"Due Date: {due_date_str}")
        print(f"Completed: {completed}")
        print(f"Assigned: {assigned}")
        print("------------------------")

# Function to view tasks assigned to the logged-in user


def view_my_tasks(username):
    print("My Tasks")
    with open("tasks.txt", "r") as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]

    tasks_assigned_to_me = [
        task_entry for task_entry in task_data if task_entry.startswith(username)]
    if not tasks_assigned_to_me:
        print("No tasks assigned to you.")
        return

    for task_entry in tasks_assigned_to_me:
        _, task_title, task_description, due_date_str, completed, assigned = task_entry.split(
            ";")
        print(f"Title: {task_title}")
        print(f"Description: {task_description}")
        print(f"Due Date: {due_date_str}")
        print(f"Completed: {completed}")
        print(f"Assigned: {assigned}")
        print("------------------------")

    # Prompt the user to select a task and perform actions
    while True:
        task_index = input(
            "Enter the index of the task you want to edit (or 'q' to quit): ")
        if task_index.lower() == "q":
            break
        try:
            task_index = int(task_index)
            if task_index >= 0 and task_index < len(tasks_assigned_to_me):
                selected_task = tasks_assigned_to_me[task_index]
                _, task_title, task_description, due_date_str, completed, assigned = selected_task.split(
                    ";")
                print("Selected Task:")
                print(f"Title: {task_title}")
                print(f"Description: {task_description}")
                print(f"Due Date: {due_date_str}")
                print(f"Completed: {completed}")
                print(f"Assigned: {assigned}")
                action_choice = input(
                    "Enter 'c' to mark the task as complete or 'e' to edit the task: ")
                if action_choice.lower() == "c":
                    selected_task = selected_task.replace("No", "Yes", 4)
                    tasks_assigned_to_me[task_index] = selected_task
                    print("Task marked as complete.")
                elif action_choice.lower() == "e":
                    new_title = input(
                        "Enter a new task title (or leave blank to keep the same): ")
                    if new_title != "":
                        selected_task = selected_task.replace(
                            task_title, new_title, 1)
                    new_description = input(
                        "Enter a new task description (or leave blank to keep the same): ")
                    if new_description != "":
                        selected_task = selected_task.replace(
                            task_description, new_description, 1)
                    new_due_date_str = input(
                        "Enter a new due date (YYYY-MM-DD) (or leave blank to keep the same): ")
                    if new_due_date_str != "":
                        selected_task = selected_task.replace(
                            due_date_str, new_due_date_str, 1)
                    tasks_assigned_to_me[task_index] = selected_task
                    print("Task updated successfully.")
                else:
                    print("Invalid choice.")
            else:
                print("Invalid task index.")
        except ValueError:
            print("Invalid task index.")

    # Write the updated task data to the tasks.txt file
    with open("tasks.txt", "w") as task_file:
        task_file.write("\n".join(task_data))

# Function to generate reports


def generate_reports():
    print("Generate Reports")

    # Read task data from the tasks.txt file
    with open("tasks.txt", "r") as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]

    # Calculate task statistics
    total_tasks = len(task_data)
    completed_tasks = sum(
        [1 for task_entry in task_data if task_entry.split(";")[4] == "Yes"])
    incomplete_tasks = total_tasks - completed_tasks
    overdue_tasks = sum([1 for task_entry in task_data if task_entry.split(
        ";")[3] < datetime.datetime.now().strftime(DATETIME_STRING_FORMAT)])

    # Write task report
    with open("task_overview.txt", "w") as task_report_file:
        task_report_file.write(f"Total tasks: {total_tasks}\n")
        task_report_file.write(f"Completed tasks: {completed_tasks}\n")
        task_report_file.write(f"Incomplete tasks: {incomplete_tasks}\n")
        task_report_file.write(f"Overdue tasks: {overdue_tasks}\n")

    # Read user data from the user.txt file
    with open("user.txt", "r") as user_file:
        user_data = user_file.read().split("\n")
        user_data = [u for u in user_data if u != ""]

    # Calculate user statistics
    total_users = len(user_data)

    # Write user report
    with open("user_overview.txt", "w") as user_report_file:
        user_report_file.write(f"Total users: {total_users}\n")

    print("Reports generated successfully.")

# Function to display statistics


def display_statistics():
    print("Display Statistics")

    # Read task report
    with open("task_overview.txt", "r") as task_report_file:
        task_report = task_report_file.read()

    # Read user report
    with open("user_overview.txt", "r") as user_report_file:
        user_report = user_report_file.read()

    # Display task report
    print("Task Report:")
    print(task_report)

    # Display user report
    print("User Report:")
    print(user_report)

# Main program


def main():
    while True:
        print("Task Manager")
        print("1. Register User")
        print("2. Login")
        print("3. Add Task")
        print("4. View All Tasks")
        print("5. View My Tasks")
        print("6. Generate Reports")
        print("7. Display Statistics")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            register_user()
        elif choice == "2":
            username = login_user()
            if username:
                while True:
                    print(f"Logged in as {username}")
                    print("1. Add Task")
                    print("2. View All Tasks")
                    print("3. View My Tasks")
                    print("4. Generate Reports")
                    print("5. Display Statistics")
                    print("6. Logout")

                    user_choice = input("Enter your choice (1-6): ")

                    if user_choice == "1":
                        add_task()
                    elif user_choice == "2":
                        view_all_tasks()
                    elif user_choice == "3":
                        view_my_tasks(username)
                    elif user_choice == "4":
                        generate_reports()
                    elif user_choice == "5":
                        display_statistics()
                    elif user_choice == "6":
                        print("Logged out.")
                        break
                    else:
                        print("Invalid choice.")
            else:
                print("Login failed.")
        elif choice == "3":
            add_task()
        elif choice == "4":
            view_all_tasks()
        elif choice == "5":
            print("Please log in to view your tasks.")
        elif choice == "6":
            print("Please log in to generate reports.")
        elif choice == "7":
            print("Please log in to display statistics.")
        elif choice == "8":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")


# Run the program
if __name__ == "__main__":
    main()
