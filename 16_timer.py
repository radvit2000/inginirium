import time

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

place = mc.player.getPos()
x, y, z = place.x, place.y, place.z

mc.setBlocks(x, y, z, x, y + 5, z, 20)
i = 0
mod = True
while True:
    if mod:
        block = 22
    else:
        block = 20

    mc.setBlock(x, y + i, z, block)
    i += 1

    if i > 5:
        i = 0
        mod = not mod

    time.sleep(1)