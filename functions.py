# This is the functions file
from engi1020.arduino.api import *
from constants import screen


def coin_notification(coin_count, ability_status):
    None
    # Find the coin count and ability and take that and figure out if the sound should go or the light should turn on


def total_score(coins, abilities_used, enemys_defeated, boss_time, total_time):
    None
    # Calculate the total score of the run





def arduino_dial_read(dial, function):
    if function == 0:
        return (analog_read(dial) / 511) - 1
    elif function == 1:
        return analog_read(dial)
    else:
        return 0
