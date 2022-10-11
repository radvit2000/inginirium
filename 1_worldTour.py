import time

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.player.setPos(100, 100, 100)
time.sleep(2)
mc.player.setPos(923, 106, 156)
time.sleep(2)
mc.player.setPos(778, 79, 74)
time.sleep(2)
mc.player.setPos(-183, 81, 177)
time.sleep(2)
mc.player.setPos(-275, 113, -87)
time.sleep(2)
