def main():
    tasks = []

    while True:
        print("\n To-Do List App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter a new task: ")
            tasks.append(task)
            print("Task added.")
        elif choice == '2':
            if not tasks:
                print("No tasks found.")
            else:
                print("\nTo-Do List:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
        elif choice == '3':
            if not tasks:
                print("No tasks to delete.")
            else:
                index = int(input("Enter the number of the task to delete: ")) - 1
                if 0 <= index < len(tasks):
                    tasks.pop(index)
                    print("Task deleted.")
                else:
                    print("Invalid task number.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
