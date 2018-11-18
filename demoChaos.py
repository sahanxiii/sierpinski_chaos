import turtle
import hw2Functions
import random

bob = turtle.Turtle()
win = turtle.Screen()
bob.speed(0)
win.bgcolor("black")
win.setworldcoordinates(0, 0, 700, 700)
win.title("Sahan Shrestha's Chaos Game")
x1 = 30
y1 = 30
x2 = 640
y2 = 30
x3 = 335
y3 = 670
bob.up()
bob.goto(x1, y1)
bob.dot(10, "green")
bob.down()
bob.goto(x2, y2)
bob.dot(10, "blue")
bob.goto(x3, y3)
bob.dot(10, "red")
bob.goto(x1, y1)
bob.up()
bob.goto(x3, 335)
bob.pos()
bob.dot(10, "yellow")
bob.hideturtle()

for i in range(20000):
    x = bob.xcor()
    y = bob.ycor()

    val = random.randint(0,2)
    if val == 0:

        point = hw2Functions.midPoint(x1, y1, x, y)
        #y = hw2Functions.midPoint(y1, y)
        bob.goto(point)
        bob.dot(2,"green")
        #bob.goto(hw2Functions.midPoint(x1, y1, bob.xcor(), floatbob.ycor()))
    elif val == 1:
        #print(val)
        point = hw2Functions.midPoint(x2, y2, x, y)
        #y = hw2Functions.midPoint(y2, bob.ycor())
        bob.goto(point)
        bob.dot(2, "blue")
        #bob.goto(hw2Functions.midPoint(x2, y2, bob.xcor(), bob.ycor()))
        #print(point)
    else:
        #print(val)
        point = hw2Functions.midPoint(x3, y3, x, y)
        #y = hw2Functions.midPoint(y3, bob.ycor())
        bob.goto(point)
        bob.dot(2, "red")
        #bob.goto(hw2Functions.midPoint(x3, y3, bob.xcor(), bob.ycor()))
        #print(point)
    #bob.goto(hw2Functions.midPoint(x1, y1, bob.xcor(), bob.ycor()))

    #bob.goto(hw2Functions.midPoint(x, y, int(turtle.xcor()), int(turtle.ycor())))






win.exitonclick()