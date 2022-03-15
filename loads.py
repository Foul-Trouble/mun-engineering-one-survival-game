# This is the loads file
import math
import pygame
from pygame.constants import *
from pygame import mixer
from engi1020.arduino.api import *
import numpy
import os
import sys
import random

import functions
from constants import *
from classes import *
from main_game_mechanics import *

from assets import *
pygame.init()
mun_logo = pygame.image.load('assets/MUN Logo.png')
mixer.music.load('assets/Wii Sports Resort (Remix).wav')
startup_sound = mixer.Sound('assets/NINTENDO Mii THEME (TRAP REMIX) - VANDER.wav')
