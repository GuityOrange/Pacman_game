''' 

参数设置 

'''

import os
import pygame

IS_FAILED = [False]
IS_CLEARANCE = [False]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
SKYBLUE = (0, 191, 255)
FONT_PATH = os.path.join(os.getcwd(), 'resources/font/ALGER.TTF')
HERO_PATH = os.path.join(os.getcwd(),'resources/images/pacman.png')
ICON_PATH = os.path.join(os.getcwd(),'resources/images/pacman.png')
ENEMY1_PATH = os.path.join(os.getcwd(),'resources/images/enemy1.png')
ENEMY2_PATH = os.path.join(os.getcwd(),'resources/images/enemy2.png')
ENEMY3_PATH = os.path.join(os.getcwd(),'resources/images/enemy3.png')
ENEMY4_PATH = os.path.join(os.getcwd(),'resources/images/enemy4.png')
ENEMY_TURNED_PATH = os.path.join(os.getcwd(),'resources/images/enemy_turned.png')
BGM_PATH = os.path.join(os.getcwd(),'resources/sounds/bg.mp3')
wall_positions = [        [0, 0, 6, 600],
				          [0, 0, 600, 6],
						  [0, 600, 606, 6],
						  [600, 0, 6, 606],
						  [300, 0, 6, 66],
						  [60, 60, 186, 6],
						  [360, 60, 186, 6],
						  [60, 120, 66, 6],
						  [60, 120, 6, 126],
						  [180, 120, 246, 6],
						  [300, 120, 6, 66],
						  [480, 120, 66, 6],
						  [540, 120, 6, 126],
						  [120, 180, 126, 6],
						  [120, 180, 6, 126],
						  [360, 180, 126, 6],
						  [480, 180, 6, 126],
						  [180, 240, 6, 126],
						  [180, 360, 246, 6],
						  [420, 240, 6, 126],
						  [240, 240, 42, 6],
						  [324, 240, 42, 6],
						  [240, 240, 6, 66],
						  [240, 300, 126, 6],
						  [360, 240, 6, 66],
						  [0, 300, 66, 6],
						  [540, 300, 66, 6],
						  [60, 360, 66, 6],
						  [60, 360, 6, 186],
						  [480, 360, 66, 6],
						  [540, 360, 6, 186],
						  [120, 420, 366, 6],
						  [120, 420, 6, 66],
						  [480, 420, 6, 66],
						  [180, 480, 246, 6],
						  [300, 480, 6, 66],
						  [120, 540, 126, 6],
						  [360, 540, 126, 6]           ]
big_bean_positions = [    [4,2],
						  [12,2],
						  [4,16],
						  [12,16]   ]
enemy_images_paths = [ENEMY1_PATH,ENEMY2_PATH,ENEMY3_PATH,ENEMY4_PATH]
move_track_test = {(8,9):[0,-1],
				   (6,9):[1,0],
				   (6,12):[0,1],
				   (10,12):[-1,0],
				   (10,6):[0,-1],
				   (6,6):[1,0]} 
available_point = [ ]