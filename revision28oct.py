import turtle

def move(x, y):
    # Moves turtle to a clicked location, drawing while moving
    t.goto(x, y)

# Initialize the turtle
t = turtle.Turtle()
t.screen.bgcolor("lightblue")
t.screen.title("Draw Your Own Turtle")

# Set the fill color (change "red" to any color you want)
t.fillcolor("skyblue")

# Start filling the shape
t.begin_fill()

# Use onscreenclick to call the move function for drawing
turtle.onscreenclick(move)

# Set up the screen to listen for events
turtle.listen()

# End fill after you press a key to finish the shape
def finish_shape():
    t.end_fill()  # Ends filling the shape with the specified color

# Bind a key (e.g., "space") to finish the shape and apply color
t.screen.onkey(finish_shape, "d")

# Finish up the turtle graphics
turtle.done()
