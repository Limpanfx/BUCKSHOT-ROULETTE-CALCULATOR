import os
import time

def wackprint():
    os.system('cls' if os.name == 'nt' else 'clear')

def game_loop(livebullets, blankbullets, bulletsnow, bulletnumber, hints, used_hints):
    shots_fired = bulletnumber - bulletsnow + 1
    bullet_suffix = 'st' if shots_fired == 1 else 'nd' if shots_fired == 2 else 'rd' if shots_fired == 3 else 'th'
    
    # Calculate hit chance only from remaining unknown bullets
    remaining_unknown = (livebullets + blankbullets)
    hit_chance = (livebullets / remaining_unknown) * 100 if remaining_unknown > 0 else 0

    print("----------------------------")
    print(f"L/B bullets: {livebullets}/{blankbullets} ({hit_chance:.1f}% chance of firing live bullet!)")
    print(f"Amount of bullets in the beginning: {bulletnumber}, amount of bullets left now: {bulletsnow}")
    print(f"The {shots_fired}{bullet_suffix} bullet is about to be shot")
    
    if shots_fired in hints:
        if shots_fired not in used_hints:
            if hints[shots_fired] == 'L':
                livebullets -= 1
            else:
                blankbullets -= 1
            used_hints.add(shots_fired)
        
        if hints[shots_fired] == 'L':
            print("This is a LIVE bullet! <--------------------------")
        else:
            print("This is a BLANK bullet! <--------------------------")
        
        print("----------------------------")
        bulletsnow -= 1
        del hints[shots_fired]
        input("Press Enter to proceed to the next round...")
    else:
        print("----------------------------")
        question = input("Update if a live/blank bullet has been fired, enter extra info, or end the round (L/B/E/O): ").strip().lower()
        
        if question == "e":
            extra_info = input("Enter extra info (e.g., '2L' for live or '5B' for blank): ").strip().upper()
            if len(extra_info) >= 2 and extra_info[:-1].isdigit() and extra_info[-1] in ('L', 'B'):
                bullet_pos = int(extra_info[:-1])
                if bullet_pos not in hints:
                    hints[bullet_pos] = extra_info[-1]
        elif question == "b":
            blankbullets -= 1
            bulletsnow -= 1
        elif question == "l":
            livebullets -= 1
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
        game_loop(livebullets, blankbullets, bulletsnow, bulletnumber, hints, used_hints)
    else:
        print("No bullets left! New round starting...")
        time.sleep(1)
        wackprint()
        start()

def start():
    livebullets = int(input("How many bullets are live?: "))
    blankbullets = int(input("How many bullets are blank?: "))
    bulletnumber = livebullets + blankbullets
    hints = {}
    used_hints = set()

    wackprint()
    game_loop(livebullets, blankbullets, bulletnumber, bulletnumber, hints, used_hints)

start()
