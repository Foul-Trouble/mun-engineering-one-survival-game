# This is the functions file
from loads import *


def coin_notification(coin_count, ability_status, time_interval):
    # Find the coin count and ability and take that and figure out if the sound should go or the light should turn on
    coin_count = 0
    for i in coin_count[0, 6]:
        coin_count += 1
        if coin_count == 5:
            ability_status = True
            digital_write(4, True)
        else:
            ability_status = False
            coin_notification(coin_count, ability_status, 0.5)
            digital_write(4, True)


def total_score(coins, abilities_used, enemies_defeated, boss_time, total_time):
    # Calculate the total score of the run
    initial_score = []
    coins_value = 50
    abilities_value = 400
    enemies_value = 200
    boss_value = (1000 - (boss_time/50))
    total_value = (1000 - (total_time/50))
    initial_score.append(coins*coins_value)
    initial_score.append(abilities_used*abilities_value)
    initial_score.append(enemies_defeated*enemies_value)
    initial_score.append(boss_time*boss_value)
    initial_score.append(total_time*total_value)
    return sum(inital_score)


if __name__ == '__main__':
  None














