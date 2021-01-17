import turtle

turtle.shape("turtle") # square, circle, classic, arrow
harry = turtle.Turtle()
harry.penup() # lift up the pen -- no line is drawn
harry.goto(100,100) #move to the first quadrant
harry.pendown() # put down the pen -- line in drawn
turtle.screensize(canvwidth=500, canvheight=600, 
                  bg="#ABEBC6") 
def makestar():
    for i in range(5):
        harry.forward(300)
        harry.right(216)
makestar()
turtle.done()