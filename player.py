import pygame


class Player:
    def __init__(self, symbol, turn):
        self.symbol = symbol
        self.moves = []
        self.turn = turn

    def draw(self, coord, win):
        coord = coord[0] * 201 + 100, coord[1] * 201 +100
        if self.symbol == "circle":
            pygame.draw.circle(win, (0, 0, 0), coord, 20, 5)
        else:
            pygame.draw.line(win, (0, 0, 0), (coord[0] - 20, coord[1] - 20), (coord[0] + 20, coord[1] + 20), 5)
            pygame.draw.line(win, (0, 0, 0), (coord[0] + 20, coord[1] - 20), (coord[0] - 20, coord[1] + 20), 5)
