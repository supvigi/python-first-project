from random import randint


def light_tank_shoot():
    fire = 1
    reach_or_not = randint(1, 6)

    if reach_or_not == 1:
        heavy_tank_1.health -= light_tank_2.weapon
        light_tank_2.ammunition -= 1
        print("Reach! Tank 1 health:", heavy_tank_1.health, "Tank 2 ammo:", light_tank_2.ammunition)
    elif reach_or_not == 2:
        if heavy_tank_1.armor <= 0:
            heavy_tank_1.health -= light_tank_2.weapon
            light_tank_2.ammunition -= 1
            print("Reach, but you got the armor, but the armor is broken, so you got the tank 1 itself! "
                  "Tank 1 health:", heavy_tank_1.health, "Tank 2 ammo:", light_tank_2.ammunition)
        else:
            heavy_tank_1.armor -= light_tank_2.weapon
            light_tank_2.ammunition -= 1
            print("Reach, but you got the armor! "
                  "Tank 1 armor:", heavy_tank_1.armor, "Tank 2 ammo:", light_tank_2.ammunition)
    elif reach_or_not == 3:
        heavy_tank_1.health -= light_tank_2.weapon
        heavy_tank_1.health -= fire
        light_tank_2.ammunition -= 1
        print("Reach and bonus, Tank 1 is burning! "
              "Tank 1 health:", heavy_tank_1.health, "Tank 2 ammo:", light_tank_2.ammunition)
    elif reach_or_not == 4:
        heavy_tank_1.health -= light_tank_2.weapon * 2
        light_tank_2.ammunition -= 1
        print("Reach and bonus, Tank 1 got critical! "
              "Tank 1 health:", heavy_tank_1.health, "Tank 2 ammo:", light_tank_2.ammunition)
    elif reach_or_not == 5:
        light_tank_2.ammunition -= 1
        print("Miss! Tank 1 health:", heavy_tank_1.health, "Tank 2 ammo:", light_tank_2.ammunition)
    elif reach_or_not == 6:
        if heavy_tank_1.speed == 1:
            light_tank_2.ammunition -= 1
            heavy_tank_1.speed = 0
            print("Miss, tank 1 used the speed ability and dodged the bullet! "
                  "Tank 1 health:", heavy_tank_1.health, "Tank 2 ammo:", light_tank_2.ammunition)
        elif heavy_tank_1.speed == 0:
            heavy_tank_1.health -= light_tank_2.weapon
            light_tank_2.ammunition -= 1
            print("Reach! Tank 1 health:", heavy_tank_1.health, "Tank 2 ammo:", light_tank_2.ammunition)
    if light_tank_2.ammunition <= 0:
        print("The winner is tank 1!")
        exit(0)
    elif heavy_tank_1.health <= 0:
        print("The winner is tank 2!")
        exit(0)
    else:
        pass


def heavy_tank_shoot():
    fire2 = 1
    reach_or_not2 = randint(1, 6)

    if reach_or_not2 == 1:
        light_tank_2.health -= heavy_tank_1.weapon
        heavy_tank_1.ammunition -= 1
        print("Reach! Tank 2 health:", light_tank_2.health, "Tank 1 ammo:", heavy_tank_1.ammunition)
    elif reach_or_not2 == 2:
        if light_tank_2.armor <= 0:
            light_tank_2.health -= heavy_tank_1.weapon
            heavy_tank_1.ammunition -= 1
            print("Reach, but you got the armor, but the armor is broken, so you got the tank 2 itself! "
                  "Tank 2 health:", light_tank_2.health, "Tank 1 ammo:", heavy_tank_1.ammunition)
        else:
            light_tank_2.armor -= heavy_tank_1.weapon
            heavy_tank_1.ammunition -= 1
            print("Reach, but you got the armor! "
                  "Tank 2 armor:", light_tank_2.armor, "Tank 1 ammo:", heavy_tank_1.ammunition)
    elif reach_or_not2 == 3:
        light_tank_2.health -= heavy_tank_1.weapon
        light_tank_2.health -= fire2
        heavy_tank_1.ammunition -= 1
        print("Reach and bonus, Tank 2 is burning! "
              "Tank 2 health:", light_tank_2.health, "Tank 1 ammo:", heavy_tank_1.ammunition)
    elif reach_or_not2 == 4:
        light_tank_2.health -= heavy_tank_1.weapon * 2
        heavy_tank_1.ammunition -= 1
        print("Reach and bonus, Tank 2 got critical! "
              "Tank 2 health:", light_tank_2.health, "Tank 1 ammo:", heavy_tank_1.ammunition)
    elif reach_or_not2 == 5:
        print("Miss! Tank 2 health:", light_tank_2.health, "Tank 1 ammo:", heavy_tank_1.ammunition)
    elif reach_or_not2 == 6:
        if light_tank_2.speed is True:
            heavy_tank_1.ammunition -= 1
            light_tank_2.speed = False
            print("Miss, tank 2 used the speed ability and dodged the bullet! "
                  "Tank 2 health:", light_tank_2.health, "Tank 1 ammo:", heavy_tank_1.ammunition)
        elif light_tank_2.speed is False:
            light_tank_2.health -= heavy_tank_1.weapon
            heavy_tank_1.ammunition -= 1
            print("Reach! Tank 2 health:", light_tank_2.health, "Tank 1 ammo:", heavy_tank_1.ammunition)
    if heavy_tank_1.ammunition <= 0:
        print("The winner is tank 2!")
        exit(0)
    elif light_tank_2.health <= 0:
        print("The winner is tank 1!")
        exit(0)
    else:
        pass


class Tank:

    def __init__(self, wp, arm, hp, ammo, spd):
        self.weapon = wp
        self.armor = arm
        self.health = hp
        self.ammunition = ammo
        self.speed = spd


heavy_tank_1 = Tank(15, 70, 330, 100, False)
light_tank_2 = Tank(30, 100, 300, 50, False)

while True:
    move = input("Put in who shoots, or use the power of dodge: ")

    if move == "tank1 shoot" or move == "Tank1 shoot":
        heavy_tank_shoot()
    elif move == "tank2 shoot" or move == "Tank2 shoot":
        light_tank_shoot()
    elif move == "tank1 speed" or move == "Tank1 speed":
        heavy_tank_1.speed = True
    elif move == "tank2 speed" or move == "Tank2 speed":
        light_tank_2.speed = True
    else:
        print("What did you write?")
