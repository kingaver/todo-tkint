import tkinter as tk

def addtask():
    task_to_add = tk.Frame(master=bot_frame, height=100, width=100, bg="black")
    task_to_add.pack(pady=5)

root = tk.Tk()
root.geometry('500x500')

# Title at the top of the window
title = tk.Label(master=root, text="To-Do", font='Calibri 24 bold', pady=20)

# Add frames for the new task entry / task display
top_frame = tk.Frame(master=root)
bot_frame = tk.Frame(master=root, width=450, height=300, bg="white")

# Add elements for task entry
new_task = tk.Entry(master=top_frame, width=50)
button = tk.Button(master=top_frame, width=10, padx=10, text="Add Task", command=addtask)

# Pack elements into window
title.pack()
top_frame.pack()
new_task.pack(fill=tk.X, side=tk.LEFT, expand=True)
button.pack(padx=10)
bot_frame.pack(pady=20)

root.mainloop()