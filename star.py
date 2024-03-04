import turtle

a = turtle.Turtle()
a.speed()
a.getscreen().bgcolor("black")
a.penup()
a.pendown
a.color("skyblue")
a.speed(25)

# Define the starting position
start_position = (-180, 50)

# Move the turtle to the starting position
a.penup()
a.goto(start_position)
a.pendown()

def star(turtle, size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.pensize(2)
            turtle.forward(size)
            next_pos = turtle.position()
            next_heading = turtle.heading()
            star(turtle, size / 3)
            turtle.penup()
            turtle.setposition(next_pos)
            turtle.setheading(next_heading)
            turtle.pendown()
            turtle.left(216)
        turtle.end_fill()

star(a, 360)

turtle.done()
