import random

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

place = mc.player.getPos()
x, y, z = place.x, place.y, place.z

while True:
    place = mc.player.getPos()
    x, y, z = place.x, place.y, place.z

    block = random.randint(0, 150)
    mc.setBlock(x, y + 2, z, block)
