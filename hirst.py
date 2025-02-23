import random
import turtle

turtle.colormode(255)

# Initialize turtle
tim = turtle.Turtle()
tim.penup()
tim.hideturtle()

# Define color palette
colors = [
    (229, 228, 226), (225, 223, 224), (199, 176, 117), (124, 37, 24),
    (208, 221, 212), (166, 106, 57), (6, 57, 83), (185, 158, 54),
    (220, 224, 228), (108, 68, 84), (113, 161, 175), (40, 37, 35),
    (23, 122, 173), (64, 153, 139), (77, 40, 48), (90, 142, 53),
    (9, 67, 47), (180, 97, 80), (131, 39, 41), (211, 202, 152),
    (140, 172, 157), (176, 152, 158), (178, 201, 186), (218, 181, 171),
    (169, 200, 209), (205, 183, 188), (41, 75, 61), (148, 116, 122),
    (39, 72, 81), (97, 138, 153)
]

# Fixed parameters
DOT_SIZE = 30
STEP_SIZE = 50
GRID_SIZE = 10
START_X = -300
START_Y = -300


# Function to draw a dot at the turtle's position
def make_dot():
    tim.dot(DOT_SIZE, random.choice(colors))


# Function to draw the Hirst painting
def draw_hirst_painting():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            make_dot()
            tim.forward(STEP_SIZE)
        # Move to the next row
        tim.setx(START_X)
        tim.sety(START_Y + (row + 1) * STEP_SIZE)


# Set the initial position and draw the painting
tim.setpos(START_X, START_Y)
draw_hirst_painting()

# Exit on click
screen = turtle.Screen()
screen.exitonclick()
