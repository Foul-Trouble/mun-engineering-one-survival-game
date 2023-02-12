import pygame
from pygame.locals import *
import random

if __name__ == '__main__':
    pygame.init()

    screen_width = 1000
    screen_height = 720

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Math Game')


def run(size, screen):
    global random, clicked
    font = pygame.font.SysFont('Times New Roman', 55)

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
                elif pygame.mouse.get_pressed()[0] == 0 and clicked is True:
                    clicked = False
                    action = True
                else:
                    pygame.draw.rect(screen, self.hover_colour, Button_rect)
            else:
                pygame.draw.rect(screen, self.Button_colour, Button_rect)

            # add shading to the Button
            pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
            pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
            pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height),
                             2)
            pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height),
                             2)

            # add text to the Button
            text_img = font.render(self.text, True, self.text_colour)
            text_len = text_img.get_width()
            screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 5))
            return action

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
    looking_for_possible_equation = True
    while looking_for_possible_equation:
        answer_box = []
        num1 = random.randint(1, 25)
        num2 = random.randint(1, 50)
        rand_op = random.randint(0, 3)
        if rand_op == 0:
            ans = num1 + num2
            ans_str = f'{num1} + {num2}'
        elif rand_op == 1:
            ans = num1 - num2
            ans_str = f'{num1} - {num2}'
        elif rand_op == 2:
            ans = num1 * num2
            ans_str = f'{num1} * {num2}'
        elif rand_op == 3:
            ans = int(num1 / num2)
            ans_str = f'{num1} / {num2}'
        if ans > 0 and str(ans)[::-1].find('.') < 5:
            print(ans)
            break
    guess_count = 0
    while run:

        guess = []
        screen.fill(bg)

        font = pygame.font.Font('freesansbold.ttf', 32)
        prompt_text = font.render('How well do you know math?', True, (255, 255, 255))
        textRect = prompt_text.get_rect()
        textRect.center = (500, 100)
        screen.blit(prompt_text, textRect)
        q_prompt_text = font.render(ans_str, True, (255, 255, 255))
        textRect3 = q_prompt_text.get_rect()
        textRect3.center = (500, 200)
        screen.blit(q_prompt_text, textRect3)

        if number_1.draw_Button():
            answer_box.append('1')
        if number_2.draw_Button():
            answer_box.append('2')
        if number_3.draw_Button():
            answer_box.append('3')
        if number_4.draw_Button():
            answer_box.append('4')
        if number_5.draw_Button():
            answer_box.append('5')
        if number_6.draw_Button():
            answer_box.append('6')
        if number_7.draw_Button():
            answer_box.append('7')
        if number_8.draw_Button():
            answer_box.append('8')
        if number_9.draw_Button():
            answer_box.append('9')
        if number_0.draw_Button():
            answer_box.append('0')
        if symbol_period.draw_Button():
            answer_box.append('.')
        if button_enter.draw_Button():
            if str(ans) == ''.join(answer_box):
                run = False
                result = True
                score = 1000 - 333*guess_count
            else:
                guess_count += 1
                if guess_count == 3:
                    run = False
                    result = False
                    score = 0
            answer_box = []
        if button_back.draw_Button():
            answer_box.pop(-1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        answer_text = font.render("".join(answer_box), True, (255, 255, 255))
        textRect2 = answer_text.get_rect()
        textRect2.center = (500, 400)
        screen.blit(answer_text, textRect2)

        pygame.display.update()

        # ''''
        # rect1 = pygame.Rect(175, 400, 600, 50)
        #
        # colour = (0, 0, 255)
        # pygame.draw.rect(screen, colour, rect1)
        # '''

    return result, score



