from mcpi.minecraft import Minecraft
mc = Minecraft.create()

place = mc.player.getPos()
x, y, z = place.x, place.y, place.z

for i in range(20):
    mc.setBlock(x + i, y + i, z, 53)