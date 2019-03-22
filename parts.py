class Board(object):
    board_arr = []

    def __init__(self):
        for x in range(7):
            for y in range(7):
                self.board_arr[x][y] = Part(x, y)


class Part(object):
    xcoord = 0
    ycoord = 0


    def __init__(self, x, y):
        self.xcoord = x
        self.ycoord = y
