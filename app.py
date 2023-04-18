import tkinter as tk

root = tk.Tk()
root.geometry('500x500')

# Title at the top of the window
title = tk.Label(master=root, text="To-Do", font='Calibri 24 bold', pady=20)
title.pack()

# Add frames for the new task entry / task display
top_frame = tk.Frame(master=root)

new_task = tk.Text(master=top_frame)
top_frame.pack()
new_task.pack()

root.mainloop()