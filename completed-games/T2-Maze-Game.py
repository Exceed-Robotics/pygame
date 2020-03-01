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
from typing import Tuple
import os

# Global Variables
game_name = "The Maze Game"
window_size = (800,600)
FPS = 60

# Initial Setup
pg.init()
screen = pg.display.set_mode(window_size) # Setting game window size to (x,y)
pg.display.set_caption(game_name)
clock = pg.time.Clock()

# Add other global variables here
speed = 2
player_start_x_position = 100
player_start_y_position = 100
font = pg.font.Font('freesansbold.ttf', 32)
score = 0
tressure_score = 0

# Add your colors here
red = (255, 0, 0)
white = (255,255,255)
green = (0,255,0)
blue = (0,0,255)
gold = (255,223,0)

# Add your shape params here
player = pg.Rect(player_start_x_position, player_start_y_position, 50, 50)

maze = [
    pg.Rect(100, 200, 100, 50),
    pg.Rect(100, 300, 50, 50)
]

tressures = [
    pg.Rect(120, 160, 10, 10),
    pg.Rect(120, 360, 10, 10)
]

game_completion_tile = pg.Rect(400, 400, 20, 20)

# Initialize Score Board 
text = font.render('', True, green, white)
textRect = text.get_rect() 
textRect.center = (100, 60)

# Methods Begin
def player_movement(keyboard_state: Tuple[int]) -> None:
    '''
    @keyboard_state: Takes input of the current keyboard snapshot
    Sets the x, y coordinates of the player appropriate to the keyboard input 
    '''
    if keyboard_state[pg.K_UP] == 1:
        player[1] -= speed
    if keyboard_state[pg.K_DOWN] == 1:
        player[1] += speed
    if keyboard_state[pg.K_RIGHT] == 1:
        player[0] += speed
    if keyboard_state[pg.K_LEFT] == 1:
        player[0] -= speed  

def render_all_objects() -> None:
    '''
    Renders the player, game_completion_tile, maze, score_board and tressures
    '''
    # Rendering Player
    pg.draw.rect(screen, red, player)
    
    # Render tile that detects game completion
    pg.draw.rect(screen, red, game_completion_tile)
    
    # Rendering Maze
    render_maze()
    
    # Render Tressure
    render_tressure()
        
    # Render Scoreboard
    render_score_board()
    
def render_maze() -> None:
    ''' 
    Walk through each maze element and draw it
    '''
    for wall in maze:
        pg.draw.rect(screen, green, wall)

def render_score_board() -> None:
  '''
  Render the game completion and the tressure count score
  '''
  text = font.render('Score : ' + str(score) + '   T-Score : ' + str(tressure_score), True, green, white)
  screen.blit(text, textRect)

def render_tressure():
    '''
    Walk through each tressure element and draw it
    '''
    for tressure in tressures:
        pg.draw.rect(screen, gold, tressure)


# Detectors

def detect_collisions() -> None:
    '''
    A compilation of all 3 detectors currently used
    '''
    tressure_collision_detector()
    wall_collision_detector()
    game_completion_detector()

def tressure_collision_detector() -> None:
    '''
    Walk through each tressure element 
    and on collide with a tressure
    we delete it from the tressure array 
    and add 1 to tressure_score 
    '''
    global tressure_score # To assign a global variable 
    
    # Tip: Enumerate lets me walk through each tressure element and give me the index of that tressure element
    for index, tressure in enumerate(tressures):
        if player.colliderect(tressure):
            del tressures[index] # Tip: `del` lets me delete a list element at a specified index
            tressure_score += 1

def wall_collision_detector() -> None:
    '''
    Walk through each wall element 
    and on collide with a wall reset
    the player position
    '''
    for wall in maze:
        if player.colliderect(wall):
            restart_state()

def game_completion_detector() -> None:
    '''
    On colliding with the `game_completion_tile`
    execute game_completion_state
    '''
    if player.colliderect(game_completion_tile):
        game_completion_state()

# States
def restart_state() -> None:
    '''
    Set the x and y coordinate 
    of player to initial location
    '''
    player[0] = player_start_x_position
    player[1] = player_start_y_position

def game_completion_state() -> None:
    '''
    Increment the score and restart_state()
    '''
    global score
    print('Woohoo! Game Won !!!')
    score += 1
    restart_state()

# Main Game
while True:
  # Fill Screen to erase previous frame
  # Try removing it and see what happens
  screen.fill(white)
  
  # To make keyboard inputs work
  pg.event.pump()
  
  # Get keyboard Input
  keys = pg.key.get_pressed()

  # Player Movement
  player_movement(keys)
  
  # Render all the objects
  render_all_objects()
  
  # Activate all detectors [Wall Collision, Tressure Collection, Game Completion]
  detect_collisions()
  
  pg.display.flip() # To update the screen
  clock.tick(60) # Setting game FPS
