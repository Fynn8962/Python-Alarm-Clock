import tkinter as tk 
# from tkinter import ttk / das wird nicht mer gebraucht weil jetzt ttkbootstrap alle ttk dinger verwendet 
import ttkbootstrap as ttk #um bessere design zu haben (extensions die ich mittels pip install instaliert habe)

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)
# window
window = ttk.Window(themename = 'darkly')    #neues Window erstellen / theme vom fenster ändern
window.title('Miles to kilometers')    #window Title definieren
window.geometry('750x450')  #window grösse definierte (widthxheight)


# title
title_lable = ttk.Label(master = window, text = "Alarm Clock", font ='calibiri 24 bold')     #ein erstes label definieren, mit (master = window) gibt man denen Container in welchem das sitzen wird. Bei uns das erstellte window. text, font etc definiert das design und den inhalt
title_lable.pack()

#input field
input_frame = ttk.Frame(master = window)    #Ist der Frame um die beiden Elemente "entry" "button" rundherum
entry_int = tk.IntVar() # Erstellt eine Variable welche Werte speichern und aufrufen kann. 
entry = ttk.Entry(master = input_frame, textvariable = entry_int) # Eingabefeld, alles was in diesem eingegben wrid wird im entryInt gespeichert
button = ttk.Button(master = input_frame, text = 'Convert', command = convert) # Button des input fields (command um funktion anzugeben die wo anders defniert wird (nie die funktion direkt aufrufen heisst NICHT convert() schreiben))
entry.pack(side = 'left', padx = 10)    #um das widget in den Frame (master = window) zu packen
button.pack(side = 'left')   #um das widget in den Frame (master = window) zu packen
input_frame.pack(pady = 10)  #macht auch das verschiedene dinge untereinader platziert werden (das eingaefeld unter dem Titel bsp.)

# padx und pady um padding zu setzen
# side = um objekte nebeneinander zu platzieren. 


# output
output_string = tk.StringVar()
output_label = ttk.Label(
    master = window,
    text = 'output', 
    font ='calibiri 24', 
    textvariable = output_string)

output_label.pack(pady = 5)


# run
window.mainloop()   #damit das window überhaupt dauerhaft angezeigt wird. 