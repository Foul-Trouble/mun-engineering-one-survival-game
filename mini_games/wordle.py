if __name__ == '__main__':
    import pygame
    from pygame.constants import *
    from pygame.locals import *
    import sys

    pygame.init()
    screen = pygame.display.set_mode((1000, 720), 0, 32)
    pygame.display.set_caption('Wordle')
game_amount = 0
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
counter = 0

screen_width = 1000
screen_height = 720
turn = 0
font = pygame.font.SysFont('Times New Roman', 30)


def draw_board():
    global turn, piece_text
    global board
    for col in range(0, 5):
        for row in range(0, 6):
            if board[row][col] is None:
                pygame.draw.rect(screen, black, [col * 70 + 320, row * 65 + 40, 50, 50], 3, 2)
            elif board[row][col] == green:
                pygame.draw.rect(screen, green, [col * 70 + 320, row * 65 + 40, 50, 50], 8, 2)
            elif board[row][col] == yellow:
                pygame.draw.rect(screen, yellow, [col * 70 + 320, row * 65 + 40, 50, 50], 8, 2)
            elif board[row][col] == gray:
                pygame.draw.rect(screen, gray, [col * 70 + 320, row * 65 + 40, 50, 50], 8, 2)
            # screen.blit(piece_text, (col * 100 + 30, row * 100 + 25))


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
        pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

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

    def draw_guess_square(self, text):
        guess_square_rect = Rect(self.x, self.y, self.width, self.height)
        # add shading to button
        text_col = blue
        pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        # add text to button
        text_img = font.render(text, True, text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 15))

#
# def checkGuess(turn, word, userGuess, window):
#     renderList = ["", "", "", "", ""]
#     spacing = 0
#     guessColourCode = [gray, gray, gray, gray, gray]
#
#     for x in range(0, 5):
#         if userGuess[x] in word:
#             guessColourCode[x] = yellow
#
#         if word[x] == userGuess[x]:
#             guessColourCode[x] = green
#
#     list(userGuess)
#
#     for x in range(0, 5):
#         renderList[x] = font.render(userGuess[x], True, black)
#         pygame.draw.rect(window, guessColourCode[x], pygame.Rect(60 + spacing, 50 + (turn * 80), 50, 50))
#         window.blit(renderList[x], (70 + spacing, 50 + (turns * 80)))
#         spacing += 80
#
#     if guessColourCode == [green, green, green, green, green]:
#         return True


Q = Button(200, 450, 'Q', 50, 50)
W = Button(260, 450, 'W', 50, 50)
E = Button(320, 450, 'E', 50, 50)
R = Button(380, 450, 'R', 50, 50)
T = Button(440, 450, 'T', 50, 50)
Y = Button(500, 450, 'Y', 50, 50)
U = Button(560, 450, 'U', 50, 50)
I = Button(620, 450, 'I', 50, 50)
O = Button(680, 450, 'O', 50, 50)
P = Button(740, 450, 'P', 50, 50)
A = Button(240, 510, 'A', 50, 50)
S = Button(300, 510, 'S', 50, 50)
D = Button(360, 510, 'D', 50, 50)
F = Button(420, 510, 'F', 50, 50)
G = Button(480, 510, 'G', 50, 50)
H = Button(540, 510, 'H', 50, 50)
J = Button(600, 510, 'J', 50, 50)
K = Button(660, 510, 'K', 50, 50)
L = Button(720, 510, 'L', 50, 50)
ENTER = Button(150, 570, 'ENTER', 100, 50)
Z = Button(260, 570, 'Z', 50, 50)
X = Button(320, 570, 'x', 50, 50)
C = Button(380, 570, 'C', 50, 50)
V = Button(440, 570, 'V', 50, 50)
B = Button(500, 570, 'B', 50, 50)
N = Button(560, 570, 'N', 50, 50)
M = Button(620, 570, 'M', 50, 50)
BACKSPACE = Button(680, 570, 'BACKSPACE', 170, 50)


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
                letter = Guesses(i * 70 + 320, guess_number * 65 + 40)
                letter.draw_guess_square(guess[i])


            except:
                None
        for z, w in enumerate(answer):
            for y, n in enumerate(w):
                letter = Guesses(y * 70 + 320, z * 65 + 40)
                letter.draw_guess_square(n)


# answer = []
# for i in range(6):
#     answer.append(keyboard_look(i))
#
# pygame.quit()

# white = '⬜'
# yellow = '🟨'
# green = '🟩'
game_amount = 0
while True:
    turns = 0
    answer = []
    word = 'SKEET'
    if word == '':
        quit()
    if len(word) != 5:
        print(f'"{word} is not a five-letter word."')
    else:
        while turns < 6:
            guess = keyboard_look(turns)
            print(guess)
            answer.append(guess)

            if len(guess) != 5:
                print(f'"{guess} is not a five-letter word."')
            else:
                for x in range(0, 5):
                    if guess[x] == word[x]:
                        board[turns][x] = green
                    elif guess[x] in word:
                        board[turns][x] = yellow
                    else:
                        board[turns][x] = gray
            print(board)
            if word == guess:
                break
            turns += 1
        if word != guess:
            turns = 'X'
        game_amount += 1
        print(f' "Wordle {game_amount} {turns}/6".')
        print(answer)