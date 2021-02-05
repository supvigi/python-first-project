def reach_or_not(x2, y2, a2):
    if x2 * y2 > a2 * 1753:
        print("Enemy down!")
        exit(0)
    elif x2 * y2 < a2 * 1753:
        print("Reach, but in the armor!")


reach_x = input("Put in the reach ability of the bullet:")
speed_y = input("Put in the speed of the bullet: ")
armor_a = input("Put in the armor length: ")

reach_or_not(reach_x, speed_y, armor_a)
