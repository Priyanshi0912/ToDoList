import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, name, due_date, priority):
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.completed = False

def add_task():
    name = entry_name.get()
    due_date = entry_due_date.get()
    priority = entry_priority.get()

    if name and due_date and priority:
        new_task = Task(name, due_date, priority)
        tasks.append(new_task)
        list_tasks.insert(tk.END, f"{new_task.name} - Due: {new_task.due_date} - Priority: {new_task.priority}")
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Please fill in all fields.")

def mark_completed():
    selected_task_index = list_tasks.curselection()
    if selected_task_index:
        selected_task = tasks[selected_task_index[0]]
        selected_task.completed = True
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Please select a task.")

def delete_task():
    selected_task_index = list_tasks.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Please select a task.")

def update_task_list():
    list_tasks.delete(0, tk.END)
    for task in tasks:
        status = "Completed" if task.completed else "Not Completed"
        list_tasks.insert(tk.END, f"{task.name} - Due: {task.due_date} - Priority: {task.priority} - {status}")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_due_date.delete(0, tk.END)
    entry_priority.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")

root.configure(bg='lightgray')

tasks = []

label_name = tk.Label(root, text="Task Name:", bg='lightgray')
label_name.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_due_date = tk.Label(root, text="Due Date:", bg='lightgray')
label_due_date.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
entry_due_date = tk.Entry(root)
entry_due_date.grid(row=1, column=1, padx=10, pady=5)

label_priority = tk.Label(root, text="Priority:", bg='lightgray')
label_priority.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
entry_priority = tk.Entry(root)
entry_priority.grid(row=2, column=1, padx=10, pady=5)

# Buttons
button_add = tk.Button(root, text="Add Task", command=add_task, bg='lightblue')
button_add.grid(row=3, column=0, columnspan=2, pady=10)

button_completed = tk.Button(root, text="Mark Completed", command=mark_completed, bg='lightgreen')
button_completed.grid(row=4, column=0, columnspan=2, pady=5)

button_delete = tk.Button(root, text="Delete Task", command=delete_task, bg='salmon')
button_delete.grid(row=5, column=0, columnspan=2, pady=5)

list_tasks = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=50)
list_tasks.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

list_tasks.configure(bg='white')

root.mainloop()
