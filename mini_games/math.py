if __name__ == main:
    import pygame
    from pygame.constants import *
    import sys

    pygame.init()
    pygame.display.set_caption('Physics')
    screen = pygame.display.set_mode((1000, 720), 0, 32)

'''
start_image = pygame.image.load('start_button.png').convert_alpha()
exit_image = pygame.image.load('exit_button.png').convert_alpha()
'''

#button class
class Button():
    def __init__(selfself, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.react = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False

        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

#create button instances
start_button = Button(100, 200, start_image, 0.8)
exit_button = Button(450, 200, exit_image, 0.8)

run = True
while run:

    screen.fill((200, 228, 241))

    if start_button.draw():
        print('START')
    if exit_button.draw():
        print('EXIT')
    for event in pygame.event.get()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

        elif event.type == MOUSEBUTTONUP:
            pygame.mouse.get_pressed()
        elif event.type == MOUSEBUTTONUP:
            pygame.mouse.get_pos()
        elif event.type == MOUSEBUTTONUP:
            pygame.mouse.get_rel()
        elif event.type == MOUSEBUTTONUP:
            pygame.mouse.set_pos()
        elif event.type == MOUSEBUTTONUP:
            pygame.mouse.set_visible()
        elif event.type == MOUSEBUTTONUP:
            pygame.mouse.get_visible()
        elif event.type == MOUSEBUTTONUP:
            pygame.mouse.get_focused()
        elif event.type == MOUSEBUTTONUP:
            pygame.mouse.set_cursor()
        elif event.type == MOUSEBUTTONUP:
            pygame.mouse.get_cursor()



