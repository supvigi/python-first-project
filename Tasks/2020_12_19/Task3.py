from random import randint


def tank1_shot():
    reach_or_not = randint(1, 3)
    fire_or_critical_or_not = randint(1, 3)

    if reach_or_not == 2:
        if fire_or_critical_or_not == 1:
            tank2["health"] -= tank1["fire"] * 2
            print("Reach and bonus, tank2 got critical! Tank2 health:", tank2["health"])
        elif fire_or_critical_or_not == 2:
            tank2["health"] -= tank1["fire"]
            tank2["health"] -= 1
            print("Reach and bonus, tank2 is burning! Tank2 health:", tank2["health"])
        else:
            tank2["health"] -= tank1["fire"]
            print("Reach! Tank2 health:", tank2["health"])
    elif reach_or_not == 3:
        if tank2["armor"] > 0:
            tank2["armor"] -= tank1["fire"]
            print("Reach, but you got the armor! Tank2 armor:", tank2["armor"])
        else:
            tank2["health"] -= tank1["fire"]
            print("Reach, but you got the armor, but the armor is broken, so you got the tank2 itself! "
                  "Tank2 health:", tank2["health"])
    else:
        print("Miss! Tank2 health:", tank2["health"])


def tank2_shot():
    reach_or_not2 = randint(1, 3)
    fire_or_critical_or_not2 = randint(1, 3)

    if reach_or_not2 == 2:
        if fire_or_critical_or_not2 == 2:
            tank1["health"] -= tank2["fire"]
            tank1["health"] -= 1
            print("Reach and bonus, tank1 is burning! Tank1 health:", tank1["health"])
        else:
            tank1["health"] -= tank2["fire"]
            print("Reach! Tank1 health:", tank1["health"])
    elif reach_or_not2 == 3:
        if tank1["armor"] > 0:
            tank1["armor"] -= tank2["fire"]
            print("Reach, but you got the armor! Tank1 armor:", tank1["armor"])
        else:
            tank1["health"] -= tank1["fire"]
            print("Reach, but you got the armor, but the armor is broken, so you got the tank1 itself! "
                  "Tank1 health:", tank1["health"])
    else:
        print("Miss! Tank1 health:", tank1["health"])


tank1 = {"armor": 5, "health": 15, "speed": 15, "fire": 2, "steer": 2}
tank2 = {"armor": 10, "health": 20, "speed": 5, "fire": 3, "steer": 1}

while True:
    if tank1["health"] < 0:
        print("The winner is tank2!")
        exit(0)
    elif tank2["health"] < 0:
        print("The winner is tank1!")
        exit(0)
    else:
        pass

    who_shoots = input("Put in the tank that is shooting: ")

    if who_shoots == "tank1 shoot":
        tank1_shot()
    elif who_shoots == "tank2 shoot":
        tank2_shot()
    else:
        print("What did you write?")
