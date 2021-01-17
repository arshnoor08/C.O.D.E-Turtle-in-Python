import turtle
turtle.title("Pattern 1")
bob = turtle.Turtle()
bob.begin_fill() 
bob.color("#607D8B", "#FFA726")
bob.speed(20) 

for i in range(15):
    bob.forward(150)
    bob.left(168)
bob.end_fill()
turtle.done()