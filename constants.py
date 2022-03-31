# This is the constants file
apple = 4
banana = 8
game = True
start_time = 0
arduino = False
arduino_test = True
start_game = False

world_init = 0
coin_score = 0
mini_game_called = False
mini_game_time = 0

from win32api import GetSystemMetrics
window = GetSystemMetrics(1) / 1.33
window = 900
world_size = (window * 1000 / 720, window)
