import time

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
score = 0
while True:
    place = mc.player.getPos()
    x, y, z = place.x, place.y, place.z

    block = mc.getBlock(x, y + 1, z)

    if block == 8 or block == 9:
        score += 1
    else:
        score = 0
    mc.postToChat(score)
    time.sleep(1)