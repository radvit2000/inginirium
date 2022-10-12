import random
import time

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

place = mc.player.getPos()
x, y, z = place.x, place.y, place.z

while True:
    x = random.randint(-1000, 1000)
    y = random.randint(80, 150)
    z = random.randint(-1000, 1000)
    mc.player.setPos(x, y, z)
    time.sleep(3)