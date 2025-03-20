import random as rand

def main():
    results = []
    rand.seed(0)
    results.append(roll_dice(6))
    results.append(roll_dice(10))
    results.append(roll_dice(12))
    results.append(roll_dice(20))
    print(results)

def roll_dice(faces: int):
    return rand.randint(1, faces)

main()
