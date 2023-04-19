import tkinter as tk

def addtask(frame, canvas, last_y):
    task_to_add = tk.Frame(master=frame, height=100, width=100, bg="black", pady=5)
    canvas.create_window((50, last_y[0]), window=task_to_add, anchor='nw')
    last_y[0] += 100
    print(last_y[0])

root = tk.Tk()
root.geometry('500x500')

# Title at the top of the window
title = tk.Label(master=root, text="To-Do", font='Calibri 24 bold', pady=20)

# Add frames for the new task entry / task display
top_frame = tk.Frame(master=root)
bot_frame = tk.Frame(master=root, bg="white")

# Create a scrollable canvas for the task list
canvas = tk.Canvas(bot_frame, bg="white")
scrollbar = tk.Scrollbar(bot_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="white")
last_y = [0]

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
canvas.configure(yscrollcommand=scrollbar.set)

# Add elements for task entry
new_task = tk.Entry(master=top_frame, width=50)
print(last_y)
button = tk.Button(master=top_frame, width=10, padx=10, text="Add Task", command=lambda: addtask(bot_frame, canvas, last_y))

# Pack elements into window
title.pack()
top_frame.pack()
new_task.pack(fill=tk.X, side=tk.LEFT, expand=True)
button.pack(padx=10)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
bot_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

root.mainloop()
