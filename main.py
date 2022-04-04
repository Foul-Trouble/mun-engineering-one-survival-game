import math
import pygame
from pygame.constants import *
from pygame import mixer
from engi1020.arduino.api import *
import numpy
import os
import sys
import random
import time

from functions import *
from constants import *
from classes import *
from loads import *
from levels import *
from mini_games import wordle

import mini_games

from assets import *

# Testing Stuff
if __name__ == "__main__":
    None


def init():
    global arduino, clock, screen, start_game, start_time, player, teacher, world, character_chosen, coin_count, grade_count
    pygame.display.set_caption('ENGI Survival')
    screen = pygame.display.set_mode(world_size, 0, 32)
    clock = pygame.time.Clock()
    character_chosen = '_____'
    character_hit_loc = 0
    while not start_game:
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if key[pygame.K_r]:
                character_chosen = 'Russell'
                character_hit_loc = -(world_size[0] / 50)
            elif key[pygame.K_m]:
                character_chosen = 'McKenna'
                character_hit_loc = 0
            elif key[pygame.K_z]:
                character_chosen = 'Zach'
                character_hit_loc = -(world_size[0] / 10)
            elif key[pygame.K_j]:
                character_chosen = 'Jenna'
            elif key[pygame.K_a]:
                character_chosen = 'Adrian'

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                if not character_chosen == '_____':
                    start_time = pygame.time.get_ticks()
                    start_game = True
        screen.fill(color=(0, 0, 0))
        font = pygame.font.Font('freesansbold.ttf', int(world_size[0] / 30))
        continue_text = font.render('Click Anywhere to Continue', True, (255, 255, 255))
        question_text = font.render('Please click the initial of the player you would like', True, (255, 255, 255))
        chosen_text = font.render(f'You have chosen {character_chosen}', True, (255, 255, 255))
        textRect = continue_text.get_rect()
        textRect.center = (world_size[0] / 2, world_size[1] / 1.3)
        screen.blit(continue_text, textRect)
        textRect = chosen_text.get_rect()
        textRect.center = (world_size[0] / 2, world_size[1] / 2)
        screen.blit(chosen_text, textRect)
        textRect = question_text.get_rect()
        textRect.center = (world_size[0] / 2, world_size[1] / 4)
        screen.blit(question_text, textRect)

        pygame.display.update()
    player = Player(-world_size[0] / 3.3, world_size[1] / 1.22, character_chosen, character_hit_loc)
    world = World(blank_level)
    coin_count = Coins(newfoundland_coin)
    grade_count = Grades()
    if not arduino_test:
        try:
            digital_read(6)
            arduino = True
        except Exception:
            print("Arduino not detected")
            arduino = False
    teacher = Enemy(400, 590)
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
            screen.blit(pygame.transform.scale(mun_logo, (logo_approach, logo_approach / 2)),
                        (world_size[0] / 10.41, world_size[1] / 5.33))
        else:
            screen.blit(pygame.transform.scale(mun_logo, (world_size[0] / 1.24, world_size[1] / 1.78)),
                        (world_size[0] / 10.41, world_size[1] / 5.33))
        pygame.display.update()
        clock.tick(60)


def mini_game_check():
    global mini_game_called, mini_game_time
    if mini_game_called:
        mini_game_start = pygame.time.get_ticks()
        mixer.music.pause()
        startup_sound.play()
        mini_game_choice = random.randint(1, 5)
        flash = 2
        while flash > 0:
            screen.fill('black')
            pygame.display.update()
            time.sleep(0.1)
            screen.fill('white')
            pygame.display.update()
            time.sleep(0.1)
            flash -= 1

        result, score = wordle.run(world_size, screen)
        # if mini_game_choice == 1:
        #     mini_games.cipher.run()
        # elif mini_game_choice == 2:
        #     mini_games.math.run()
        # elif mini_game_choice == 3:
        #     mini_games.physics.run()
        # elif mini_game_choice == 4:
        #     mini_games.wordle.run(world_size)
        # elif mini_game_choice == 5:
        #     mini_games.work_term.run()
        # else:
        #     None
        startup_sound.stop()
        mixer.music.unpause()
        mini_game_called = False
        mini_game_time += (pygame.time.get_ticks() - mini_game_start)
        return result, score
    return True, 0


def main_game():
    global world, world_init, mini_game_called, mini_game_time, current_background, levels
    time_since_enter = pygame.time.get_ticks() - start_time - mini_game_time
    screen.blit(pygame.transform.scale(current_background, world_size), (0, 0))

    if time_since_enter < 11300:
        if world_init == 0:
            world_init = 1
            world = World(level_one)
            current_background = outside_engineering

            for coin in level_one_coins:
                coin_count.add_coins(coin[0], coin[1])
            for grade in level_one_grades:
                grade_count.add_grades(grade[0], grade[1], grade[2], grade[3])

    elif time_since_enter < 18850:
        if world_init == 1:
            world_init = 2
            world = World(level_two)
            current_background = bruneau

            coin_count.reset()
            grade_count.reset()
            for coin in level_two_coins:
                coin_count.add_coins(coin[0], coin[1])
            for grade in level_two_grades:
                grade_count.add_grades(grade[0], grade[1], grade[2], grade[3])

    elif time_since_enter < 33850:
        if world_init == 2:
            world_init = 3
            world = World(level_three)
            current_background = chem_lab

            coin_count.reset()
            grade_count.reset()

            for coin in level_three_coins:
                coin_count.add_coins(coin[0], coin[1])
            for grade in level_three_grades:
                grade_count.add_grades(grade[0], grade[1], grade[2], grade[3])

    elif time_since_enter < 48850:
        if world_init == 3:
            world_init = 4
            world = World(level_four)
            current_background = old_sci_hall

            coin_count.reset()
            grade_count.reset()

            for coin in level_four_coins:
                coin_count.add_coins(coin[0], coin[1])
            for grade in level_four_grades:
                grade_count.add_grades(grade[0], grade[1], grade[2], grade[3])

    elif time_since_enter < 60000:
        if world_init == 4:
            print('level five')
            world_init = 5
            world = World(level_five)
            current_background = outside_university_center

            coin_count.reset()
            grade_count.reset()

            for coin in level_five_coins:
                coin_count.add_coins(coin[0], coin[1])
            for grade in level_five_grades:
                grade_count.add_grades(grade[0], grade[1], grade[2], grade[3])

    elif time_since_enter < 71200:
        if world_init == 5:
            print('level six')
            world_init = 6
            world = World(level_six)
            current_background = outside_engineering

            coin_count.reset()
            grade_count.reset()

            for coin in level_six_coins:
                coin_count.add_coins(coin[0], coin[1])
            for grade in level_six_grades:
                grade_count.add_grades(grade[0], grade[1], grade[2], grade[3])
    elif time_since_enter < 86200:
        if world_init == 6:
            world_init = 7
            world = World(level_seven)
            current_background = outside_university_center

            coin_count.reset()
            grade_count.reset()

            for coin in level_seven_coins:
                coin_count.add_coins(coin[0], coin[1])
            for grade in level_seven_grades:
                grade_count.add_grades(grade[0], grade[1], grade[2], grade[3])

    elif time_since_enter < 101400:
        if world_init == 7:
            print('level eight')
            world_init = 8
            world = World(level_eight)
            current_background = outside_engineering

            coin_count.reset()
            grade_count.reset()

            for coin in level_eight_coins:
                coin_count.add_coins(coin[0], coin[1])
            for grade in level_eight_grades:
                grade_count.add_grades(grade[0], grade[1], grade[2], grade[3])


    else:
        screen.fill(color=(0, 0, 0))

    world.draw(screen)
    coin_count.emit(screen, player)
    mini_game_called = grade_count.emit(screen, player, mini_game_called)


def boss_battle():
    global start_time
    boss_battle_time = pygame.time.get_ticks() - start_time
    screen.blit(pygame.transform.scale(eo_center, world_size), (0, 0))


def loop():
    global mini_points
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    main_game()
    player.update(world, screen)
    result, score = mini_game_check()
    if not result:
        sys.exit()
    mini_points += score
    pygame.display.update()
    clock.tick(60)


init()
while game:
    loop()

# Exit Stuff
exit()
