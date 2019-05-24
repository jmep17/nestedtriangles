# Importing turtle
from turtle import *

# Declaring variables and values
triangle_quantity = 4
z = 0
coordinate_x = 0
coordinate_y = 0
side_lengths = 20

# Creating loop (z)
# Loop repeats until number of loops is equal to triangle amount
while z < triangle_quantity:
# Building each triangle:
    for i in range(triangle_quantity):
        penup()
        goto(coordinate_x,coordinate_y)
        pendown()

        for sides in range(3):
            forward(side_lengths)
            left(120)
# Increasing values of variables
        z += 1
        coordinate_x += -10
        coordinate_y += -7
        side_lengths += 20
