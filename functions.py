# This is the functions file
from loads import *


def coin_notification(coin_count, ability_status, time_interval):
    None
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






def total_score(coins, abilities_used, enemys_defeated, boss_time, total_time):
    None
    # Calculate the total score of the run
    inital_score = []
    total_coins = coins
    total_abilities = abilities_used
    total_enemys = enemys_defeated
    total_boss = boss_time
    final_time = total_time
    coins_value = 50
    abilities_value = 100
    enemys_value = 200
    boss_value = 400
    total_value = 600
    inital_score.append(coins*coins_value)
    inital_score.append(abilities_used)
    inital_score.append(enemys_defeated)
    inital_score.append(boss_time)
    inital_score.append(total_time)
    sum(inital_score)
















