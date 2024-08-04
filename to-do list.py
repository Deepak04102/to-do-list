import tkinter as tk
from tkinter import messagebox
import json

FILE_PATH = 'tasks.json'

def load_tasks():
    try:
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_PATH, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task():
    task = task_entry.get()
    if task:
        tasks = load_tasks()
        tasks.append({'task': task, 'completed': False})
        save_tasks(tasks)
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def update_task_list():
    for widget in task_frame.winfo_children():
        widget.destroy()
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        status = '✓' if task['completed'] else '✗'
        tk.Label(task_frame, text=f"{i + 1}. [{status}] {task['task']}").pack()

root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

task_frame = tk.Frame(root)
task_frame.pack(pady=10)

update_task_list()
root.mainloop()