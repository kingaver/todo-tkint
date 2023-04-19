import tkinter as tk

def addtask(lb, task_string):
    lb.insert(0,task_string.get())

root = tk.Tk()
root.geometry('500x500')

task_string = tk.StringVar()

# Title at the top of the window
title = tk.Label(master=root, text="To-Do", font='Calibri 24 bold', pady=20)

# Add frames for the new task entry / task display
top_frame = tk.Frame(master=root)
bot_frame = tk.Frame(master=root, width=450, height=300, bg="white")
bot_frame.pack_propagate(False)

# Add elements for task entry
new_task = tk.Entry(master=top_frame, width=50, textvariable=task_string)
button = tk.Button(master=top_frame, width=10, padx=10, text="Add Task", command=lambda: addtask(lb, task_string))
lb = tk.Listbox(master=root, width=30, height=10, font='Calibri 16 bold')

# Pack elements into window
title.pack()
top_frame.pack()
new_task.pack(fill=tk.X, side=tk.LEFT, expand=True)
button.pack(padx=10)
lb.pack(pady=20)

root.mainloop()