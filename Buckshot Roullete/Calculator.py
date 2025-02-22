import os

def wackprint():
    os.system('cls' if os.name == 'nt' else 'clear')

def game_loop(realbullets, blankbullets, bulletsnow, bulletnumber, hints):
    shots_fired = bulletnumber - bulletsnow + 1
    bullet_suffix = 'st' if shots_fired == 1 else 'nd' if shots_fired == 2 else 'rd' if shots_fired == 3 else 'th'
    hit_chance = (realbullets / (realbullets + blankbullets)) * 100 if (realbullets + blankbullets) > 0 else 0

    print("----------------------------")
    print(f"L/B bullets: {realbullets}/{blankbullets} ({hit_chance:.1f}% chance of firing a live bullet!)")
    print(f"Amount of bullets in the beginning: {bulletnumber}, amount of bullets now: {bulletsnow}")
    print(f"The {shots_fired}{bullet_suffix} bullet is about to be shot")

    if shots_fired in hints:
        print(f"Hint: This bullet is {'live' if hints[shots_fired] == 'L' else 'blank'}")

    print("----------------------------")
    
    question = input("Update if a live/blank bullet has been fired, enter extra info, or end the round (L/B/E/O): ").strip().lower()
    
    if question == "e":
        extra_info = input("Enter extra info (e.g., '2L' for live or '5B' for blank): ").strip().upper()
        if len(extra_info) >= 2 and extra_info[:-1].isdigit() and extra_info[-1] in ('L', 'B'):
            bullet_pos = int(extra_info[:-1])
            hints[bullet_pos] = extra_info[-1] 
            
            if extra_info[-1] == "B":
                blankbullets -= 1
            elif extra_info[-1] == "L":
                realbullets -= 1

    elif question == "b":
        blankbullets -= 1
        bulletsnow -= 1 
    elif question == "l":
        realbullets -= 1
        bulletsnow -= 1
    elif question == "o":
        question2 = input("New game? (y/n): ").strip().lower()
        if question2 == "y":
            wackprint()
            start()
        else:
            print("Have a nice one!")
            return
    else:
        print("Super Cool Error!")

    wackprint()

    if bulletsnow > 0:
        game_loop(realbullets, blankbullets, bulletsnow, bulletnumber, hints)
    else:
        print("No bullets left! Game over.")
        start()

def start():
    realbullets = int(input("How many bullets are live?: "))
    blankbullets = int(input("How many bullets are blank?: "))
    bulletnumber = realbullets + blankbullets
    hints = {}

    wackprint()
    game_loop(realbullets, blankbullets, bulletnumber, bulletnumber, hints)

start()