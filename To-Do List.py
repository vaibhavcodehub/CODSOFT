import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = entry.get()
    if task:
        var = tk.BooleanVar()
        cb = tk.Checkbutton(task_frame, text=task, variable=var,
                            font=("Arial", 12), bg="#FFF1B6", anchor="w", padx=10)
        cb.var = var
        cb.pack(fill="x", pady=4)
        tasks.append(cb)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to clear all tasks
def clear_tasks():
    for task in tasks:
        task.destroy()
    tasks.clear()

# Function to edit a selected task
def edit_task():
    for task in tasks:
        if task.var.get():
            new_text = entry.get()
            if new_text:
                task.config(text=new_text)
                entry.delete(0, tk.END)
                return
            else:
                messagebox.showwarning("Input Error", "Please enter the new task text.")
                return
    messagebox.showinfo("Edit Task", "Please check a task to edit.")

# Main Window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x520")
root.config(bg="#F26522")
root.resizable(False, False)

tasks = []

# Title
title = tk.Label(root, text="To-Do List", font=("Arial Rounded MT Bold", 22),
                 bg="#FECB4F", fg="#D94B1D", pady=10)
title.pack(fill="x", pady=(20, 10), padx=20)

# Input Area Frame
input_frame = tk.Frame(root, bg="#FECB4F", padx=10, pady=10)
input_frame.pack(padx=20, pady=(0, 10), fill="x")

# Entry Field
entry = tk.Entry(input_frame, font=("Arial", 14), bg="#FFF1B6", fg="black", relief="flat")
entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

# Add Button
add_button = tk.Button(input_frame, text="+", font=("Arial", 16, "bold"),
                       bg="#1E90FF", fg="white", relief="flat", command=add_task, width=3)
add_button.pack(side="right")

# Task Display Frame
task_frame = tk.Frame(root, bg="#FFF1B6", bd=2, relief="groove")
task_frame.pack(padx=20, pady=10, fill="both", expand=True)

# Button Frame
button_frame = tk.Frame(root, bg="#F26522")
button_frame.pack(pady=10, padx=20, fill="x")

# Edit Button
edit_button = tk.Button(button_frame, text="Edit", font=("Arial", 12, "bold"),
                        bg="#F89B1F", fg="white", width=10, relief="flat", command=edit_task)
edit_button.pack(side="left", padx=10)

# Clear Button
clear_button = tk.Button(button_frame, text="Clear", font=("Arial", 12, "bold"),
                         bg="#D94B1D", fg="white", width=10, relief="flat", command=clear_tasks)
clear_button.pack(side="right", padx=10)

root.mainloop()
