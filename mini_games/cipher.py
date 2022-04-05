import pygame
from pygame.constants import *
from pygame.locals import *
import sys
import string
import random
from constants import word_list
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1000, 720), 0, 32)
    pygame.display.set_caption('Cypher')


def run(size, screen):
    screen.fill(color=(0,0,0))
    pygame.display.update()
    global clicked
    game_amount = 0
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    gray = (128, 128, 128)
    blue = (0, 0, 255)

    clicked = False
    counter = 0

    screen_width = 1000
    screen_height = 720
    turn = 0
    font = pygame.font.SysFont('Times New Roman', 30)
    class Button():
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

        def draw_button(self):

            global clicked
            action = False

            # get mouse position
            pos = pygame.mouse.get_pos()

            # create pygame Rect object for the button
            button_rect = Rect(self.x, self.y, self.width, self.height)

            # check mouseover and clicked conditions
            if button_rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    clicked = True
                    pygame.draw.rect(screen, self.click_col, button_rect)
                elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
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
            text_img = font.render(self.text, True, self.text_col)
            text_len = text_img.get_width()
            screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 15))
            return action
    class Guesses():
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.text = ' '
            self.height = 50
            self.width = 50

    def checkGuess(turn, word, userGuess, window):
        renderList = ["", "", "", "", ""]
        spacing = 0
        guessColourCode = [gray, gray, gray, gray, gray]

        for x in range(0, 3):
            if word[x] == userGuess[x]:
                guessColourCode[x] = green

        list(userGuess)

        for x in range(0, 3):
            renderList[x] = font.render(userGuess[x], True, black)
            pygame.draw.rect(window, guessColourCode[x], pygame.Rect(60 + spacing, 50 + (turn * 80), 50, 50))
            window.blit(renderList[x], (70 + spacing, 50 + (turns * 80)))
            spacing += 80

        if guessColourCode == [green, green, green, green, green]:
            return True

    number_1 = Button(200, 450, '1', 50, 50)
    number_2 = Button(260, 450, '2', 50, 50)
    number_3 = Button(320, 450, '3', 50, 50)
    number_4 = Button(380, 450, '4', 50, 50)
    number_5 = Button(440, 450, '5', 50, 50)
    number_6 = Button(500, 450, '6', 50, 50)
    number_7 = Button(560, 450, '7', 50, 50)
    number_8 = Button(620, 450, '8', 50, 50)
    number_9 = Button(680, 450, '9', 50, 50)

    def keyboard_look(guess_number):
        while True:
            if number_1.draw_button():
                return 1

            if number_2.draw_button():
                return 2

            if number_3.draw_button():
                return 3

            if number_4.draw_button():
                return 4

            if number_5.draw_button():
                return 5

            if number_6.draw_button():
                return 6

            if number_7.draw_button():
                return 7

            if number_8.draw_button():
                return 7

            if number_9.draw_button():
                return 9

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    csprng = random.SystemRandom()

    def random_string():

        x = random.randint(0, len(word_list)-1)
        return word_list[x]


    original_word = random_string()

    inty = random.randint(0, 9)
    print(inty)

    # a is 97 and z is 122
    # A is 65 and Z is 90
    def shift(plaintext, key=3):
        org_nums, new_keys = [], []
        for i in plaintext: org_nums.append(ord(i))
        for i in org_nums:
            if (65 <= i <= 122) and (i not in range(91, 97)):
                if (97 <= i <= 122 and i + key < 97) or (65 <= i <= 90 and i + key < 65):
                    new_keys.append(chr(i + key + 26))
                elif (97 <= i <= 122 and i + key <= 122) or (65 <= i <= 90 and i + key <= 90):
                    new_keys.append(chr(i + key))
                else:
                    new_keys.append(chr(i + key - 26))
            else:
                new_keys.append(chr(i))
        ciphertext = "".join(new_keys)
        return ciphertext

    original_word = random_string()

    turns = 0

    while turns < 3:
        turns += 1
        s_original_word = shift(original_word, inty)
        continue_text = font.render(s_original_word, True, (255, 255, 255))
        textRect = continue_text.get_rect()
        textRect.center = (500, 120)
        screen.blit(continue_text, textRect)

        continue_text = font.render(original_word, True, (255, 255, 255))
        textRect = continue_text.get_rect()
        textRect.center = (500, 50)
        screen.blit(continue_text, textRect)

        guess = keyboard_look(turns)
        screen.fill(color=(0, 0, 0))
        question_text = font.render((shift(s_original_word, int(-guess))), True, (150, 150, 150))
        textRect = question_text.get_rect()
        textRect.center = (500, 200)
        screen.blit(question_text, textRect)
        answer = []

        pygame.display.update()
        if original_word == shift(s_original_word, int(-guess)):
            result = True
            break
    if turns == 3:
        return False, 0
    else:
        return True, 1000 - 333*(turns-1)

if __name__ == '__main__':
    run(1000, screen)
