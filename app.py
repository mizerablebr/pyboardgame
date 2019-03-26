from parts import *

if __name__ == "__main__":
    board = Board()

    command = ''

    while command != 'sair':
        print(board)
        print('Restam {}'.format(board.quantity))
        print('Digite a origem e o destino ou \'sair\': x0,y0;x1,y0')
        command = input()
        if command.find(';') != -1:
            coordinates = command.split(';')
            coordStart = list(map(int, coordinates[0].split(',')))
            coordEnd = list(map(int, coordinates[1].split(',')))
            try:
                board.play(coordStart, coordEnd)
            except InvalidMove:
                print('Movimento Inválido!')
        else:
            print('Comando inválido')


