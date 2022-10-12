from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def star(x, y, z, lenght, blockId):
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

place = mc.player.getPos()
x, y, z = place.x + 10, place.y, place.z

for i in range(0, 24, 4):
    star(x + i, y, z, 4, 57)
    star(x - i, y, z, 4, 57)
    star(x, y + i, z, 4, 57)
    star(x, y - i, z, 4, 57)
    star(x, y, z + i, 4, 57)
    star(x, y, z - i, 4, 57)

    star(x + i, y + i, z, 4, 57)
    star(x - i, y + i, z, 4, 57)
    star(x, y + i, z + i, 4, 57)
    star(x, y + i, z - i, 4, 57)

    star(x + i, y - i, z, 4, 57)
    star(x - i, y - i, z, 4, 57)
    star(x, y - i, z + i, 4, 57)
    star(x, y - i, z - i, 4, 57)

    star(x + i, y, z + i, 4, 57)
    star(x + i, y, z - i, 4, 57)
    star(x - i, y, z + i, 4, 57)
    star(x - i, y, z - i, 4, 57)

    star(x + i, y + i, z + i, 4, 57)
    star(x + i, y + i, z - i, 4, 57)
    star(x - i, y + i, z + i, 4, 57)
    star(x - i, y + i, z - i, 4, 57)

    star(x + i, y - i, z + i, 4, 57)
    star(x + i, y - i, z - i, 4, 57)
    star(x - i, y - i, z + i, 4, 57)
    star(x - i, y - i, z - i, 4, 57)