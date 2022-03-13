#from loads import bubble, startup_sound, logo, arrow, sprite
#from constants import start_time, skip, left_joy, vert_move, view_demo
from pygame.locals import *

import random
import pygame
x = 0
y = 0

if view_demo:
    pygame.display.set_caption('ROV Insight')
    screen = pygame.display.set_mode((1000, 720), 0, 32)
    clock = pygame.time.Clock()


class BubblePhysics:
    def __init__(self):
        self.bubbles = []

    def emit(self):
        self.delete_bubbles()
        if self.bubbles:
            for bubb in self.bubbles:
                bubbx = random.randint(-10, 10)
                bubb[0][1] += bubb[1]
                bubb[0][0] += bubbx
                screen.blit(pygame.transform.scale(bubble, (bubb[2], bubb[2])), (bubb[0]))

    def add_bubbles(self, a, b, dir_t, x_spot, y_spot):
        pos_x = random.randint(a-30, a+30) + x_spot
        pos_y = random.randint(b-15, b+15) + y_spot
        direction = dir_t
        bubb_size = random.randint(20, 60)
        bubble_circle = [[pos_x, pos_y], direction, bubb_size]
        self.bubbles.append(bubble_circle)

    def delete_bubbles(self):
        bubble_copy = [bubb for bubb in self.bubbles if 0 < bubb[0][1] < 720]
        self.bubbles = bubble_copy


bubble_summon = BubblePhysics()


def startup_logo():
    global skip, sys, screen, clock
    startup_sound.play()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == JOYBUTTONDOWN:
                if event.button == 0:
                    skip = True

        time_since_enter = pygame.time.get_ticks() - start_time

        if time_since_enter >= 8080:
            break
        if skip:
            startup_sound.stop()
            break
        logo_approach = time_since_enter / 5
        if time_since_enter <= 4040:
            screen.blit(pygame.transform.scale(logo, (logo_approach, logo_approach / 2)), (96, 135))
        else:
            screen.blit(pygame.transform.scale(logo, (808, 404)), (96, 135))
        pygame.display.update()
        clock.tick(60)


def place_objects(x, y, vert_move):
    global left_joy, bubble_summon
    if left_joy[1] < -0.3:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(arrow, (75, 30)), 45), (100, 30))
    if left_joy[1] > 0.3:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(arrow, (75, 30)), 225), (37, 95))
    if left_joy[0] < -0.3:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(arrow, (75, 30)), 135), (36, 31))
    if left_joy[0] > 0.3:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(arrow, (75, 30)), 315), (101, 94))
    if vert_move < -0.15:
        bubble_summon.add_bubbles(350, 400, 20, x, y)
        bubble_summon.add_bubbles(350, 300, 20, x, y)
        bubble_summon.add_bubbles(675, 350, 20, x, y)
        screen.blit(pygame.transform.rotate(pygame.transform.scale(arrow, (75, 30)), 90), (90, 17))
    if vert_move > 0.15:
        bubble_summon.add_bubbles(350, 400, -20, x, y)
        bubble_summon.add_bubbles(350, 300, -20, x, y)
        bubble_summon.add_bubbles(675, 350, -20, x, y)
        screen.blit(pygame.transform.rotate(pygame.transform.scale(arrow, (75, 30)), 270), (91, 107))

    # Test w/No Controller
    # bubble_summon.add_bubbles(350, 400, 20)
    # bubble_summon.add_bubbles(350, 300, 20)
    # bubble_summon.add_bubbles(675, 350, 20)

    screen.blit(sprite, (x + 100, y - 50))
    screen.blit(pygame.transform.scale(sprite, (75, 75)), (70, 68))

#    screen.blit(pygame.transform.rotate(pygame.transform.scale(arrow, (75, 30)), 0), (113, 85))
#    screen.blit(pygame.transform.rotate(pygame.transform.scale(arrow, (75, 30)), 45), (100, 30))
#    screen.blit(pygame.transform.rotate(pygame.transform.scale(arrow, (75, 30)), 90), (90, 17))
#    screen.blit(pygame.transform.rotate(pygame.transform.scale(arrow, (75, 30)), 135), (36, 31))

#    screen.blit(pygame.transform.rotate(pygame.transform.scale(arrow, (75, 30)), 180), (23, 85))
#    screen.blit(pygame.transform.rotate(pygame.transform.scale(arrow, (75, 30)), 225), (37, 95))
#    screen.blit(pygame.transform.rotate(pygame.transform.scale(arrow, (75, 30)), 270), (91, 107))
#    screen.blit(pygame.transform.rotate(pygame.transform.scale(arrow, (75, 30)), 315), (101, 94))