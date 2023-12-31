# -*- coding: utf-8 -*-
"""to do list.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/171E3Df7xeAHpjZj3N2u1-BzAWK-DPseT
"""

# To-Do List Application

# Create an empty to-do list
todo_list = []

def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print("Task added!")

def view_tasks():
    if todo_list:
        print("To-Do List:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")
    else:
        print("Your to-do list is empty.")

def complete_task():
    view_tasks()
    task_index = int(input("Enter the task number to mark as completed: "))
    if 1 <= task_index <= len(todo_list):
        completed_task = todo_list.pop(task_index - 1)
        print(f"Completed: {completed_task}")
    else:
        print("Invalid task number.")

while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")