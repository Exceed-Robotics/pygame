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

# Add your shape params here

# Add other global variables here

while True:
  pg.event.pump()

  # Getting mouse position as (x,y)
  mouse_position = pg.mouse.get_pos()
  print('x-axis: ' + str(mouse_position[0]))
  print('y-axis: ' + str(mouse_position[1]))

  # Getting button event as (left-btn, scroll-btn, right, btn)
  # (0,0,0) indicates nothing has been pressed
  # (1,1,1) indicates all buttons have been pressed
  # (1,0,0) indicates left button has been pressed
  buttons = pg.mouse.get_pressed()
  print('left-button: ' + str(buttons[0]))
  print('scroll-button: ' + str(buttons[1]))
  print('right-button: ' + str(buttons[2]))

  pg.display.flip() # To update the screen
  clock.tick(60) # Setting game FPS