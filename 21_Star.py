from mcpi.minecraft import Minecraft
mc = Minecraft.create()

place = mc.player.getPos()
x, y, z = place.x + 7, place.y, place.z

lenght = 5
blockId = 57
for i in range(lenght):
    mc.setBlock(x + i, y + i, z + i, blockId)
    mc.setBlock(x - i, y + i, z + i, blockId)
    mc.setBlock(x + i, y + i, z - i, blockId)
    mc.setBlock(x - i, y + i, z - i, blockId)

    mc.setBlock(x + i, y - i, z + i, blockId)
    mc.setBlock(x - i, y - i, z + i, blockId)
    mc.setBlock(x + i, y - i, z - i, blockId)
    mc.setBlock(x - i, y - i, z - i, blockId)

    mc.setBlock(x, y + i, z, blockId)
    mc.setBlock(x, y - i, z, blockId)
    mc.setBlock(x + i, y, z, blockId)
    mc.setBlock(x - i, y, z, blockId)
    mc.setBlock(x, y, z + i, blockId)
    mc.setBlock(x, y, z - i, blockId)

    mc.setBlock(x, y - i, z - i, blockId)
    mc.setBlock(x, y - i, z + i, blockId)
    mc.setBlock(x - i, y - i, z, blockId)
    mc.setBlock(x + i, y - i, z, blockId)

    mc.setBlock(x, y + i, z - i, blockId)
    mc.setBlock(x, y + i, z + i, blockId)
    mc.setBlock(x - i, y + i, z, blockId)
    mc.setBlock(x + i, y + i, z, blockId)

    mc.setBlock(x + i, y, z + i, blockId)
    mc.setBlock(x - i, y, z + i, blockId)
    mc.setBlock(x + i, y, z - i, blockId)
    mc.setBlock(x - i, y, z - i, blockId)