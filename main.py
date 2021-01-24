#!/usr/bin/python
import turtle as tu

tu.tracer(0,0)
tu.bgcolor("black")
tu.right(90)
tu.forward(450)
tu.left(5)

screen = tu.Screen()
screen.colormode(255)

colors = ["white", "orange", "yellow", "green", "blue", "pink", "purple", (192, 192, 192)]
lengths = [90,80,70,60,50,40,30,20,10]

def thingy(length):
    for i in range(72):
        tu.forward(length)
        tu.right(5)
        tu.backward(length)
        tu.update()
    tu.backward(length)

for i in range(15):
    for c, l in zip(colors, lengths):
        tu.color(c)
        thingy(l)
    tu.backward(10)
    tu.penup()
    tu.right(24)
    tu.forward(450)
    tu.pendown()

tu.done()
