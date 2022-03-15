from loads import *

# Testing Stuff
if __name__ == "__main__":
    None


# Main Loop !!!DO NOT TOUCH, RUSSELL ONLY!!!
def init():
    global arduino, clock
    pygame.display.set_caption('ENGI Survival')
    screen = pygame.display.set_mode((1000, 720), 0, 32)
    clock = pygame.time.Clock()
    try:
        digital_read(6)
        arduino = True
    except Exception:
        print("Arduino not detected")
        arduino = False
    student = Character()
    teacher = Enemy()
    coin_summon = Coins()
    grade_summon = Grades()
    time_since_enter = pygame.time.get_ticks() - start_time
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if time_since_enter >= 8080:
            break
        if arduino:
            if digital_read(6):
                break
        logo_approach = time_since_enter / 5
        if time_since_enter <= 4040:
            screen.blit(pygame.transform.scale(logo, (logo_approach, logo_approach / 2)), (96, 135))
        else:
            screen.blit(pygame.transform.scale(logo, (808, 404)), (96, 135))


def close():
    exit()


def loop():
    main_game()
    pygame.display.update()
    clock.tick(60)


init()
while game:
    loop()

# Exit Stuff
close()
exit()