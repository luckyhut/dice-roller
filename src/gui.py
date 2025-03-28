from tkinter import *
from tkinter import ttk
from dice import roll_dice

current_roll = {
    4: [],
    6: [],
    10: [],
    12: [],
    20: [],
}
history_listbox = None

def start_window():
    # setup root; left is 2/3, right is 1/3
    root = Tk()
    root.rowconfigure(0, weight=2)
    root.columnconfigure(0, weight=2)
    root.columnconfigure(1, weight=1)

    # setup frames and add buttons
    frame_left = left_setup(root)
    frame_right = right_setup(root)
    add_clear_button(frame_left)
    add_history(frame_left)
    add_dice_buttons(frame_right)
        
    root.mainloop()

def left_setup(root):
    frame_left = ttk.Frame(root, borderwidth=10, relief="ridge")
    frame_left.grid(column=0, row=0, sticky="nsew")
    frame_left.rowconfigure(1, weight=1)
    frame_left.columnconfigure(0, weight=1)
    return frame_left

def right_setup(root):
    frame_right = ttk.Frame(root, borderwidth=10, relief="ridge")
    frame_right.grid(column=1, row=0, sticky="nsew")
    frame_right.rowconfigure(0, weight=1)
    frame_right.columnconfigure(0, weight=1)
    return frame_right

def add_clear_button(frame_left):
    clear = ttk.Button(frame_left, text="clear", command=clear_roll)
    clear.grid(column=0, row=0, sticky="n", padx=5, pady=5)

def add_history(frame_left):
    global history_listbox
    history_listbox= Listbox(frame_left)
    history_listbox.grid(column=0, row=1, sticky="nsew", padx=5, pady=5)
    sb = ttk.Scrollbar(frame_left, orient=VERTICAL, command=history_listbox.yview)
    sb.grid(column=1, row=1, stick=(N,S))
    history_listbox['yscrollcommand'] = sb.set
    
def add_dice_buttons(frame_right):
    button_frame = ttk.Frame(frame_right)
    button_frame.grid(column=0, row=0, sticky="n")
    finish = ttk.Button(button_frame, text="Roll !", command=finish_roll)
    d4 = ttk.Button(button_frame, text="d4", command=roll_d4)
    d6 = ttk.Button(button_frame, text="d6", command=roll_d6)
    d10 = ttk.Button(button_frame, text="d10", command=roll_d10)
    d12 = ttk.Button(button_frame, text="d12", command=roll_d12)
    d20 = ttk.Button(button_frame, text="d20", command=roll_d20)
    # add buttons to button_container
    finish.grid(column=0, row=0, sticky="", padx=5, pady=5)
    d4.grid(column=0, row=1, sticky="", padx=5, pady=5)
    d6.grid(column=0, row=2, sticky="", padx=5, pady=5)
    d10.grid(column=0, row=3, sticky="", padx=5, pady=5)
    d12.grid(column=0, row=4, sticky="", padx=5, pady=5)
    d20.grid(column=0, row=5, sticky="", padx=5, pady=5)

def finish_roll():
    if len(current_roll[4]) == 0 and len(current_roll[6]) == 0 and len(current_roll[10]) == 0 and len(current_roll[12]) == 0 and len(current_roll[20]) == 0:
        return
    result = ""
    for die, rolls in current_roll.items():
        if rolls:
            result += f"{len(rolls)}d{die}:{rolls}"
    history_listbox.insert(0, result)
    clear_roll()

def clear_roll():
    for _, rolls in current_roll.items():
        rolls.clear()

def roll_d4():
    result = roll_dice(4)
    current_roll[4].append(result)
    
def roll_d6():
    result = roll_dice(6)
    current_roll[6].append(result)
           
def roll_d10():
    result = roll_dice(10)
    current_roll[10].append(result)
            
def roll_d12():
    result = roll_dice(12)
    current_roll[12].append(result)
            
def roll_d20():
    result = roll_dice(20)
    current_roll[20].append(result)
    
