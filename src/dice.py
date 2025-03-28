import random as rand
import time

def roll_dice(faces: int):
    rand.seed(time.time_ns())
    return rand.randint(1, faces)
