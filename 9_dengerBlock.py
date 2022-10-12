from mcpi.minecraft import Minecraft
mc = Minecraft.create()

place = mc.player.getPos()
x, y, z = place.x, place.y, place.z

block = mc.getBlock(x, y - 1, z)
if block == 57:
    mc.setBlock(x, y, z, 10)
    mc.setBlock(x, y - 1, z, 10)
    mc.setBlock(x, y + 1, z, 10)