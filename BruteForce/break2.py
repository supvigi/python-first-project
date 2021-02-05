from mcpi.minecraft import Minecraft

mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

mc.setBlock(x + 1, y, z, 0)
mc.setBlock(x - 1, y, z, 0)
mc.setBlock(x, y, z + 1, 0)
mc.setBlock(x, y, z - 1, 0)
mc.setBlock(x, y + 2, z, 0)
mc.setBlock(x, y + 3, z, 0)

while True:
    if x == -302 and y == 63 and z == 225:
        mc.setBlock(x + 1, y, z, 160)
        mc.setBlock(x - 1, y, z, 160)
        mc.setBlock(x, y, z + 1, 160)
        mc.setBlock(x, y, z - 1, 160)
        mc.setBlock(x, y + 2, z, 160)
        mc.setBlock(x, y + 3, z, 8)
        exit(0)
