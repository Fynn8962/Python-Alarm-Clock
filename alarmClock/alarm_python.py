import time
import tkinter as tk
import ttkbootstrap as ttk
from time import strftime
from datetime import datetime

# clock
def update_clock():
        string_time = strftime('%H:%M:%S %p')
        clock_label.config(text = string_time)
        clock_label.after(1000, update_clock)    


# timer 
timer_running = False  

def display_timer():
        close_stopwatch()
        hour_entry.place(relx=0.38, rely=0.55, anchor="center", relwidth=0.11, relheight = 0.2) 
        minute_entry.place(relx=0.5, rely=0.55, anchor="center", relwidth=0.11, relheight = 0.2)
        second_entry.place(relx=0.62, rely=0.55, anchor="center", relwidth=0.11, relheight = 0.2)
        timer_state_button.place(relx=0.5, rely=0.85, anchor="center")
        timer_state_button.config(text = "start", command = set_timer)
        timer_button.config(command=close_timer)

def close_timer():
        global timer_running
        hour_entry.place_forget()
        minute_entry.place_forget()
        second_entry.place_forget()
        timer_state_button.place_forget()
        alt_label.pack_forget()
        timer_button.config(command=display_timer)
        timer_running = False



def set_timer():
        timer_state_button.config(text = "close", command=close_timer)

        global timer_running
        if timer_running:
                return
        
        timer_running = True

        try: 
                timeData = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        except:
                hour.set("00")
                minute.set("00")
                second.set("00")
                return 
        
        while timeData >-1 and timer_running:

                mins,secs = divmod(timeData,60)

                hours=0
                if mins >60:
                        hours, mins = divmod(mins, 60)

                        
                hour.set("{0:2d}".format(hours))
                minute.set("{0:2d}".format(mins))
                second.set("{0:2d}".format(secs))

                window.update()
                time.sleep(1)

                if(timeData == 0):
                        hour_entry.place_forget()
                        minute_entry.place_forget()
                        second_entry.place_forget()
                        alt_label.pack()
                        alt_label.config(text = "RING RING")
                        timer_state_button.config(text = "close", command = close_timer)
        
                timeData -= 1
        timer_running = False

# stopwatch 
stopwatch_running = False
stopwatch_counter = 0

def display_stopwatch():
        close_timer()
        stopwatch_label.place(relx=0.5, rely=0.55, anchor="center", relheight = 0.2) 
        stopwatch_start.place(relx=0.3, rely=0.85, anchor="center", relwidth=0.15, relheight = 0.2) 
        stopwatch_stop.place(relx=0.5, rely=0.85, anchor="center", relwidth=0.15, relheight = 0.2)
        stopwatch_reset.place(relx=0.7, rely=0.85, anchor="center", relwidth=0.15, relheight = 0.2)
        stopwatch_button.config(command= close_stopwatch)

def close_stopwatch():
        stopwatch_label.place_forget()
        stopwatch_button.config(command=display_stopwatch)
        stopwatch_start.place_forget()
        stopwatch_stop.place_forget()
        stopwatch_reset.place_forget()

def update_stopwatch():
        global stopwatch_running, stopwatch_counter
        if stopwatch_running:
                mins, secs = divmod(stopwatch_counter, 60)
                hours, mins = divmod(mins, 60)
                stopwatch_label.config(text=f"{hours:02d}:{mins:02d}:{secs:02d}")
                stopwatch_counter += 1
                stopwatch_label.after(1000, update_stopwatch)

def start_stopwatch():
    global stopwatch_running
    if not stopwatch_running:
        stopwatch_running = True
        update_stopwatch()

def stop_stopwatch():
    global stopwatch_running
    stopwatch_running = False

def reset_stopwatch():
    global stopwatch_running, stopwatch_counter
    stopwatch_running = False
    stopwatch_counter = 0
    stopwatch_label.config(text="00:00:00")



# create window
window = ttk.Window(themename = 'darkly')
window.title('Alarm Clock')
window.geometry('750x450')
window.resizable(False, False)

# clock
clock_frame = ttk.Frame(window)
clock_label = ttk.Label(clock_frame, font=("arial", 43), anchor="center", foreground = 'white')
alt_label = ttk.Label(clock_frame, font=("Arial", 18))

# timer function
hour= tk.StringVar()
minute= tk.StringVar()
second=tk.StringVar()
  
hour.set("00")
minute.set("00")
second.set("00")

## timer button
timer_frame = ttk.Frame(window)                 
timer_button = ttk.Button(timer_frame, text = '    Timer    ', command = display_timer)

## timer in main
hour_entry = ttk.Entry(clock_frame, width = 3,  font=("Arial",18), textvariable = hour) 
minute_entry = ttk.Entry(clock_frame, width = 3,  font=("Arial",18), textvariable = minute)
second_entry = ttk.Entry(clock_frame, width = 3,  font=("Arial",18), textvariable = second)
timer_state_button = ttk.Button(clock_frame, command = set_timer)

#stopwatch function
stopwatch_placer = ttk.StringVar()
stopwatch_placer.set("00:00:00")

# Stopwatch button
stopwatch_frame = ttk.Frame(window)
stopwatch_button = ttk.Button(stopwatch_frame, text = 'Stopwatch', command = display_stopwatch)

# stopwatch in main
stopwatch_label = ttk.Label(clock_frame, font = ("Arial", 18), text = "00:00:00")
stopwatch_start = ttk.Button(clock_frame, text= "start", command= start_stopwatch)
stopwatch_stop = ttk.Button(clock_frame, text= "stop", command = stop_stopwatch)
stopwatch_reset = ttk.Button(clock_frame, text= "reset", command = reset_stopwatch)


# grid  
window.columnconfigure(0, weight= 1)
window.columnconfigure(1, weight= 1)
window.columnconfigure(2, weight= 1)
window.rowconfigure(0, weight = 1)
window.rowconfigure(1, weight = 1)
window.rowconfigure(2, weight = 1)


# clock pack
clock_frame.grid(row =1, column = 1, sticky = 'nesw')
clock_label.pack( fill = 'both')
alt_label.pack_forget()

# timer pack
timer_frame.grid(row = 2, column = 0, sticky = 'nsew')
timer_button.pack(expand = 'True', fill="both")
timer_state_button.place_forget()
hour_entry.place_forget()
minute_entry.place_forget()
second_entry.place_forget()

#stopwatch pack
stopwatch_frame.grid(row = 2, column = 2, sticky = 'nsew')
stopwatch_button.pack(expand='True', fill="both")
stopwatch_label.place_forget()
stopwatch_start.place_forget()
stopwatch_stop.place_forget()
stopwatch_reset.place_forget()

# run
update_clock()
window.mainloop()  