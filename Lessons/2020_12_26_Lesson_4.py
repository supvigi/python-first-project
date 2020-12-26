def punk_2(func):
    def punk_3(x5, x6):
        print("___________")
        func(x5, x6)

    return punk_3


@punk_2
def punk_1(x3, x4):
    print("|{} * {} =".format(x3, x4), x3 * x4, "|")


for x in range(1, 11):
    for x2 in range(1, 11):
        punk_1(x, x2)

print("-----------")

class normal_tank:
    type = "Special forces"
    weaponized = True

    def __init__(self, prim_weap, armr, ammo, sec_weap):
        self.primary_weapon = prim_weap
        self.armor = armr
        self.ammunition = ammo
        self.secondary_weapon = sec_weap

    def shoot_primary_weapon(self):
        self.ammunition -= 1
        print("Reach! Ammo left:", self.ammunition)


tank1 = normal_tank("80-mm primary weapon", 100, 50, "10-mm secondary weapon")
tank2 = normal_tank("")
