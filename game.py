import pygame

class Game:
    def __init__(self, turn):
        self.turn = turn
        self.p1moves = []
        self.p2moves = []
        self.winner = 'neither'

    def draw(self, coord, win, symbol):
        coord = coord[0] * 201 + 100, coord[1] * 201 + 100
        if symbol == "circle":
            pygame.draw.circle(win, (0, 0, 0), coord, 20, 5)
        else:
            pygame.draw.line(win, (0, 0, 0), (coord[0] - 20, coord[1] - 20), (coord[0] + 20, coord[1] + 20), 5)
            pygame.draw.line(win, (0, 0, 0), (coord[0] + 20, coord[1] - 20), (coord[0] - 20, coord[1] + 20), 5)

    def change_turn(self):
        if self.turn == 'circle':
            self.turn = 'cross'
        else:
            self.turn = 'circle'

    def add_move(self, move):
        if move.symbol == 'circle':
            self.p1moves.append(move.coord)
        else:
            self.p2moves.append(move.coord)

    def valid_move(self, move):
        if self.turn == move.symbol and move.coord != (100,100):
            if move.coord not in self.p1moves and move.coord not in self.p2moves:
                return True
            else:
                return False
        else:
            return False

    def check_victory(self):
        win_possibilities = [[(0,0), (0,1), (0,2)],
                             [(0,0), (1,0), (2,0)],
                             [(0,0), (1,1), (2,2)],
                             [(0,1), (1,1), (2,1)],
                             [(0,2), (1,2), (2,2)],
                             [(0,0), (0,1), (0,2)],
                             [(0,0), (0,1), (0,2)],
                             [(0,0), (0,1), (0,2)],
                             [(0,0), (0,1), (0,2)]]
        for poss in win_possibilities:
            if all([x in self.p1moves for x in poss]):
                self.winner = 'circle'
            elif all([x in self.p2moves for x in poss]):
                self.winner = 'cross'
            else:
                self.winner = 'neither'

    def __str__(self):
        return self.winner

class Turn:
    def __init__(self, symbol, coord):
        self.symbol = symbol
        self.coord = coord

    def __str__(self):
        return self.symbol + str(self.coord)
