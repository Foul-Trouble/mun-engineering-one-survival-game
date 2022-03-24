import math
import pygame
from pygame.constants import *
from pygame import mixer
from engi1020.arduino.api import *
import numpy
import os
import sys
import random

from functions import *
from constants import *
from classes import *
from main_game_mechanics import *
from loads import *

from assets import *

# Testing Stuff
if __name__ == "__main__":
    None


# Main Loop !!!DO NOT TOUCH, RUSSELL ONLY!!!
def init():
    global arduino, clock, screen, start_game, start_time, player, world
    pygame.display.set_caption('ENGI Survival')
    screen = pygame.display.set_mode((1000, 720), 0, 32)
    clock = pygame.time.Clock()
    player = Player(100, 720-130)
    world = World(level_one)
    while not start_game:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                start_time = pygame.time.get_ticks()
                start_game = True
        font = pygame.font.SysFont("fontname", 20)
        text = font.render('GeeksForGeeks', True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000 // 2, 720 // 2)
        screen.blit(text, textRect)

    if not arduino_test:
        try:
            digital_read(6)
            arduino = True
        except Exception:
            print("Arduino not detected")
            arduino = False
    student = Character()
    teacher = Enemy()
    coin_summon = Coins()
    grade_summon = Grades()
    mixer.music.play(-1)
    while True:
        time_since_enter = pygame.time.get_ticks() - start_time
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if time_since_enter >= 3900:
            screen.fill(color=(0, 0, 0))
            break
        if arduino:
            if digital_read(6):
                break
        logo_approach = time_since_enter / 5
        screen.fill(color=(0, 0, 0))
        if time_since_enter <= 4040:
            screen.blit(pygame.transform.scale(mun_logo, (logo_approach, logo_approach / 2)), (96, 135))
        else:
            screen.blit(pygame.transform.scale(mun_logo, (808, 404)), (96, 135))
        pygame.display.update()
        clock.tick(60)


def main_game():
    # Load Screen - 0 to 11300
    # Outside - 11300 to 18850
    # 3 - 18850 to 33850
    # 4 - 33850 to 48850
    # 5 - 48850 to ?
    global screen
    time_since_enter = pygame.time.get_ticks() - start_time
    screen.blit(pygame.transform.scale(current_background, (1000, 720)), (0, 0))
    if time_since_enter < 11300:
        # Outside Engineering Building Level
        world = World(level_one)
        world.draw(screen)
        # screen.blit(pygame.transform.scale(adrian1, (168, 384)), (50, 366))
    elif time_since_enter < 18850:
        screen.fill(color=(255, 0, 0))
    elif time_since_enter < 33850:
        screen.fill(color=(0, 255, 0))
    elif time_since_enter < 48850:
        screen.fill(color=(255, 0, 0))
    else:
        screen.fill(color=(0, 0, 0))


def close():
    exit()


def loop():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    main_game()
    player.update(world, screen)
    pygame.display.update()
    clock.tick(60)


init()
while game:
    loop()

# Exit Stuff
close()
exit()
