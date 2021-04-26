import pygame, sys, math
import config
from pygame.locals import *
from scripts.button import Button, RadioButton
from scripts.font import Font
from scripts.text import Text
from scripts.player import Player
from scripts.coin import Coin

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
    global STATE
    STATE = config.GAME_STATE

def enter_menu():
    global STATE
    STATE = config.MENU_STATE

def exit_game():
    global STATE
    STATE = config.END_STATE

def enter_settings():
    global STATE
    STATE = config.SETTINGS_STATE

def menu():
    title = Text("Fp24", font, (400, 50))
    play = Button(400, 350, 500, 100, "Play", font, enter_game)
    go_settings = Button(400, 450, 500, 100, "Settings", font, enter_settings)
    quit = Button(400, 550, 500, 100, "Quit", font, exit_game)
    while STATE == config.MENU_STATE:
        quit.hovered()
        play.hovered()
        go_settings.hovered()

        for event in pygame.event.get():
            if event.type == QUIT:
                exit_game()
                break
            if event.type == MOUSEBUTTONDOWN:
                go_settings.clicked(event)
                play.clicked(event)
                quit.clicked(event)

        win.fill((0, 0, 0))
        title.render(win, 300)
        play.render(win)
        go_settings.render(win)
        quit.render(win)
        pygame.display.update()
        clock.tick(config.FPS)

    if STATE == config.MENU_STATE:
        menu()
    elif STATE == config.GAME_STATE:
        game()
    elif STATE == config.SETTINGS_STATE:
        settings()
    elif STATE == config.END_STATE:
        terminate()


def game():
    player = Player()
    coin = Coin((100, 100), 128)
    back = Button(50, 550, 100, 100, "Q", font, enter_menu)
    while STATE == config.GAME_STATE:
        back.hovered()
        for event in pygame.event.get():
            if event.type == QUIT:
                exit_game()
                break
            if event.type == MOUSEBUTTONDOWN:
                back.clicked(event)
            player.move(event)

        win.fill((0, 0, 0))
        player.render(win)
        coin.render(win)
        back.render(win)
        pygame.display.update()
        clock.tick(config.FPS)

    if STATE == config.MENU_STATE:
        menu()
    elif STATE == config.GAME_STATE:
        game()
    elif STATE == config.SETTINGS_STATE:
        settings()
    elif STATE == config.END_STATE:
        terminate()


def settings():
    play_music = RadioButton(100, 100, 50, "Play Music", font)
    play_sounds = RadioButton(100, 180, 50, "Play Sounds", font)
    back = Button(50, 550, 100, 100, "<", font, enter_menu)
    while STATE == config.SETTINGS_STATE:
        play_music.hovered()
        play_sounds.hovered()
        back.hovered()
        for event in pygame.event.get():
            if event.type == QUIT:
                exit_game()
                break
            if event.type == MOUSEBUTTONDOWN:
                back.clicked(event)
                play_music.clicked(event)
                play_sounds.clicked(event)

        win.fill((0, 0, 0))
        play_music.render(win)
        play_sounds.render(win)
        back.render(win)
        pygame.display.update()
        clock.tick(config.FPS)

    if STATE == config.MENU_STATE:
        menu()
    elif STATE == config.GAME_STATE:
        game()
    elif STATE == config.SETTINGS_STATE:
        settings()
    elif STATE == config.END_STATE:
        terminate()

menu()
