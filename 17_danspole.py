import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
q = mc.player.getPos()
x, y, z = q.x, q.y, q.z
while True:
    i = 0
    while i < 5:
        j = 0
        while j < 5:
            r = random.randint(0, 15)
            mc.setBlock(x + i, y, z + j, 35,r)
            j += 1
        i += 1