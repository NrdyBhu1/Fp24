import pygame, sys, math
import config
from pygame.locals import *
from scripts.button import Button
from scripts.font import Font
from scripts.text import Text

pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
pygame.display.set_caption("Fp24")
font = Font("./assets/fonts/m6x11.ttf")
global STATE
STATE = config.MENU_STATE

def terminate():
    pygame.quit()
    sys.exit()

def enter_game():
    STATE = config.GAME_STATE

def exit_game():
    STATE = config.END_STATE

def menu():
    title = Text("Fp24", font, (400, 50))
    play = Button(400, 350, 500, 100, "Play", font, enter_game)
    settings = Button(400, 450, 500, 100, "Settings", font, enter_game)
    quit = Button(400, 550, 500, 100, "Quit", font, terminate)
    while STATE == config.MENU_STATE:
        quit.hovered()
        quit.clicked()

        play.hovered()
        play.clicked()

        settings.hovered()
        settings.clicked()

        for event in pygame.event.get():
            if event.type == QUIT:
                exit_game()
                break

        win.fill((0, 0, 0))
        title.render(win, 300)
        play.render(win)
        settings.render(win)
        quit.render(win)
        pygame.display.update()
        clock.tick(config.FPS)


def game():
    while STATE == config.GAME_STATE:

        for event in pygame.event.get():
            if event.type == QUIT:
                exit_game()
                break

        win.clear()
        win.fill((0, 0, 0))
        pygame.display.update()
        clock.tick(config.FPS)

if __name__ == "__main__":
    menu()
    if STATE == config.GAME_STATE:
        game()
    else:
        terminate()
