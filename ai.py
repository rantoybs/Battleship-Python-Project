import random

class Player:
    def __init__(self):
        self.grid = {}
        self.shipLocations = {}
        self.values = {}
        self.rand_x = 0
        self.rand_y = 0
        self.count = 0

    def get_ship_locations(self):
        return self.shipLocations

    def set_grid(self, grid):
        self.grid = grid

    def place_ships(self, block):
        getRandom = random.randint(0,3)
        if getRandom == 0:
            self.shipLocations = {
                'corvette': [[352.6751345948129, 181.47005383792515], [410.41016151377545, 181.47005383792515]]
                ,'sub': [[64.0, 66.0], [179.47005383792515, 66.0]]
                ,'carrier': [[237.20508075688772, 354.6751345948129], [410.41016151377545, 354.6751345948129]]
                    ,'destroyer': [[121.73502691896257, 470.145188432738], [352.6751345948129, 470.145188432738]]
            }
        elif getRandom == 1:
            self.shipLocations = {
                'corvette': [[294.9401076758503, 66.0], [352.6751345948129, 66.0]]
                , 'sub': [[64.0, 66.0], [179.47005383792515, 66.0]]
                , 'carrier': [[294.9401076758503, 470.145188432738], [468.14518843273805, 470.145188432738]]
                , 'destroyer': [[64.0, 412.41016151377545], [294.9401076758503, 412.41016151377545]]
            }
        elif getRandom == 2:
            self.shipLocations = {
                'corvette': [[179.47005383792515, 66.0], [237.20508075688772, 66.0]]
                , 'sub': [[237.20508075688772, 470.145188432738], [352.6751345948129, 470.145188432738]]
                , 'carrier': [[64.0, 239.20508075688772], [237.20508075688772, 239.20508075688772]]
                , 'destroyer': [[179.47005383792515, 354.6751345948129], [410.41016151377545, 354.6751345948129]]
            }
        elif getRandom == 3:
            self.shipLocations = {
                'corvette': [[237.20508075688772, 66.0], [294.9401076758503, 66.0]]
                , 'sub': [[294.9401076758503, 239.20508075688772], [410.4101615137755, 239.20508075688772]]
                , 'carrier': [[179.47005383792515, 470.145188432738], [352.6751345948129, 470.145188432738]]
                , 'destroyer': [[64.0, 296.9401076758503], [294.9401076758503, 296.9401076758503]]
            }


    def set_hit(self, is_hit):
        if is_hit:
            self.grid[self.rand_x] = 'H'

    def make_decision(self):
        self.rand_x = random.randint(0, 7)
        getKeys = list(self.grid.keys())
        self.values = self.grid[getKeys[self.rand_x]]

        self.rand_y = random.randint(0, 7)
        self.count = self.rand_y
        while (True):
            if self.values[self.count] != 'S' and self.values[self.count] != 'H':
                yReturnVal = self.values[self.count]
                self.values[self.count] = 'S'
                self.grid[getKeys[self.rand_x]] = self.values
                return [getKeys[self.rand_x], yReturnVal]

            elif self.count == 7:
                self.rand_x = random.randint(0, 7)
                self.values = self.grid[getKeys[self.rand_x]]
                self.rand_y = random.randint(0, 7)
                self.count = self.rand_y-1
            self.count += 1
