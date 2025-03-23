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
    frame_left = ttk.Frame(root, borderwidth=10, relief="ridge", width=200, height=100)
    frame_right = ttk.Frame(root, borderwidth=10, relief="ridge", width=200, height=100)
        
    # main two frames on the grid
    frame_left.grid(column=0, row=0, sticky="nsew")
    frame_right.grid(column=1, row=0, sticky="nsew")

    # center the buttons in the frames
    frame_left.columnconfigure(0, weight=1)
    frame_left.columnconfigure(0, weight=1)
    frame_right.columnconfigure(0, weight=1)
    frame_right.columnconfigure(0, weight=1)

    # create and add clear button
    clear = ttk.Button(frame_left, text="clear")
    clear.grid(column=0, row=0, sticky="", padx=5, pady=5)

    
    # create dice buttons
    d4 = ttk.Button(frame_right, text="d4")
    d6 = ttk.Button(frame_right, text="d6")
    d10 = ttk.Button(frame_right, text="d10")
    d12 = ttk.Button(frame_right, text="d12")
    d20 = ttk.Button(frame_right, text="d20")

    # add buttons to right
    d4.grid(column=0, row=0, sticky="", padx=5, pady=5)
    d6.grid(column=0, row=1, sticky="", padx=5, pady=5)
    d10.grid(column=0, row=2, sticky="", padx=5, pady=5)
    d12.grid(column=0, row=3, sticky="", padx=5, pady=5)
    d20.grid(column=0, row=4, sticky="", padx=5, pady=5)
        
    root.mainloop()
