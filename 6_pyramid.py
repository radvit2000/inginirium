from mcpi.minecraft import Minecraft
mc = Minecraft.create()

place = mc.player.getPos()
x, y, z = place.x, place.y, place.z

mc.setBlocks(x, y, z, x + 4, y, z + 4, 57)
mc.setBlocks(x + 1, y + 1, z + 1, x + 3, y + 1, z + 3, 57)
mc.setBlock(x + 2, y + 2, z + 2, 57)
