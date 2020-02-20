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
white = (255,255,255)

# Add your shape params here
obj_moving_right = pg.Rect(100, 100, 50, 50)
obj_moving_left = pg.Rect(100, 100, 50, 50)
obj_moving_up = pg.Rect(100, 100, 50, 50)
obj_moving_down = pg.Rect(100, 100, 50, 50)

# Add other global variables here
right = 2
left = 2
up = 2
down = 2

while True:
  
  # Fill Screen to erase previous frame
  # Try removing it and see what happens
  screen.fill(white)
  
  # Move all the objects
  obj_moving_right[0] += right
  obj_moving_left[0] -= left
  obj_moving_up[1] -= up
  obj_moving_down[1] += down  
  
  # Render all the objects
  pg.draw.rect(screen, red, obj_moving_right)
  pg.draw.rect(screen, red, obj_moving_left)
  pg.draw.rect(screen, red, obj_moving_up)
  pg.draw.rect(screen, red, obj_moving_down)
  
  pg.display.flip() # To update the screen
  clock.tick(60) # Setting game FPS