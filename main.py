#
# Turtle Challenge 4 - Generate a Random Walk
#
from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.speed(6)

def do_random_walk():

    pen_colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'turquoise']
    angle_turns = [0, 90, 180, 270,]

    timmy_the_turtle.pensize(7)
    timmy_the_turtle.pendown()

    for _ in range(100):

        timmy_the_turtle.pencolor(random.choice(pen_colors))
        timmy_the_turtle.lt(random.choice(angle_turns))
        timmy_the_turtle.forward(50)

    return

do_random_walk()

screen = Screen()
screen.exitonclick()












#
# Turtle Challenge 3 - Drawing Different Shapes
#
# from turtle import Turtle, Screen
# import random
#
# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.speed(2)
#
# def draw_shapes():
#     # Define the least and greatest number of sides of shapes
#     number_of_triangle_sides = 3
#     number_of_decagon_sides = 10
#
#     # Define original pen colors to draw shapes in
#     original_pen_colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'turquoise']
#
#     # Define list containing pen colors already used
#     already_used_pen_colors = []
#
#     # Put the pen down, ready to start drawing
#     timmy_the_turtle.pendown()
#
#     # Loop through all the shapes to be drawn
#     for shape_sides in range(number_of_triangle_sides, number_of_decagon_sides + 1):
#
#         # Calculate the turn angle for each side of current shape
#         shape_turn_angle = 360 / shape_sides
#
#         # Generate random index into original pen colors list
#         random_shape_pencolor_index = random.randint(0, len(original_pen_colors) - 1)
#
#         # Select the next random shape pen color
#         next_shape_pencolor = original_pen_colors[random_shape_pencolor_index]
#
#         # Check that next shape pen color has not already been randomly selected
#         while next_shape_pencolor in already_used_pen_colors:
#
#             # currently selected pen color has already been used, so generate another random index in to
#             # the original pen color list
#             random_shape_pencolor_index = random.randint(0, len(original_pen_colors) - 1)
#
#             # select the next random shape pen color
#             next_shape_pencolor = original_pen_colors[random_shape_pencolor_index]
#
#         # save new unused shape pen color in to list of already used pen colors
#         already_used_pen_colors.append(next_shape_pencolor)
#
#         # set pen color to be used on turtle
#         timmy_the_turtle.pencolor(next_shape_pencolor)
#
#         # draw the next shape
#         for _ in range(shape_sides):
#
#             # move turtle forward drawing next shape side
#             timmy_the_turtle.forward(100)
#
#             # turn the turtle ready for the next shape side
#             timmy_the_turtle.rt(shape_turn_angle)
#     return
#
# draw_shapes()
#
# screen = Screen()
# screen.exitonclick()
#
