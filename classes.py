# Classes file
import random
import pygame
from pygame.constants import *
from pygame.locals import *
from loads import newfoundland_coin, fail_img
from constants import coin_score, mini_game_called
from constants import world_size, sdx
from constants import clicked
from arduino import *

class Player:
    # Initialising the player.
    # This handles all the setup of the player including all the class variables, positions, and sizes.
    def __init__(self, x, y, character_chosen, re_hit=0):
        self.images_right = []
        self.images_left = []
        self.images_jump = []
        self.index = 0
        self.counter = 0
        # Create the animation of the player moving left and right
        img_jump = pygame.image.load(f'assets/{character_chosen}/{character_chosen} 1.jpeg')
        img_jump = pygame.transform.scale(img_jump, (world_size[0] / 1.3, world_size[1] / 2.15))
        img_jump_l = pygame.transform.flip(img_jump, True, False)
        self.images_jump.append(img_jump)
        self.images_jump.append(img_jump_l)
        for num in range(2, 6):
            img_right = pygame.image.load(f'assets/{character_chosen}/{character_chosen} {num}.jpeg')
            img_right = pygame.transform.scale(img_right, (world_size[0] / 1.3, world_size[1] / 2.15))
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
        self.hit_box.x = x + (world_size[0] / 3.08) + re_hit
        self.hit_box.y = y - (world_size[1] / 3.08)
        self.hit_box.width = world_size[0] / 6.66
        self.hit_box.height = world_size[1] / 2.4
        self.walking_direction = 0
        self.last_walking_direction = 1
        self.control_method = 'keyboard'
        self.ctl_index = 0

    # This handles the movement of the player as well as the players collisions with boundaries
    # This does not handle the collisions with objects
    def update(self, world, screen):
        # Find the position of the player
        # dx and dy are the amount of movement the player will have in this frame
        dx = 0
        dy = 0
        walk_cooldown = 9

        key = pygame.key.get_pressed()

        # Changing the input methods
        if key[pygame.K_k]:
            self.control_method = 'keyboard'
        elif key[pygame.K_a]:

            self.control_method = 'arduino'
            # else:
            #     print('Arduino not connected')
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
        elif self.control_method == 'arduino':
            dx += dial()

            if button():
                self.vel_y = -15
        # Using the Arduino to play

        # handle animation
        # every 9 ticks the image will change so that the sprite appears moving
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

        if self.hit_box.left < -world_size[0] / 20:
            dx = 0
        if self.hit_box.right > world_size[0] + world_size[0] / 20:
            dx = 0

        # update player coordinates
        # the dx and dy will be summed up from previous calculations
        self.rect.x += dx
        self.rect.y += dy
        self.hit_box.x += dx
        self.hit_box.y += dy

        if self.rect.bottom > world_size[1]:
            self.rect.bottom = world_size[1]
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
        tile_size = world_size[0] / 50

        # load images
        floor_img = pygame.image.load('assets/Floor.jpg')
        pavement_img = pygame.image.load('assets/Pavement.jpeg')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(floor_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(pavement_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(floor_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
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
        self.counter2 = 0
        # Create the animation of the player moving left and right
        for num in range(2, 4):
            img_right = pygame.image.load(f'assets/Adrian/Adrian {num}.jpeg')
            img_right = pygame.transform.scale(img_right, (world_size[0] / 1.3, world_size[1] / 2.15))
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
        self.hit_box.x = x + 315
        self.hit_box.y = y - 5
        self.hit_box.width = 100
        self.hit_box.height = 320

    def update(self, world, screen, player_hitbox, difficulty):
        global sdx
        dx = 0
        dy = 0
        walk_cooldown = 5
        jump_cooldown = 100
        self.counter += 1
        self.counter2 += 1

        # AI here
        if difficulty == 1:
            # print(self.rect.x)
            if self.hit_box.right > 1000:
                sdx *= -1
            if self.hit_box.left < 0:
                sdx *= -1

            dx = sdx
        elif difficulty == 2:
            if self.hit_box.right > 1000:
                print(self.hit_box.right)
                sdx *= -1
            if self.hit_box.left < 0:
                print(self.hit_box.left)
                sdx *= -1
            dx = sdx
            if not self.jumped:
                self.vel_y = -35
                self.jumped = True
            if self.counter2 > jump_cooldown:
                self.jumped = False
                self.counter2 = 0
        elif difficulty == 3:
            print(player_hitbox)
            adrian = self.hit_box.x + self.width/2
            player = player_hitbox.x + player_hitbox.width/2

            adrian_y = self.hit_box.y
            player_y = player_hitbox.y

            if player > adrian:
                sdx *= 5
            elif player < adrian:
                sdx = -5
            else:
                sdx = 0

            if player_y > adrian_y:
                if not self.jumped:
                    self.vel_y = -20
                    self.jumped = True
                if self.counter2 > jump_cooldown:
                    self.jumped = False
                    self.counter2 = 0





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

        self.rect.x += dx
        self.hit_box.x += dx
        if dx > 0:
            self.direction = 1
        elif dx < 0:
            self.direction = -1
        else:
            self.direction = 0
        self.rect.y += dy
        self.hit_box.y += dy

        if self.hit_box.bottom > world_size[1]:
            self.hit_box.bottom = world_size[1]

        # draw enemy onto screen
        screen.blit(self.image, self.rect)
        # pygame.draw.rect(screen, (255, 255, 255), self.hit_box, 2)

        return loss


class Coins:

    def __init__(self, coin):
        self.coins = []
        self.image = coin
        self.rect = self.image.get_rect()

    def emit(self, screen, player):
        self.check(player)
        if self.coins:
            for coin in self.coins:
                screen.blit(pygame.transform.scale(self.image, (world_size[0] / 12.5, world_size[0] / 12.5)), (coin[0]))

    def add_coins(self, x_spot, y_spot):
        coin_circle = [[x_spot, y_spot], 20]
        self.coins.append(coin_circle)

    def check(self, player):
        global coin_score, mini_game_called
        coin_copy = []
        for coin in self.coins:
            coin_img = pygame.transform.scale(newfoundland_coin, (world_size[0] / 12.5, world_size[0] / 12.5))
            coin_rect = coin_img.get_rect()
            coin_rect.x = coin[0][0]
            coin_rect.y = coin[0][1]

            if not coin_rect.colliderect(player.hit_box.x, player.hit_box.y, player.hit_box.width,
                                         player.hit_box.height):
                coin_copy.append(coin)
            else:
                coin_score += 1

        self.coins = coin_copy

    def reset(self):
        self.coins = []


class Grades:

    def __init__(self):
        self.grades = []

    def emit(self, screen, player, mini_game_called):
        mini_game_called = self.delete_grades(player, mini_game_called)
        for grade in self.grades:
            if not 0 < grade[0][0] < world_size[0] / 1.15:
                grade[1][0] = -grade[1][0]
                grade[2] += 1
            if not 0 < grade[0][1] < world_size[1] / 1.11:
                grade[1][1] = -grade[1][1]
                grade[2] += 1
            grade[0][0] += grade[1][0]
            grade[0][1] += grade[1][1]

            screen.blit(pygame.transform.scale(fail_img, (world_size[0] / 8, world_size[1] / 9.6)), (grade[0]))
        return mini_game_called

    def add_grades(self, x, y, sx, sy):
        pos_x = x
        pos_y = y
        spd_x = sx
        spd_y = sy
        bounce = 0
        grade_loc = [[pos_x, pos_y], [spd_x, spd_y], bounce]
        self.grades.append(grade_loc)

    def delete_grades(self, player, mini_game_called):
        grades_copy1 = []
        grades_copy = [grad for grad in self.grades if grad[2] < 6]
        if grades_copy:
            for grade in grades_copy:
                grade_rect = pygame.transform.scale(fail_img, (world_size[0] / 8, world_size[1] / 9.6)).get_rect()
                grade_rect.x = grade[0][0]
                grade_rect.y = grade[0][1]

                if grade_rect.colliderect(player.hit_box.x, player.hit_box.y, player.hit_box.width,
                                          player.hit_box.height):
                    mini_game_called = True
                else:
                    grades_copy1.append(grade)
        else:
            mini_game_called = False
        self.grades = grades_copy1
        return mini_game_called

    def reset(self):
        self.grades = []


class Platform:

    def __init__(self):
        self.platforms = []


class Button:
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    gray = (128, 128, 128)
    blue = (0, 0, 255)
    # colours for button and text
    button_col = (128, 128, 128)
    hover_col = (75, 225, 255)
    click_col = (50, 150, 255)
    text_col = black

    def __init__(self, x, y, text, width, height):
        self.x = x
        self.y = y
        self.text = text
        self.height = height
        self.width = width

    def draw_button(self, screen):
        white = (255, 255, 255)
        black = (0, 0, 0)
        green = (0, 255, 0)
        yellow = (255, 255, 0)
        gray = (128, 128, 128)
        blue = (0, 0, 255)

        action = False
        global clicked

        # get mouse position
        pos = pygame.mouse.get_pos()

        # create pygame Rect object for the button
        button_rect = Rect(self.x, self.y, self.width, self.height)

        # check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked is True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(screen, self.button_col, button_rect)

        # add shading to button
        pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height),
                         2)
        pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height),
                         2)

        # add text to button
        font = pygame.font.Font('assets/pricedown bl.otf', 48)
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y))
        return action
