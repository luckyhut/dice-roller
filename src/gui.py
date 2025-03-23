from tkinter import *
from tkinter import ttk
from dice import roll_dice

def start_window():
    # Get a d6 and a d20 roll
    d6 = roll_dice(6)
    d20 = roll_dice(20)
    output = f"Hello World \nd6 roll: {d6} \nd20 roll: {d20}"

    # setup root; left is 2/3, right is 1/3
    root = Tk()
    root.columnconfigure(0, weight=2)
    root.columnconfigure(1, weight=1)

    # set up tkinter frames
    frame_left = ttk.Label(root, text="left side", padding=20)
    frame_right = ttk.Label(root, text="right side", padding=20)
        
    # place items on the grid
    frame_left.grid(column=0, row=0, sticky="e")
    frame_right.grid(column=1, row=0, sticky="nsew")
    
    root.mainloop()
