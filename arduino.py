from engi1020.arduino.api import *
from engi1020.arduino import oled
from time import sleep



# DIAL
def dial():
    while True:
        val = analog_read(0)
        y = int(-((val/51.15) - 10))
        return y


# LIGHT
def light(con):
    #Turn on light
    if con == True:
        con = digital_write(4, True)
    else:
        con = digital_write(4, False)

# BUZZER
def buzz(nie):
    if nie == True:
        nie = buzzer_frequency(5, 550)
    else:
        nie = buzzer_stop(5)



# BUTTON
def button(): 
    if digital_read(6) == True:
        return True
    else:
        return False

def lcd(val_1, val_2, val_3):
    oled_print('ENGI Survival')
    oled_print(f'Points: {val_1}')
    oled_print(f'Time: {val_2}')
    oled_print(f'Coins: {val_3}')


# print(lcd)
# val_1 = 1
# val_2 = 2
# val_3 = 3
# oled_print('ENGI Survival')
# oled_print(f'Current points: {val_1}')
# oled_print(f'Current time: {val_2}')
# oled_print(f'Coins: {val_3}')

         

# light(False)
# buzz(False)






  

