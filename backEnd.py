from frontEnd import run

from furnace import Furnace
from inserter import Inserter

coordDict = {}
objects = []
playerSpeed = 10

class Entity:
    def __init__(self, coords, data):
        self.coords = coords
        self.data = data
        coordDict[coords] = self
        objects.append(self)

class Player:
    def __init__(self):
        self.coords = [0,0]
player = Player()
for i in range(100):
    for j in range(100):
        Entity((i * 2,j * 2), Furnace())


while True:
    keypresses = run(objects, player)
    if keypresses[0] == 1:
        player.coords[1] = player.coords[1] - (1 * playerSpeed)
    if keypresses[1] == 1:
        player.coords[0] = player.coords[0] - (1 * playerSpeed)
    if keypresses[2] == 1:
        player.coords[1] = player.coords[1] + (1 * playerSpeed)
    if keypresses[3] == 1:
        player.coords[0] = player.coords[0] + (1 * playerSpeed)
    print(player.coords)
    