if __name__ == '__main__':
    import pygame
    from pygame.constants import *
    import sys

    pygame.init()
    screen = pygame.display.set_mode((1000, 720), 0, 32)
    pygame.display.set_caption('Wordle')
    start_img = pygame.image.load('minigameassets/wordle picture.png').convert_alpha()
    start_img = pygame.transform.scale(start_img, (50, 50))


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):



        # draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))







# create button instances
top_row = []
q = Button(200, 450, start_img)
top_row.append(q)

w = Button(260, 450, start_img)
top_row.append(w)

e = Button(320, 450, start_img)
top_row.append(e)

r = Button(380, 450, start_img)
top_row.append(r)

t = Button(440, 450, start_img)
top_row.append(t)

y = Button(500, 450, start_img)
top_row.append(y)

u = Button(560, 450, start_img)
top_row.append(u)

i = Button(620, 450, start_img)
top_row.append(i)

o = Button(680, 450, start_img)
top_row.append(o)

p = Button(740, 450, start_img)
top_row.append(p)

a = Button(240, 510, start_img)
top_row.append(a)

s = Button(300, 510, start_img)
top_row.append(s)

d = Button(360, 510, start_img)
top_row.append(d)

f = Button(420, 510, start_img)
top_row.append(f)

g = Button(480, 510, start_img)
top_row.append(g)

h = Button(540, 510, start_img)
top_row.append(h)

j = Button(600, 510, start_img)
top_row.append(j)

k = Button(660, 510, start_img)
top_row.append(k)

l = Button(720, 510, start_img)
top_row.append(l)

Enter = Button(200, 570, start_img)
top_row.append(Enter)

z = Button(260, 570, start_img)
top_row.append(z)

x = Button(320, 570, start_img)
top_row.append(x)

c = Button(380, 570, start_img)
top_row.append(c)

v = Button(440, 570, start_img)
top_row.append(v)

b = Button(500, 570, start_img)
top_row.append(b)

n = Button(560, 570, start_img)
top_row.append(n)

m = Button(620, 570, start_img)
top_row.append(m)

Backspace = Button(680, 570, start_img)
top_row.append(Backspace)


while True:
    for i in top_row:
        i.draw()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

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

    pygame.display.update()

white = '⬜'
yellow = '🟨'
green = '🟩'
game_amount = 0
while True:
    results = [None, None, None, None, None, None]
    turns = 0
    word = input("Input a five-letter word: ")
    if word == '':
        quit()
    if len(word) != 5:
        print(f'"{word} is not a five-letter word."')
    else:
        while turns < 6:
            colour = [white, white, white, white, white]
            guess = input("Guess the five-letter word: ")
            turns += 1
            if len(guess) != 5:
                print(f'"{guess} is not a five-letter word."')
                colour = '⬜⬜⬜⬜⬜'
            else:
                for x in range(0, 5):
                    if guess[x] == word[x]:
                        colour[x] = green
                    elif guess[x] in word:
                        colour[x] = yellow
                    else:
                        colour[x] = white
                colour = colour[0] + colour[1] + colour[2] + colour[3] + colour[4]
            results[turns - 1] = colour
            print(colour)
            if word == guess:
                break
        if word != guess:
            turns = 'X'
        game_amount += 1
        print(f' "Wordle {game_amount} {turns}/6".')
        for i in results:
            if i is not None:
                print(i)
