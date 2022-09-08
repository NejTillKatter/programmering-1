import turtle, random, time

olle = turtle.Turtle()

olle.shape("turtle")

olle.shapesize(4)

olle.pensize(2)

olle.speed(2)

def up():
    olle.seth(90)
    olle.forward(20)

def down():
    olle.seth(270)
    olle.forward(20)

def right():
    olle.seth(0)
    olle.forward(20)

def left():
    olle.seth(180)
    olle.forward(20)
      
def click(x,y):
    olle.goto(x,y)

turtle.onkey(up,'Up')
turtle.onkey(down,'Down')
turtle.onkey(right,'Right')
turtle.onkey(left,'Left')

turtle.listen()

turtle.done()