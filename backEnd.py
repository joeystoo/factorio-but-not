coordDict = {}

class Entity:
    def __init__(self, coords, coordDict):
        self.coords = coords
        self.width = 2
        self.height = 2
        coordDict[coords] = self