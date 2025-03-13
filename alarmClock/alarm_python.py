import tkinter as tk
import ttkbootstrap as ttk
from time import strftime


def update_time():
        string_time = strftime('%H:%M:%S %p')
        time_label.config(text = string_time)
        time_label.after(1000, update_time)

# create window
window = ttk.Window(themename = 'darkly')
window.title('Alarm Clock')
window.geometry('750x450')

# widget
time_frame = ttk.Frame(window)
time_label = ttk.Label(time_frame, font=("Arial", 48), anchor="center", foreground = 'red')
alt_label = ttk.Label(time_frame, font=("Arial", 24), text = 'timer', anchor="center", foreground = 'red')

# grid
window.columnconfigure(0, weight= 1)
window.columnconfigure(1, weight= 1)
window.columnconfigure(2, weight= 1)
window.columnconfigure(3, weight= 1)
window.rowconfigure(0, weight = 1)
window.rowconfigure(1, weight = 1)
window.rowconfigure(2, weight = 1)

time_frame.grid(row =1, column = 1, columnspan = 2, sticky = 'nsew')
time_label.pack(expand = 'true', fill = 'both')
alt_label.pack(expand = 'true', fill = 'x')
# run
update_time()
window.mainloop()  