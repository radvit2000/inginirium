from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    hit = mc.events.pollBlockHits()
    if len(hit) > 0:
        mc.setBlock(hit[0].pos.x, hit[0].pos.y, hit[0].pos.z, 41)