'''
Exceed Robotics (2010+)
All Rights Reserved.
NOTICE:  All information contained herein is, and remains
the property of Exceed Robotics. The intellectual and technical
concepts contained herein are proprietary to Exceed Robotics, and
are protected by trade secret or copyright law. Dissemination of
this information or reproduction of this material is strictly
forbidden unless prior written permission is obtained from
Exceed Robotics.
'''

# Generic import statements
import pygame as pg
from sys import path
from sys import exit
import os

# Global Variables
game_name = "Game Name"
window_size = (800,600)
FPS = 60

# Initial Setup
pg.init()
screen = pg.display.set_mode(window_size) # Setting game window size to (x,y)
pg.display.set_caption("Game Name")
clock = pg.time.Clock()

# Add your colors here
red = (255, 0, 0)

# Add your shape params here
obj = (10, 10, 50, 50)

point_1 = (10, 10)
point_2 = (20, 20)
thickness = 5

# Add other global variables here

while True:

  # For Rect
  pg.draw.rect(screen, red, obj)
  
  # For Ellipse
  pg.draw.ellipse(screen,red,obj)
  
  # For Line
  pg.draw.line(screen, red, point_1, point_2, thickness)

  pg.display.flip() # To update the screen
  clock.tick(60) # Setting game FPS