import time

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

place = mc.player.getPos()
x, y, z = place.x, place.y, place.z

mc.setBlocks(x, y + 100, z, x + 20, y + 100, z + 20, 1)
mc.setBlocks(x, y + 101, z, x + 20, y + 101, z + 20, 12)

mc.player.setPos(x, y + 110, z)
y += 110
time.sleep(3)
while y > 100:
    place = mc.player.getPos()
    x, y, z = place.x, place.y, place.z

    mc.setBlock(x, y - 2, z, 0)
