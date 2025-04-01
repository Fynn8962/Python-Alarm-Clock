import time
import tkinter as tk
import ttkbootstrap as ttk
import winsound
import datetime
import threading
from time import strftime


def entry_select_all(event):
        event.widget.select_range(0, 'end')
        return "break"


# region CLOCK FUNCTIONS
def update_clock():
        string_time = strftime('%H:%M:%S')
        clock_label.config(text=string_time)
        clock_label.after(1000, update_clock)
# endregion

# region TIMER FUNCTIONS


timer_running = False
timer_stoped = False


def display_timer():
        global timer_running

        close_stopwatch()
        close_alarm()

        if timer_running:
                pass
        elif not timer_running or timer_stoped:
                hour.set("00")
                minute.set("00")
                second.set("00")
                hour_entry.place(
                        relx=0.35, rely=0.55, anchor="center",
                        relwidth=0.13, relheight=0.22
                )
                minute_entry.place(
                        relx=0.50, rely=0.55, anchor="center",
                        relwidth=0.13, relheight=0.22
                )
                second_entry.place(
                        relx=0.65, rely=0.55, anchor="center",
                        relwidth=0.13, relheight=0.22
                )
                timer_start_button.place(
                        relx=0.3, rely=0.85, anchor="center",
                        relwidth=0.18, relheight=0.2
                )
                timer_stop_button.place(
                        relx=0.5, rely=0.85, anchor="center",
                        relwidth=0.18, relheight=0.2
                )
                timer_restart_button.place(
                        relx=0.7, rely=0.85, anchor="center",
                        relwidth=0.18, relheight=0.2
                )


def close_timer():
        hour_entry.place_forget()
        minute_entry.place_forget()
        second_entry.place_forget()
        timer_start_button.place_forget()
        timer_stop_button.place_forget()
        timer_restart_button.place_forget()
        alt_label.place_forget()
        timer_button.config(command=display_timer)
        timer_stop_button.config(text='stop', command=stop_timer)


def update_timer():
        global timeData, timer_running

        if not timer_running or timer_stoped:
                return

        if not isinstance(timeData, int) or timeData < 0:
                return

        if timeData >= 0:
                mins, secs = divmod(timeData, 60)

                hours = 0
                if mins > 60:
                        hours, mins = divmod(mins, 60)

                hour.set("{0:2d}".format(hours))
                minute.set("{0:2d}".format(mins))
                second.set("{0:2d}".format(secs))
                formatted_time = f"{hours:02d}:{mins:02d}:{secs:02d}"
                timer_button.config(text=formatted_time)

                if timeData == 0:
                        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
                        close_alarm()
                        close_stopwatch()
                        hour_entry.place_forget()
                        minute_entry.place_forget()
                        second_entry.place_forget()
                        timer_start_button.place_forget()
                        timer_restart_button.place_forget()
                        alt_label.place(relx=0.50, rely=0.55, anchor="center")
                        alt_label.config(text="RING RING")
                        timer_stop_button.config(
                                text='close', command=close_timer
                        )
                        timer_running = False
                        return

                timeData -= 1
                window.after(1000, update_timer)


def set_timer():
        global timeData, timer_running, timer_stoped

        if timer_running and not timer_stoped:
                return

        timer_running = True
        timer_stoped = False
        try:
                timeData = (int(hour.get()) * 3600 +
                            int(minute.get()) * 60 +
                            int(second.get()))
        except ValueError:
                hour.set("00")
                minute.set("00")
                second.set("00")
                return
        update_timer()


def stop_timer():
        global timer_stoped
        timer_stoped = True
        timer_button.config(text="timer")


def restart_timer():
        global timer_running
        timer_running = False
        hour.set("00")
        minute.set("00")
        second.set("00")
        timer_button.config(text="timer")
# endregion

# region STOPWATCH FUNCTIONS


stopwatch_running = False
start_time = 0
elapsed_time = 0


def display_stopwatch():
        close_timer()
        close_alarm()
        stopwatch_label.place(relx=0.5, rely=0.55,
                              anchor="center", relheight=0.2
                              )
        stopwatch_start.place(relx=0.3, rely=0.85, anchor="center",
                              relwidth=0.18, relheight=0.2
                              )
        stopwatch_stop.place(relx=0.5, rely=0.85, anchor="center",
                             relwidth=0.18, relheight=0.2
                             )
        stopwatch_reset.place(relx=0.7, rely=0.85, anchor="center",
                              relwidth=0.18, relheight=0.2
                              )
        stopwatch_button.config(command=close_stopwatch)


def close_stopwatch():
        stopwatch_label.place_forget()
        stopwatch_button.config(command=display_stopwatch)
        stopwatch_start.place_forget()
        stopwatch_stop.place_forget()
        stopwatch_reset.place_forget()


def update_stopwatch():
        global stopwatch_running, stopwatch_counter_ms
        if stopwatch_running:
                current_time = time.time()
                total_time = elapsed_time + (current_time - start_time)

                hours, remainder = divmod(total_time, 3600)
                minutes, seconds = divmod(remainder, 60)
                millis = int((total_time - int(total_time)) * 100)
                stopwatch_label.config(
                        text=f"{int(hours):02d}:{int(minutes):02d}:"
                        f"{int(seconds):02d}.{millis:02d}"
                )
                stopwatch_label.after(10, update_stopwatch)


def start_stopwatch():
    global stopwatch_running, start_time
    if not stopwatch_running:
        stopwatch_running = True
        start_time = time.time()
        update_stopwatch()


def stop_stopwatch():
    global stopwatch_running, elapsed_time
    if stopwatch_running:
        elapsed_time += time.time() - start_time
        stopwatch_running = False


def reset_stopwatch():
    global stopwatch_running, elapsed_time
    stopwatch_running = False
    elapsed_time = 0
    stopwatch_label.config(text="00:00:00.00")
# endregion

# region ALARM FUNCTIONS


alarm_set = False


def display_alarm():
        global alarm_set
        if alarm_set:
                pass
        elif not alarm_set:
                hour.set("00")
                minute.set("00")

        close_timer()
        close_stopwatch()
        alarm_button.config(command=close_alarm)
        alarm_hour_entry.place(relx=0.42, rely=0.55, anchor="center",
                               relwidth=0.13, relheight=0.22
                               )
        alarm_minute_entry.place(relx=0.58, rely=0.55, anchor="center",
                                 relwidth=0.13, relheight=0.22
                                 )
        alarm_set_button.place(relx=0.5, rely=0.85, anchor="center",
                               relwidth=0.18, relheight=0.2
                               )


def close_alarm():
        alarm_button.config(command=display_alarm)
        alarm_hour_entry.place_forget()
        alarm_minute_entry.place_forget()
        alarm_set_button.place_forget()
        alt_label.place_forget()


def exit_alarm():
        global alarm_set
        alarm_set = False
        alarm_button.config(text='    Alarm    ', command=display_alarm)
        alarm_set_button.config(text='start', command=set_alarm)
        alarm_hour_entry.place_forget()
        alarm_minute_entry.place_forget()
        alarm_set_button.place_forget()
        alt_label.place_forget()


def set_alarm():
        global alarm_set

        try:
                alarm_hour = int(hour.get())
                alarm_minute = int(minute.get())

                if not (0 <= alarm_hour <= 23 and 0 <= alarm_minute <= 59):
                        hour.set("00")
                        minute.set("00")
                        return

                set_alarm_time = f"{alarm_hour:02d}:{alarm_minute:02d}"

        except ValueError:
                hour.set("00")
                minute.set("00")
                return

        alarm_set_button.config(text='stop', command=exit_alarm)
        alarm_set = True

        def alarm_loop():
                global alarm_set
                while True:
                        if not alarm_set:
                                break
                        current_time = datetime.datetime.now().strftime(
                                "%H:%M"
                                )
                        alarm_button.config(text="Alarm: " + set_alarm_time)

                        if current_time == set_alarm_time:
                                close_stopwatch()
                                close_timer()
                                alarm_hour_entry.place_forget()
                                alarm_minute_entry.place_forget()
                                alarm_set_button.place(relx=0.5, rely=0.85,
                                                       anchor="center",
                                                       relwidth=0.18,
                                                       relheight=0.2
                                                       )
                                alt_label.place(relx=0.50, rely=0.55,
                                                anchor="center"
                                                )
                                alt_label.config(text="AUFSTEHEN!")
                                alarm_set_button.config(text='close',
                                                        command=close_alarm
                                                        )
                                winsound.PlaySound("sound.wav",
                                                   winsound.SND_ASYNC
                                                   )
                                alarm_set = False
                                break
                        time.sleep(1)

        alarm_thread = threading.Thread(target=alarm_loop)
        alarm_thread.daemon = True
        alarm_thread.start()
# endregion

# WINDOW


window = ttk.Window(themename="minty")
# Darkmode: "darkly", "solar" / Lightmode: "minty", "sandstone"
window.title('Alarm Clock')
window.geometry('750x450')
window.resizable(False, False)

# CLOCK
clock_frame = ttk.Frame(window)
clock_label = ttk.Label(clock_frame, font=("arial", 43),
                        anchor="center"
                        )
alt_label = ttk.Label(clock_frame, font=("Arial", 18))

# TIMER
hour = tk.StringVar()
minute = tk.StringVar()
second = tk.StringVar()

hour.set("00")
minute.set("00")
second.set("00")

timer_frame = ttk.Frame(window)
timer_button = ttk.Button(timer_frame, text='    Timer    ',
                          command=display_timer
                          )
hour_entry = ttk.Entry(clock_frame, width=3,
                       font=("Arial", 18),
                       textvariable=hour
                       )
minute_entry = ttk.Entry(clock_frame, width=3,
                         font=("Arial", 18),
                         textvariable=minute
                         )
second_entry = ttk.Entry(clock_frame, width=3,
                         font=("Arial", 18),
                         textvariable=second
                         )
timer_start_button = ttk.Button(clock_frame,
                                text='start',
                                command=set_timer
                                )
timer_stop_button = ttk.Button(clock_frame,
                               text='stop',
                               command=stop_timer
                               )
timer_restart_button = ttk.Button(clock_frame,
                                  text='restart',
                                  command=restart_timer
                                  )

# STOPWATCH
stopwatch_placer = ttk.StringVar()
stopwatch_placer.set("00:00:00")

stopwatch_frame = ttk.Frame(window)
stopwatch_button = ttk.Button(stopwatch_frame,
                              text='Stopwatch',
                              command=display_stopwatch
                              )
stopwatch_label = ttk.Label(clock_frame,
                            font=("Arial", 18),
                            text="00:00:00.00"
                            )
stopwatch_start = ttk.Button(clock_frame,
                             text="start",
                             command=start_stopwatch
                             )
stopwatch_stop = ttk.Button(clock_frame,
                            text="stop",
                            command=stop_stopwatch
                            )
stopwatch_reset = ttk.Button(clock_frame,
                             text="reset",
                             command=reset_stopwatch
                             )

# ALARM
alarm_frame = ttk.Frame(window)
alarm_button = ttk.Button(alarm_frame,
                          text='    Alarm    ',
                          command=display_alarm
                          )

alarm_hour_entry = ttk.Entry(clock_frame, width=3,
                             font=("Arial", 18),
                             textvariable=hour
                             )
alarm_minute_entry = ttk.Entry(clock_frame, width=3,
                               font=("Arial", 18),
                               textvariable=minute
                               )
alarm_set_button = ttk.Button(clock_frame,
                              text="set",
                              command=set_alarm
                              )

# GRID
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)

# CLOCK PACK
clock_frame.grid(row=1, column=1, sticky='nesw')
clock_label.pack(fill='both')
alt_label.place_forget()

# TIMER PACK
timer_frame.grid(row=2, column=0, sticky='nsew')
timer_button.pack(expand='True', fill='both')
timer_start_button.place_forget()
timer_stop_button.place_forget()
timer_restart_button.place_forget()
hour_entry.place_forget()
minute_entry.place_forget()
second_entry.place_forget()

# STOPWATCH PACK
stopwatch_frame.grid(row=2, column=2, sticky='nsew')
stopwatch_button.pack(expand='True', fill="both")
stopwatch_label.place_forget()
stopwatch_start.place_forget()
stopwatch_stop.place_forget()
stopwatch_reset.place_forget()

# ALARM PACK
alarm_frame.grid(row=0, column=0, sticky='nesw')
alarm_button.pack(expand='True', fill='both')

alarm_hour_entry.place_forget()
alarm_minute_entry.place_forget()
alarm_set_button.place_forget()

# BILD
hour_entry.bind("<FocusIn>", entry_select_all)
minute_entry.bind("<FocusIn>", entry_select_all)
second_entry.bind("<FocusIn>", entry_select_all)
alarm_hour_entry.bind("<FocusIn>", entry_select_all)
alarm_minute_entry.bind("<FocusIn>", entry_select_all)

# RUN
update_clock()
window.mainloop()
