import turtle

cursor = turtle.Screen()


# method to perform action
def function(x, y):
    turtle.goto(x, y)
    turtle.write(str(x) + "," + str(y))


# onclick action
cursor.onclick(function)
cursor.mainloop()
turtle.done()