from mcpi.minecraft import Minecraft
mc = Minecraft.create()

place = mc.player.getPos()
x, y, z = place.x, place.y, place.z

# снеговик
mc.setBlock(x, y, z, 80)
mc.setBlock(x, y + 1, z, 80)
mc.setBlock(x, y + 2, z, 86)

# голем
mc.setBlock(x, y, z, 42)
mc.setBlock(x, y + 1, z, 42)
mc.setBlock(x + 1, y + 1, z, 42)
mc.setBlock(x - 1, y + 1, z, 42)
mc.setBlock(x, y + 2, z, 86)