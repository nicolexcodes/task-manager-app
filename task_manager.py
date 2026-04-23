tasks = []

def show_menu():
  print("\nTask Manager")
  print("1. View Tasks")
  print("2. Add Task")
  print("3. Remove Task")
  print("4. Exit")

while True:
  show_menu()
  choice = input("Choose an option: ")
  
  if choice == "1":
    if not tasks:
      print("No tasks available.")
    else:
      for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
        
  elif choice == "2":
    new_task = input("Enter new task:")
    tasks.append(new_task)
    print("Task added.")
    
  elif choice == "3":
    if not tasks:
      print("No tasks to remove.")
    else:
      for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
      remove_num = int(input("Enter task number to remove: "))
      if 1 <= remove_num <= len(tasks):
        removed = tasks.pop(remove_num - 1)
        print(f"Removed: {removed}")
      else:
        print("Invalid number.")
        
  elif choice == "4":
    print("Goodbye!")
    break
    
  else: 
    print("Invalid choice.")
