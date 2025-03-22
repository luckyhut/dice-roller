from tkinter import *
from tkinter import ttk
from dice import roll_dice

def start_window():
    # Get a d6 and a d20 roll
    d6 = roll_dice(6)
    d20 = roll_dice(20)
    output = f"Hello World \nd6 roll: {d6} \nd20 roll: {d20}"

    # Tkinter setup
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text=output).grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()
