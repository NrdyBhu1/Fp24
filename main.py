import pygame, sys, math
import config
from pygame.locals import *
from scripts.button import Button, RadioButton
from scripts.font import Font
from scripts.text import Text
from scripts.player import Player
from scripts.coin import Coin
from scripts.bar import Bar
from scripts.settings import SettingsHandler

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
    settings_handler = SettingsHandler("settings.json")
    settings_data = settings_handler.load_data()
    settings_title = Text("Settings", font, (360, 25))
    play_music = RadioButton(100, 200, 50, "Play Music", font)
    play_sounds = RadioButton(100, 310, 50, "Play Sounds", font)
    music_vol = Bar((100, 430), settings_data['music_vol'], 4)
    sound_vol = Bar((100, 575), settings_data['sounds_vol'], 4)
    back = Button(0, 0, 100, 100, "<", font, enter_menu)
    play_music.selected = settings_data['play_music']
    play_sounds.selected = settings_data['play_sounds']
    while STATE == config.SETTINGS_STATE:
        play_music.hovered()
        play_sounds.hovered()
        music_vol.hovered()
        sound_vol.hovered()
        back.hovered()
        for event in pygame.event.get():
            if event.type == QUIT:
                exit_game()
                break
            if event.type == MOUSEBUTTONDOWN:
                back.clicked(event)
                play_music.clicked(event)
                play_sounds.clicked(event)

            music_vol.dragged(event)
            sound_vol.dragged(event)

        win.fill((0, 0, 0))
        settings_title.render(win, 200)
        play_music.render(win)
        play_sounds.render(win)
        music_vol.render(win)
        sound_vol.render(win)
        back.render(win)
        pygame.display.update()
        clock.tick(config.FPS)

    settings_data['play_music'] = play_music.selected
    settings_data['play_sounds'] = play_sounds.selected
    settings_data['music_vol'] = music_vol.value
    settings_data['sounds_vol'] = sound_vol.value
    settings_handler.save_data(settings_data)

    if STATE == config.MENU_STATE:
        menu()
    elif STATE == config.GAME_STATE:
        game()
    elif STATE == config.SETTINGS_STATE:
        settings()
    elif STATE == config.END_STATE:
        terminate()

if __name__ == '__main__':
    menu()
