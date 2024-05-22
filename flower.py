# Import necessary modules
import turtle as t
import colorsys as cs

# Set up the turtle graphics environment
t.speed(1)         # Set the speed of the turtle
t.tracer(10)        # Control the animation speed (higher values = faster drawing)
t.width(2)         # Set the width of the turtle's pen
t.bgcolor("black") # Set the background color of the canvas

# Draw a colorful geometric pattern using nested loops
for i in range(25):
    for j in range(25):
        # Set the color of the turtle's pen using HSV color model
        t.color(cs.hsv_to_rgb(i/15, j/25, 1))
    
        # Draw a series of arcs to create the pattern
        t.right(90)
        t.circle(150 - j * 4, 90)
        t.left(90)
        t.circle(150 - j * 4, 90)
        t.right(180)
        t.circle(25, 24)
    
    # Hide the turtle cursor for a cleaner look
    t.hideturtle()

# Finish the turtle graphics drawing
t.done()
