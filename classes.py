# Classes file
import random
import pygame
from constants import screen


class Player:
    def __init__(self):
        self.coins = [None, None]
        self.aura = None
        self.avatar_choice = None


class World:
    def __init__(self, data):
        self.tile_list = []

        # load images
        floor_img = pygame.image.load('assets/Floor.jpg')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(floor_img, (20, 20))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * 20
                    img_rect.y = row_count * 20
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                # if tile == 2:
                #     img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                #     img_rect = img.get_rect()
                #     img_rect.x = col_count * tile_size
                #     img_rect.y = row_count * tile_size
                #     tile = (img, img_rect)
                #     self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        global screen
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


class Character:
    global screen

    def __init__(self):
        self.characters = []
        self.position = [[None, None], None, None]
        self.hitbox = [25, 25]

    def place_character(self):
        for avatar in self.characters:
            screen.blit(avatar)

    def move_character(self, x, y, direction, size=1):
        self.position = [[x, y], direction, size]

    def add_character(self):
        None

    def remove_character(self):
        None


class Enemy:

    def __init__(self):
        self.enemys = []

    def create_enemy(self):
        None

    def place_enemy(self):
        # Adrian
        None

    def move_enemy(self):
        None

    def add_enemy(self):
        None

    def remove_enemy(self):
        None


class Coins:

    def __init__(self):
        self.coins = []

    def emit(self):
        self.delete_coins()
        if self.coins:
            for coin in self.coins:
                rand_coin = random.randint(-10, 10)
                coin[0][1] += coin[1]
                coin[0][0] += rand_coin
                screen.blit(pygame.transform.scale(coin, (coin[2], coin[2])), (coin[0]))

    def add_bubbles(self, a, b, dir_t, x_spot, y_spot):
        pos_x = random.randint(a - 30, a + 30) + x_spot
        pos_y = random.randint(b - 15, b + 15) + y_spot
        direction = dir_t
        coin_size = random.randint(20, 60)
        coin_circle = [[pos_x, pos_y], direction, coin_size]
        self.coins.append(coin_circle)

    def delete_coins(self):
        coin_copy = [coin for coin in self.coins if 0 < coin[0][1] < 720]
        self.coins = coin_copy


class Grades:

    def __init__(self):
        self.grades = []


class Platform:

    def __init__(self):
        self.platforms = []
