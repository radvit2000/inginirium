from mcpi.minecraft import Minecraft
mc = Minecraft.create()

place = mc.player.getPos()
x, y, z = place.x, place.y, place.z

mc.player.setPos(x, y + 10, z)