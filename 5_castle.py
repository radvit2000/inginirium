from mcpi.minecraft import Minecraft
mc = Minecraft.create()

place = mc.player.getPos()
x, y, z = place.x + 10, place.y, place.z

mc.setBlocks(x, y, z, x + 10, y + 10, z + 10, 1)
mc.setBlocks(x + 1, y + 1, z + 1, x + 9, y + 10, z + 9, 0)

x = x - 4
z = z - 4
mc.setBlocks(x, y, z, x + 4, y + 10, z + 4, 1)
mc.setBlocks(x + 1, y + 1, z + 1, x + 3, y + 10, z + 3, 0)

x = x + 14
mc.setBlocks(x, y, z, x + 4, y + 10, z + 4, 1)
mc.setBlocks(x + 1, y + 1, z + 1, x + 3, y + 10, z + 3, 0)

z = z + 14
mc.setBlocks(x, y, z, x + 4, y + 10, z + 4, 1)
mc.setBlocks(x + 1, y + 1, z + 1, x + 3, y + 10, z + 3, 0)

x = x - 14
mc.setBlocks(x, y, z, x + 4, y + 10, z + 4, 1)
mc.setBlocks(x + 1, y + 1, z + 1, x + 3, y + 10, z + 3, 0)
