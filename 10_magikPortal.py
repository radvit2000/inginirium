from mcpi.minecraft import Minecraft
mc = Minecraft.create()

place = mc.player.getPos()
x, y, z = place.x, place.y, place.z

down = mc.getBlock(x, y - 1, z)
up = mc.getBlock(x, y + 2, z)
front = mc.getBlock(x + 1, y, z)
frontUp = mc.getBlock(x + 1, y + 1, z)
back = mc.getBlock(x - 1, y, z)
backUp = mc.getBlock(x - 1, y + 1, z)
leftUp = mc.getBlock(x, y + 1, z - 1)
rightUp = mc.getBlock(x, y + 1, z + 1)
left = mc.getBlock(x, y, z - 1)
right = mc.getBlock(x, y, z + 1)

if down == 57 and up == 57 and (front == 57 or right == 57) and (frontUp == 57 or rightUp == 57) and (back == 57 or left == 57) and (backUp == 57 or leftUp == 57):
    mc.setBlocks(x + 5, y, z + 5, x + 5, y + 15, z + 5, 57)
