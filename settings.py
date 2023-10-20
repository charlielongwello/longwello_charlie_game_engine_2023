# this file was created by charlie longwello

# game settings 
WIDTH = 360
HEIGHT = 480
FPS = 30
SCORE = 0

# player settings
PLAYER_JUMP = 30
# change players gravity from 1.5 - 2.5
PLAYER_GRAV = 2.5

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (85, 75, 169)
# added two new colors for the game
PURPLE = (215, 172, 240)
TEAL = (151, 247, 241)

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, " "),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, " "),
                 (350, 200, 100, 20, " "),
                 (175, 100, 50, 20, " "),
                 (250, 75, 100, 20, " "),
                 (200, 100, 50, 20, " "),
                 ]