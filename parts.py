from helper import *


class Board(object):
    board_arr = []

    def __init__(self):
        # Cria tabuleiro completo com peças
        [self.board_arr.append([Part(x, y, True) for y in range(7)]) for x in range(7)]
        # Ajusta tabuleiro
        # Superior
        self.board_arr[0][:1] = [None, None]
        self.board_arr[1][:1] = [None, None]
        self.board_arr[0][-3:] = [None, None]
        self.board_arr[1][-3:] = [None, None]
        # Inferior
        self.board_arr[5][:1] = [None, None]
        self.board_arr[6][:1] = [None, None]
        self.board_arr[5][-3:] = [None, None]
        self.board_arr[6][-3:] = [None, None]

        # Remove peça do meio
        self.board_arr[3][3].rem()

    def play(self, start, end):
        # Verifica Distância máxima do movimento
        if abs(start[0] - end[0]) <= 2 and abs(start[1] - end[1]) <= 2:
            # Verifica se há peça e se não foi removida
            part_start = self.board_arr[start[0]][start[1]]
            if part_start is not None and part_start.inside != False:
                # Verifica se o destino é válido
                part_ent = self.board_arr[end[0]][end[1]]
                if part_ent is not None and part_ent.inside == False:
                    part_start.inside = False
                    part_ent.inside = True
        else:
            raise InvalidMove

    def __repr__(self):
        return_str = ''
        for x in self.board_arr:
            for y in x:
                if y is None:
                    return_str += ' '
                else:
                    return_str += '1' if y.inside == True else '0'
            return_str += '\n'
        return return_str


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
