import copy

from agentes import AgenteHumano
from helper import *
from regras_jogo import Jogavel


class Board(Jogavel):
    JOGADOR_PADRAO = AgenteHumano()

    def registrarAgenteJogador(self, elemAgente=JOGADOR_PADRAO):
        self.jogadores.append(elemAgente)
        return self.jogadores.index(elemAgente)

    def isFim(self):
        if self.quantity <= 1:
            print('VOCÊ VENCEU, PARABÉNS! RESTA {}'.format(self.quantity))
            return True
        if self.quantity == 9999:
            return True

    def gerarCampoVisao(self, idAgente):
        # TODO: Ignorando id do agente
        print(self)
        return copy.deepcopy(self)

    def registrarProximaAcao(self, id_jogador, acao):
        self.jogadas[id_jogador] = acao

    def atualizarEstado(self, diferencial_tempo):
        # TODO: Hardcoded primeiro jogador
        command = self.jogadas.get(0)
        if command != 'sair':
            if command.find(';') != -1:
                coordinates = command.split(';')
                coordStart = list(map(int, coordinates[0].split(',')))
                coordEnd = list(map(int, coordinates[1].split(',')))
                try:
                    self.play(coordStart, coordEnd)
                except InvalidMove:
                    print('Movimento Inválido!')
            else:
                print('Comando inválido')

            print('Restam {}'.format(self.quantity))
        else:
            self.quantity = 9999


    def __init__(self):
        self.board_arr = []
        self.quantity = 0
        self.jogadores = []
        self.jogadas = dict()
        # Cria tabuleiro completo com peças
        [self.board_arr.append([Part(True) for _ in range(7)]) for _ in range(7)]
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

        self.quantity = self.quantify()

    def play(self, start, end):
        # Verifica Distância máxima do movimento
        if self.valida_jogada(start, end):
            # Verifica se há peça e se não foi removida
            part_start = self.board_arr[start[0]][start[1]]
            if part_start is not None and part_start.inside is not False:
                # Verifica se o destino é válido
                part_ent = self.board_arr[end[0]][end[1]]
                if part_ent is not None and part_ent.inside is False:
                    # Move peça
                    part_start.inside = False
                    part_ent.inside = True
                    # Remove Peça
                    jumped_xCoord = int((start[0] + end[0]) / 2)
                    jumped_yCoord = int((start[1] + end[1]) / 2)
                    self.board_arr[jumped_xCoord][jumped_yCoord].inside = False
                    # Atualiza contagem
                    self.quantity -= 1
                else:
                    raise InvalidMove
            else:
                raise InvalidMove
        else:
            raise InvalidMove

    def valida_jogada(self, start, end):
        if abs(start[0] - end[0]) == 2 and abs(start[1] - end[1]) == 0:
            return True
        if abs(start[0] - end[0]) == 0 and abs(start[1] - end[1]) == 2:
            return True
        return False


    def quantify(self):
        count = 0
        for x in self.board_arr:
            count += sum([1 if part is not None and part.inside is True else 0 for part in x])
        return count

    def __repr__(self):
        return_str = '   0 1 2 3 4 5 6\n \n'
        for n, x in enumerate(self.board_arr):
            return_str += '{}  '.format(n)
            for y in x:
                if y is None:
                    return_str += '  '
                else:
                    return_str += '1 ' if y.inside == True else '0 '
            return_str += '\n'
        return return_str


class Part(object):
    inside = False

    def __init__(self, inside):
        self.inside = inside

    def rem(self):
        self.inside = False
