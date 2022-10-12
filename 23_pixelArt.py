from mcpi.minecraft import Minecraft
mc = Minecraft.create()

place = mc.player.getPos()
x, y, z = place.x, place.y, place.z

smile = [[0, 1, 1, 1, 0],
         [1, 0, 0, 0, 1],
         [0, 0, 0, 0, 0],
         [0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0]]
for i in range(5):
    for j in range(5):
        mc.setBlock(x + j, y + i, z, smile[i][j])