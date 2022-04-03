import random
import time

if __name__ == '__main__':
    import pygame
    from pygame.constants import *
    from pygame.locals import *
    import sys

    pygame.init()
    world_size = (1000, 720)
    screen = pygame.display.set_mode(world_size, 0, 32)
    pygame.display.set_caption('Wordle')
else:
    import pygame
    from pygame.constants import *
    from pygame.locals import *
    import sys

    pygame.display.set_caption('Wordle')


def run(world_size, screen):
    global board, clicked
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    gray = (128, 128, 128)
    blue = (0, 0, 255)

    board = [[None, None, None, None, None],
             [None, None, None, None, None],
             [None, None, None, None, None],
             [None, None, None, None, None],
             [None, None, None, None, None],
             [None, None, None, None, None]]

    clicked = False

    screen_width = world_size[0]
    screen_height = world_size[1]
    turn = 0
    font = pygame.font.SysFont('Times New Roman', int(screen_width / 33.3))

    def draw_board():
        global turn, piece_text, board
        for col in range(0, 5):
            for row in range(0, 6):
                if board[row][col] is None:
                    pygame.draw.rect(screen, black,
                                     [(col * 70 + 320) / 1000 * world_size[0], (row * 65 + 40) / 720 * world_size[1],
                                      world_size[0] / 20, world_size[0] / 20], 3, 2)
                elif board[row][col] == green:
                    pygame.draw.rect(screen, green,
                                     [(col * 70 + 320) / 1000 * world_size[0], (row * 65 + 40) / 720 * world_size[1],
                                      world_size[0] / 20, world_size[0] / 20], 8, 2)
                elif board[row][col] == yellow:
                    pygame.draw.rect(screen, yellow,
                                     [(col * 70 + 320) / 1000 * world_size[0], (row * 65 + 40) / 720 * world_size[1],
                                      world_size[0] / 20, world_size[0] / 20], 8, 2)
                elif board[row][col] == gray:
                    pygame.draw.rect(screen, gray,
                                     [(col * 70 + 320) / 1000 * world_size[0], (row * 65 + 40) / 720 * world_size[1],
                                      world_size[0] / 20, world_size[0] / 20], 8, 2)

    class Button:
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
            text_img = font.render(self.text, True, self.text_col)
            text_len = text_img.get_width()
            screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y))
            return action

    class Guesses():
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.text = ' '
            self.height = world_size[0] / 20
            self.width = world_size[0] / 20

        def draw_guess_square(self, text):
            guess_square_rect = Rect(self.x, self.y, self.width, self.height)
            # add shading to button
            text_col = blue
            pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
            pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
            pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height),
                             2)
            pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height),
                             2)

            # add text to button
            text_img = font.render(text, True, text_col)
            text_len = text_img.get_width()
            screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 15))

    Q = Button(200 / 1000 * world_size[0], 450 / 720 * world_size[1], 'Q', world_size[0] / 20, world_size[0] / 20)
    W = Button(260 / 1000 * world_size[0], 450 / 720 * world_size[1], 'W', world_size[0] / 20, world_size[0] / 20)
    E = Button(320 / 1000 * world_size[0], 450 / 720 * world_size[1], 'E', world_size[0] / 20, world_size[0] / 20)
    R = Button(380 / 1000 * world_size[0], 450 / 720 * world_size[1], 'R', world_size[0] / 20, world_size[0] / 20)
    T = Button(440 / 1000 * world_size[0], 450 / 720 * world_size[1], 'T', world_size[0] / 20, world_size[0] / 20)
    Y = Button(500 / 1000 * world_size[0], 450 / 720 * world_size[1], 'Y', world_size[0] / 20, world_size[0] / 20)
    U = Button(560 / 1000 * world_size[0], 450 / 720 * world_size[1], 'U', world_size[0] / 20, world_size[0] / 20)
    I = Button(620 / 1000 * world_size[0], 450 / 720 * world_size[1], 'I', world_size[0] / 20, world_size[0] / 20)
    O = Button(680 / 1000 * world_size[0], 450 / 720 * world_size[1], 'O', world_size[0] / 20, world_size[0] / 20)
    P = Button(740 / 1000 * world_size[0], 450 / 720 * world_size[1], 'P', world_size[0] / 20, world_size[0] / 20)
    A = Button(240 / 1000 * world_size[0], 510 / 720 * world_size[1], 'A', world_size[0] / 20, world_size[0] / 20)
    S = Button(300 / 1000 * world_size[0], 510 / 720 * world_size[1], 'S', world_size[0] / 20, world_size[0] / 20)
    D = Button(360 / 1000 * world_size[0], 510 / 720 * world_size[1], 'D', world_size[0] / 20, world_size[0] / 20)
    F = Button(420 / 1000 * world_size[0], 510 / 720 * world_size[1], 'F', world_size[0] / 20, world_size[0] / 20)
    G = Button(480 / 1000 * world_size[0], 510 / 720 * world_size[1], 'G', world_size[0] / 20, world_size[0] / 20)
    H = Button(540 / 1000 * world_size[0], 510 / 720 * world_size[1], 'H', world_size[0] / 20, world_size[0] / 20)
    J = Button(600 / 1000 * world_size[0], 510 / 720 * world_size[1], 'J', world_size[0] / 20, world_size[0] / 20)
    K = Button(660 / 1000 * world_size[0], 510 / 720 * world_size[1], 'K', world_size[0] / 20, world_size[0] / 20)
    L = Button(720 / 1000 * world_size[0], 510 / 720 * world_size[1], 'L', world_size[0] / 20, world_size[0] / 20)
    ENTER = Button(150 / 1000 * world_size[0], 570 / 720 * world_size[1], 'ENTER', world_size[0] / 10,
                   world_size[0] / 20)
    Z = Button(260 / 1000 * world_size[0], 570 / 720 * world_size[1], 'Z', world_size[0] / 20, world_size[0] / 20)
    X = Button(320 / 1000 * world_size[0], 570 / 720 * world_size[1], 'X', world_size[0] / 20, world_size[0] / 20)
    C = Button(380 / 1000 * world_size[0], 570 / 720 * world_size[1], 'C', world_size[0] / 20, world_size[0] / 20)
    V = Button(440 / 1000 * world_size[0], 570 / 720 * world_size[1], 'V', world_size[0] / 20, world_size[0] / 20)
    B = Button(500 / 1000 * world_size[0], 570 / 720 * world_size[1], 'B', world_size[0] / 20, world_size[0] / 20)
    N = Button(560 / 1000 * world_size[0], 570 / 720 * world_size[1], 'N', world_size[0] / 20, world_size[0] / 20)
    M = Button(620 / 1000 * world_size[0], 570 / 720 * world_size[1], 'M', world_size[0] / 20, world_size[0] / 20)
    BACKSPACE = Button(680 / 1000 * world_size[0], 570 / 720 * world_size[1], 'BACKSPACE', 170 / 1000 * world_size[0],
                       world_size[0] / 20)

    def keyboard_look(guess_number):
        guess = []
        while True:

            draw_board()
            if Q.draw_button():
                guess.append('Q')

            if W.draw_button():
                guess.append('W')

            if E.draw_button():
                guess.append('E')

            if R.draw_button():
                guess.append('R')

            if T.draw_button():
                guess.append('T')

            if Y.draw_button():
                guess.append('Y')

            if U.draw_button():
                guess.append('U')

            if I.draw_button():
                guess.append('I')

            if O.draw_button():
                guess.append('O')

            if P.draw_button():
                guess.append('P')

            if A.draw_button():
                guess.append('A')

            if S.draw_button():
                guess.append('S')

            if D.draw_button():
                guess.append('D')

            if F.draw_button():
                guess.append('F')

            if G.draw_button():
                guess.append('G')

            if H.draw_button():
                guess.append('H')

            if J.draw_button():
                guess.append('J')

            if K.draw_button():
                guess.append('K')

            if L.draw_button():
                guess.append('L')

            if ENTER.draw_button():
                if len(guess) == 5:
                    return guess

            if Z.draw_button():
                guess.append('Z')

            if X.draw_button():
                guess.append('X')

            if C.draw_button():
                guess.append('C')

            if V.draw_button():
                guess.append('V')

            if B.draw_button():
                guess.append('B')

            if N.draw_button():
                guess.append('N')

            if M.draw_button():
                guess.append('M')

            if BACKSPACE.draw_button():
                if len(guess) > 0:
                    guess.pop(-1)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                screen.fill(color=(255, 255, 255))
            if len(guess) > 5:
                guess.pop(-1)

            for i in range(5):
                try:
                    letter = Guesses((i * 70 + 320) / 1000 * world_size[0],
                                     (guess_number * 65 + 40) / 720 * world_size[1])
                    letter.draw_guess_square(guess[i])

                except:
                    None
            for z, w in enumerate(answer):
                for y, n in enumerate(w):
                    letter = Guesses((y * 70 + 320) / 1000 * world_size[0], (z * 65 + 40) / 720 * world_size[1])
                    letter.draw_guess_square(n)

    turns = 0
    answer = []
    word_list = ['SKEET', 'SLEEP', 'BUILD', 'MATHS', 'CRAZY', 'EARTH', 'DIRTY', 'CIVIL', 'POWER', 'CABLE']
    word_num = random.randint(0, len(word_list)-1)
    word = list(word_list[word_num])
    guess = None

    while turns < 6:
        guess = keyboard_look(turns)
        answer.append(guess)
        letter_check = word[:]

        for x in range(5):
            if guess[x] == word[x]:
                board[turns][x] = green
                letter_check.remove(guess[x])
        for x in range(5):
            if board[turns][x] is None:
                if (guess[x] in word) and (guess[x] in letter_check):
                    board[turns][x] = yellow
                    letter_check.remove(guess[x])
                else:
                    board[turns][x] = gray

        if word == guess:
            break
        turns += 1

    if word == guess:
        t_n = pygame.time.get_ticks()
        while t_n > pygame.time.get_ticks() - 2000:
            draw_board()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        return True, turns
    else:
        return False, turns


if __name__ == '__main__':
    print(run(world_size, screen))
