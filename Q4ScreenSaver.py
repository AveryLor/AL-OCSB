# NAME OF AUTHOR: Avery Lor
# NAME OF THE PROGRAM: Pygame Practice
# DATE OF CREATION: 2022-05-30
# PURPOSE OF PROGRAM: Demonstrate Pygame

import pygame
from pygame import Color, draw, display, time
from pygame import draw
from pygame import display
from pygame import time

# VARIABLE DEFINTION

yellow_Center_Ball_X = 50  # location of ball
yellow_Center_Ball_Y = 50  # location of ball
gameDisplay = 0  # Used for display
red_Center_Ball_X = 70  # location of ball
red_Center_Ball_Y = 50  # location of ball


pygame.init() # to be used as a delay within while loop
clock = time.Clock()  # to be used as a delay within while loop
gameDisplay = display.set_mode((900, 500)) # creating a blank canvas
gameDisplay.fill(Color('light blue')) # Make white background



# Moving the ball continually

while True:

    # Going up to down
    while yellow_Center_Ball_Y < 400:
        gameDisplay.fill(Color('light blue'))
        clock.tick(100)
        draw.circle(gameDisplay, Color("yellow"), (yellow_Center_Ball_X, yellow_Center_Ball_Y), 30)
        yellow_Center_Ball_Y += 3

        # Red ball
        draw.circle(gameDisplay, Color("red"), (red_Center_Ball_X, red_Center_Ball_Y), 30)
        red_Center_Ball_Y += 3
        display.flip()

    # Going left to right
    while yellow_Center_Ball_X < 800:
        gameDisplay.fill(Color('light blue'))
        clock.tick(100)
        draw.circle(gameDisplay, Color("yellow"), (yellow_Center_Ball_X, yellow_Center_Ball_Y), 30)
        yellow_Center_Ball_X += 3

        # Red ball
        draw.circle(gameDisplay, Color("red"), (red_Center_Ball_X, red_Center_Ball_Y), 30)
        red_Center_Ball_X += 3
        display.flip()

    # Going down to up
    while yellow_Center_Ball_Y > 100:
        gameDisplay.fill(Color('light blue'))
        clock.tick(100)
        draw.circle(gameDisplay, Color("yellow"), (yellow_Center_Ball_X, yellow_Center_Ball_Y), 30)
        yellow_Center_Ball_Y -= 3

        # Red ball
        draw.circle(gameDisplay, Color("red"), (red_Center_Ball_X, red_Center_Ball_Y), 30)
        red_Center_Ball_Y -= 3
        display.flip()


    # Going left to right
    while yellow_Center_Ball_X > 100:
        gameDisplay.fill(Color('light blue'))
        clock.tick(100)
        draw.circle(gameDisplay, Color("yellow"), (yellow_Center_Ball_X, yellow_Center_Ball_Y), 30)
        yellow_Center_Ball_X -= 3

        # Red ball
        draw.circle(gameDisplay, Color("red"), (red_Center_Ball_X, red_Center_Ball_Y), 30)
        red_Center_Ball_X -= 3
        display.flip()

