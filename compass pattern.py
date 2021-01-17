import turtle
import math
turtle.title("Moving star pattern - pattern #2")
bob = turtle.Turtle()
bob.color("#39a275","#82caaf")
bob.speed(75)
bob.pensize(1.125)
bob.begin_fill()
for i in range(300):
    bob.forward(math.sqrt(i)*10)
    bob.left(168)
bob.end_fill()
turtle.done()