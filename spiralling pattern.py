import turtle

spiral = turtle.Turtle()

for i in range(20):
    spiral.forward(i * 25)
    spiral.right(144)

turtle.done()