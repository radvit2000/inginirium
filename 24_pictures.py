from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def smile(x, y, z, id):
    smile = [[0, 1, 1, 1, 0],
             [1, 0, 0, 0, 1],
             [0, 0, 0, 0, 0],
             [0, 1, 0, 1, 0],
             [0, 1, 0, 1, 0]]

    for i in range(5):
        for j in range(5):
            if smile[i][j] == 1:
                mc.setBlock(x + j, y + i, z, id)

def square(x, y, z, id):
    smile = [[1, 1, 1, 1, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 1, 1, 1, 1]]

    for i in range(5):
        for j in range(5):
            if smile[i][j] == 1:
                mc.setBlock(x + j, y + i, z, id)

def chess(x, y, z, id):
    smile = [[0, 1, 0, 1, 0],
             [1, 0, 1, 0, 1],
             [0, 1, 0, 1, 0],
             [1, 0, 1, 0, 1],
             [0, 1, 0, 1, 0]]

    for i in range(5):
        for j in range(5):
            if smile[i][j] == 1:
                mc.setBlock(x + j, y + i, z, id)
place = mc.player.getPos()
x, y, z = place.x, place.y, place.z

mc.postToChat('check picture')
picture = int(input('выбери картину 1)смайлик 2)квадрат 3)шахматы'))
id = int(input('выбери материал'))
if picture == 1:
    smile(x, y, z, id)
elif picture == 2:
    square(x, y, z, id)
elif picture == 3:
    chess(x, y, z, id)