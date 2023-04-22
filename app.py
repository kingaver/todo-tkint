import tkinter as tk

def addtask(task_string, tasks):
    tasks.append(task_string.get())
    task_string.set('')
    Tasks.set(tasks)

def delete(event):
    tasks_length = len(tasks)
    current_idx = lb.curselection()[0]
    del tasks[current_idx]
    Tasks.set(tasks)
    if current_idx == tasks_length - 1:
        lb.select_clear(0, tk.END)
        lb.select_set(current_idx - 1)
    else:
        lb.select_clear(0, tk.END)
        lb.select_set(current_idx)

root = tk.Tk()
root.geometry('500x500')

task_string = tk.StringVar()

# Title at the top of the window
title = tk.Label(master=root, text="To-Do", font='Calibri 24 bold', pady=20)

# Add frames for the new task entry / task display
top_frame = tk.Frame(master=root)
bot_frame = tk.Frame(master=root, width=450, height=300, bg="white")
bot_frame.pack_propagate(False)

tasks = []
Tasks = tk.StringVar(value=tasks)

# Add elements for task entry
new_task = tk.Entry(master=top_frame, width=50, textvariable=task_string)
button = tk.Button(master=top_frame, width=10, padx=10, text="Add Task", command=lambda : addtask(task_string, tasks))
button_del = tk.Button(master=top_frame, width=10, padx=10, text="Delete Task", command=delete)
lb = tk.Listbox(master=root, width=30, height=10, font='Calibri 16 bold',listvariable=Tasks)
new_task.bind('<Return>', lambda event: addtask(task_string, tasks))
lb.bind('<BackSpace>', delete)


# Pack elements into window
title.pack()
top_frame.pack()
new_task.pack(fill=tk.X, side=tk.LEFT, expand=True)
button.pack(padx=10)
button_del.pack(padx=10)
lb.pack(pady=20)

root.mainloop()