import time

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

place = mc.player.getPos()
x, y, z = place.x, place.y, place.z

mc.setBlocks(x, y, z, x + 10, y + 10, z + 10, 2)
mc.setBlocks(x + 1, y + 1, z + 1, x + 9, y + 9, z + 9, 0)

mc.postToChat('to get pasword')
pasword = input()
if pasword == '123':
    mc.setBlocks(x + 4, y + 1, z, x + 5, y + 2, z, 0)
    time.sleep(5)
    mc.setBlocks(x + 4, y + 1, z, x + 5, y + 2, z, 2)
else:
    place = mc.player.getPos()
    x, y, z = place.x, place.y, place.z

    mc.setBlock(x, y - 1, z, 10)