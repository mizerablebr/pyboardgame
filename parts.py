class Board(object):
    board_arr = []

    def __init__(self):
        # Cria tabuleiro completo com peças
        [self.board_arr.append([Part(x, y, True) for y in range(7)]) for x in range(7)]
        # Ajusta tabuleiro
        # Superior
        self.board_arr[0][:1] = [None, None]
        self.board_arr[1][:1] = [None, None]
        self.board_arr[0][-2:] = [None, None]
        self.board_arr[1][-2:] = [None, None]
        # Inferior
        self.board_arr[5][:1] = [None, None]
        self.board_arr[6][:1] = [None, None]
        self.board_arr[5][-2:] = [None, None]
        self.board_arr[6][-2:] = [None, None]

        # Remove peça do meio
        self.board_arr[3][3].rem()


class Part(object):
    xcoord = 0
    ycoord = 0
    inside = False


    def __init__(self, x, y, inside):
        self.xcoord = x
        self.ycoord = y
        self.inside = inside

    def rem(self):
        self.inside = False

