from mcpi.minecraft import Minecraft
mc = Minecraft.create()

air = 0
water = 9
java = 10

while True:
    pos = mc.player.getTilePos()
    blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)

    if blockBelow == 0 or blockBelow == 9 or blockBelow == 10 or blockBelow == 8 or blockBelow == 11:
        pass
    else:
        mc.setBlock(pos.x, pos.y - 1, pos.z, 41)
