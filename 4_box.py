from mcpi.minecraft import Minecraft
mc = Minecraft.create()

place = mc.player.getPos()
x, y, z = place.x, place.y, place.z

length = 5  # длина
width = 5  # ширина
height = 5  # высота
mc.setBlocks(x, y, z, x + length - 1, y + height - 1, z + width - 1, 57)
mc.setBlocks(x + 1, y + 1, z + 1, x + length - 2, y + height - 2, z + width - 2, 0)
