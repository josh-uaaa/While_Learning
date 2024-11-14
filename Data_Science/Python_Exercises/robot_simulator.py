EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3

ROTATIONS = ([SOUTH, EAST, NORTH, WEST], [NORTH, WEST, SOUTH, EAST])
ADVANCES = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, moves):
        for move in moves:
            if move == 'R':
                self.direction = ROTATIONS[0][self.direction]
            elif move == 'L':
                self.direction = ROTATIONS[1][self.direction]
            else:
                self.coordinates = tuple(map(sum, zip(self.coordinates, ADVANCES[self.direction])))