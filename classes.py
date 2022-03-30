# Classes file
import random
import pygame
from loads import newfoundland_coin
from constants import coin_score, mini_game_called
from functions import mini_message


class Player:
    def __init__(self, x, y, character_chosen, re_hit=0):
        self.images_right = []
        self.images_left = []
        self.images_jump = []
        self.index = 0
        self.counter = 0
        # Create the animation of the player moving left and right
        img_jump = pygame.image.load(f'assets/{character_chosen}/{character_chosen} 1.jpeg')
        img_jump = pygame.transform.scale(img_jump, (768, 336))
        img_jump_l = pygame.transform.flip(img_jump, True, False)
        self.images_jump.append(img_jump)
        self.images_jump.append(img_jump_l)
        for num in range(2, 6):
            img_right = pygame.image.load(f'assets/{character_chosen}/{character_chosen} {num}.jpeg')
            img_right = pygame.transform.scale(img_right, (768, 336))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Find the hit boxes of the character
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.hit_box = self.image.get_rect()
        self.hit_box.x = x + 325 + re_hit
        self.hit_box.y = y - 234
        self.hit_box.width = 150
        self.hit_box.height = 300
        self.walking_direction = 0
        self.last_walking_direction = 1
        self.control_method = 'keyboard'
        self.ctl_index = 0

    def update(self, world, screen):
        # Find the position of the player
        dx = 0
        dy = 0
        walk_cooldown = 9

        key = pygame.key.get_pressed()

        # Changing the input methods
        if key[pygame.K_k]:
            self.control_method = 'keyboard'
        elif key[pygame.K_a]:
            self.control_method = 'arduino'
        elif key[pygame.K_c]:
            self.control_method = 'controller'
        # Using a keyboard to play
        if self.control_method == 'keyboard':
            if key[pygame.K_SPACE] and not self.jumped:
                self.vel_y = -15
                self.jumped = True
            if not key[pygame.K_SPACE]:
                self.jumped = False
            if key[pygame.K_LEFT]:
                if not key[pygame.K_RIGHT]:
                    if self.walking_direction == 1:
                        self.hit_box.x += -25
                    dx -= 5
                    self.counter += 1
                    self.direction = -1
                    if not self.walking_direction == -1:
                        self.walking_direction = -1
                        self.hit_box.x += -25
                    if not self.last_walking_direction == -1:
                        self.last_walking_direction = -1
                        self.hit_box.x += -40

            if key[pygame.K_RIGHT]:
                if not key[pygame.K_LEFT]:
                    if self.walking_direction == -1:
                        self.hit_box.x += +25
                    dx += 5
                    self.counter += 1
                    self.direction = 1
                    if not self.walking_direction == 1:
                        self.walking_direction = 1
                        self.hit_box.x += 25
                    if not self.last_walking_direction == 1:
                        self.last_walking_direction = 1
                        self.hit_box.x += 40
            if not key[pygame.K_LEFT] and not key[pygame.K_RIGHT]:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]
                if not self.walking_direction == 0:
                    if self.walking_direction == 1:
                        self.walking_direction = 0
                        self.hit_box.x += -25
                    if self.walking_direction == -1:
                        self.walking_direction = 0
                        self.hit_box.x += +25

        # Using the Arduino to play

        # handle animation
        # every 5 ticks the image will change so that the sprite appears moving
        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]

        # add gravity
        # each tick falling is 1px/sec/sec up to 20px/sec
        self.vel_y += 1
        if self.vel_y > 20:
            self.vel_y = 20
        dy += self.vel_y

        # check for collision
        for tile in world.tile_list:
            # check for collision in x direction
            if tile[1].colliderect(self.hit_box.x + dx, self.hit_box.y, self.hit_box.width, self.hit_box.height):
                dx = 0
            # check for collision in y direction
            if tile[1].colliderect(self.hit_box.x, self.hit_box.y + dy, self.hit_box.width, self.hit_box.height):
                # check if below the ground i.e. jumping
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.hit_box.top
                    self.vel_y = 0
                # check if above the ground i.e. falling
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.hit_box.bottom
                    self.vel_y = 0

        if self.hit_box.left < -50:
            dx = 0
        if self.hit_box.right > 1050:
            dx = 0

        # update player coordinates
        # the dx and dy will be summed up from previous calculations
        self.rect.x += dx
        self.rect.y += dy
        self.hit_box.x += dx
        self.hit_box.y += dy

        if self.rect.bottom > 720:
            self.rect.bottom = 720
            dy = 0

        if dy > 14:
            if self.direction == 1:
                self.image = self.images_jump[0]
            elif self.direction == -1:
                self.image = self.images_jump[1]

        # draw player onto screen
        screen.blit(self.image, self.rect)
        if key[pygame.K_h]:
            pygame.draw.rect(screen, (255, 255, 255), self.hit_box, 2)


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

    def draw(self, screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


class Enemy:

    def __init__(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        # Create the animation of the player moving left and right
        for num in range(2, 4):
            img_right = pygame.image.load(f'assets/Adrian/Adrian {num}.jpeg')
            img_right = pygame.transform.scale(img_right, (768, 336))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Find the hit boxes of the character
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0

    def update(self, world, screen):

        dx = 0
        dy = 0
        walk_cooldown = 5

        # AI here
        # Find The Nearest Player

        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]

        # add gravity
        # each tick falling is 1px/sec/sec up to 20px/sec
        self.vel_y += 1
        if self.vel_y > 20:
            self.vel_y = 20
        dy += self.vel_y

        # check for collision
        for tile in world.tile_list:
            # check for collision in x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            # check for collision in y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # check if below the ground i.e. jumping
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                # check if above the ground i.e. falling
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0

        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > 720:
            self.rect.bottom = 720

        # draw enemy onto screen
        screen.blit(self.image, self.rect)


class Coins:

    def __init__(self, coin):
        self.coins = []
        self.image = coin
        self.rect = self.image.get_rect()

    def emit(self, screen, player):
        mini_game_called = self.check(player)
        if self.coins:
            for coin in self.coins:
                screen.blit(pygame.transform.scale(self.image, (80, 80)), (coin[0]))
        return mini_game_called

    def add_coins(self, x_spot, y_spot):
        coin_circle = [[x_spot, y_spot], 20]
        self.coins.append(coin_circle)

    def check(self, player):
        global coin_score, mini_game_called
        coin_copy = []
        for coin in self.coins:
            coin_img = pygame.transform.scale(newfoundland_coin, (80, 80))
            coin_rect = coin_img.get_rect()
            coin_rect.x = coin[0][0]
            coin_rect.y = coin[0][1]

            if not coin_rect.colliderect(player.hit_box.x, player.hit_box.y, player.hit_box.width,
                                         player.hit_box.height):
                coin_copy.append(coin)
            else:
                coin_score += 1
                mini_game_called = True

        self.coins = coin_copy
        return mini_game_called


        # img = pygame.transform.scale(floor_img, (20, 20))
        # img_rect = img.get_rect()
        # img_rect.x = col_count * 20
        # img_rect.y = row_count * 20
        # tile = (img, img_rect)
        # self.tile_list.append(tile)


class Grades:

    def __init__(self):
        self.grades = []


class Platform:

    def __init__(self):
        self.platforms = []
