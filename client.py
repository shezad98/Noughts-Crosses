import pygame
from player import Player
from network import Network
import pickle
from game import Game, Turn

width = 602
height = 602
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)


def redrawWindow(win, game, symbol):
    win.fill((255, 255, 255))
    if game.winner == 'neither':

        pygame.draw.line(win, (0, 0, 0), (0, 201), (602, 201), 1)
        pygame.draw.line(win, (0, 0, 0), (0, 402), (602, 402), 1)
        pygame.draw.line(win, (0, 0, 0), (201, 0), (201, 602), 1)
        pygame.draw.line(win, (0, 0, 0), (402, 0), (402, 602), 1)
        for i in game.p1moves:
            if i != (100, 100):
                game.draw(i, win, 'circle')
        for i in game.p2moves:
            if i != (100, 100):
                game.draw(i, win, 'cross')
    elif game.winner == 'circle':
        if symbol == 'circle':
            textsurface = myfont.render('You win!', False, (0, 0, 0))
        else:
            textsurface = myfont.render('You lose!', False, (0, 0, 0))
        win.blit(textsurface, (100,100))
    elif game.winner == 'cross':
        if symbol == 'cross':
            textsurface = myfont.render('You win!', False, (0, 0, 0))
        else:
            textsurface = myfont.render('You lose!', False, (0, 0, 0))
        win.blit(textsurface, (100,100))

    pygame.display.update()


def get_coord(tup):
    return tup[0] // 201, tup[1] // 201

def other_one(p):
    if p == "circle":
        return "cross"
    else:
        return "circle"

def swap_turn(game):
    if game.turn == "circle":
        game.turn = "cross"
    else:
        game.turn = "circle"

def main():
    run = True
    n = Network()
    symb = n.getP()
    print(symb)
    pos = (100, 100)
    game = Game("circle")
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = get_coord(pygame.mouse.get_pos())
                game = n.send(Turn(symb, pos))
                pos = (100,100)
        game = n.send(Turn(symb,pos))
        # if pos not in game.p1moves and pos not in game.p2moves:
        #     game.p1moves.append(pos)

        redrawWindow(win, game, symb)


main()
