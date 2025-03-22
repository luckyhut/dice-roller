import random as rand
from gui import *

def main():
    results = []
    rand.seed(0)
    results.append(roll_dice(6))
    results.append(roll_dice(10))
    results.append(roll_dice(12))
    results.append(roll_dice(20))
    print(results)
    start_window()

def roll_dice(faces: int):
    return rand.randint(1, faces)

main()
