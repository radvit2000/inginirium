from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mod = True
while True:
    hit = mc.events.pollBlockHits()

    if len(hit) > 0 and mod:
        x1 = hit[0].pos.x
        y1 = hit[0].pos.y
        z1 = hit[0].pos.z
        mod = False

    hit = mc.events.pollBlockHits()

    if len(hit) > 0 and not mod:
        x2 = hit[0].pos.x
        y2 = hit[0].pos.y
        z2 = hit[0].pos.z
        mc.postToChat('give id')
        block = int(input('введи айди'))
        mc.setBlocks(x1, y1, z1, x2, y2, z2, block)
        mod = True