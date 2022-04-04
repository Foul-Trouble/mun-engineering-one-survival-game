import pygame
from pygame.locals import *

pygame.init()

screen_width = 1000
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Math Game')

font = pygame.font.SysFont('Freesanbolt.ttf', 55)

# define colours
bg = (200, 200, 200)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)


# define global variables
clicked = False


class Button:
    # colours for button and text
    Button_colour = (25, 190, 225)
    hover_colour = (75, 225, 255)
    click_colour = (50, 150, 255)
    text_colour = (255, 255, 255)

    def __init__(self, x, y, text, width, height):
        self.x = x
        self.y = y
        self.text = text
        self.width = width
        self.height = height

    def draw_Button(self):

        global clicked
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # create pygame Rect object for the Button
        Button_rect = Rect(self.x, self.y, self.width, self.height)

        # check mouseover and clicked conditions
        if Button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.click_colour, Button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_colour, Button_rect)
        else:
            pygame.draw.rect(screen, self.Button_colour, Button_rect)

        # add shading to the Button
        pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        # add text to the Button
        text_img = font.render(self.text, True, self.text_colour)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 5))
        return action




answer_box = Button(200, 400, '', 550, 50)
question = Button(250, 50, 'How well do you know math?', 550, 50)
number_1 = Button(75, 500, '1', 50, 50)
number_2 = Button(155, 500, '2', 50, 50)
number_3 = Button(235, 500, '3', 50, 50)
number_4 = Button(315, 500, '4', 50, 50)
number_5 = Button(395, 500, '5', 50, 50)
number_6 = Button(475, 500, '6', 50, 50)
number_7 = Button(555, 500, '7', 50, 50)
number_8 = Button(635, 500, '8', 50, 50)
number_9 = Button(715, 500, '9', 50, 50)
number_0 = Button(795, 500, '0', 50, 50)
button_enter = Button(175, 600, 'Enter', 110, 50)
# symbol_add = Button(315, 600, '+', 50, 50)
# symbol_sub = Button(395, 600, '-', 50, 50)
# symbol_multi = Button(475, 600, '×', 50, 50)
# symbol_divis = Button(555, 600, '÷', 50, 50)
symbol_period = Button(315, 600, '.', 50, 50)
button_back = Button(635, 600, 'Backspace', 210, 50)



run = True
while run:

    guess = []
    screen.fill(bg)

    font = pygame.font.Font('freesansbold.ttf', 32)
    prompt_text = font.render('How well do you know math?', True, (255, 255, 255))
    textRect = prompt_text.get_rect()
    textRect.center = (500, 100)
    screen.blit(prompt_text, textRect)




    if answer_box.draw_Button():
        print('Jenna')
    if number_1.draw_Button():
        print('1')
    if number_2.draw_Button():
        print('2')
    if number_3.draw_Button():
        print('3')
    if number_4.draw_Button():
        print('4')
    if number_5.draw_Button():
        print('5')
    if number_6.draw_Button():
        print('6')
    if number_7.draw_Button():
        print('7')
    if number_8.draw_Button():
        print('8')
    if number_9.draw_Button():
        print('9')
    if number_0.draw_Button():
        print('0')
    if symbol_period.draw_Button():
        print('.')
    if button_enter.draw_Button():
        print('Enter')
    if button_back.draw_Button():
        if len(guess) > 0:
            guess.pop(-1)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()



        # ''''
        # rect1 = pygame.Rect(175, 400, 600, 50)
        #
        # colour = (0, 0, 255)
        # pygame.draw.rect(screen, colour, rect1)
        # '''


import random
import operator


def random_problem():
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '×': operator.mul,
        '÷': operator.truediv,
    }

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(list(operators.keys()))
    answer = operators.get(operation)(num1, num2)
    print(f'What is {num1} {operation} {num2}')
    return answer


def ask_question():
    answer = random_problem()
    guess = float(input())
    return guess == answer


def game():
    print("How well do you know math?")
    score = 0

    for i in range(3):

        if ask_question() == True:
            score += 1
            print("Correct!")
        else:
            print("Incorrect")

    print(f'Your score is {score}/3!')


game()
