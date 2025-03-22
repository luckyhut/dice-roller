import random as rand

def roll_dice(faces: int):
    rand.seed(0)
    return rand.randint(1, faces)
