#!/usr/bin/python
import turtle

turtle.speed(0)
turtle.bgcolor("black")
turtle.right(90)
turtle.forward(450)
turtle.left(5)
for i in range(15):
  turtle.color("white")
  for i in range(72):
    turtle.forward(90)
    turtle.right(5)
    turtle.backward(90)

  turtle.backward(90)
  turtle.color("red")

  for i in range(72):
    turtle.forward(80)
    turtle.right(5)
    turtle.backward(80)

  turtle.backward(80)
  turtle.color("orange")

  for i in range(72):
    turtle.forward(70)
    turtle.right(5)
    turtle.backward(70)

  turtle.backward(70)
  turtle.color("yellow")

  for i in range(72):
    turtle.forward(60)
    turtle.right(5)
    turtle.backward(60)
 
  turtle.backward(60)

  turtle.color("green")

  for i in range(72):
    turtle.forward(50)
    turtle.right(5)
    turtle.backward(50)

  turtle.backward(50)

  turtle.color("blue")

  for i in range(72):
    turtle.forward(40)
    turtle.right(5)
    turtle.backward(40)

  turtle.backward(40)

  turtle.color("pink")

  for i in range(72):
    turtle.forward(30)
    turtle.right(5)
    turtle.backward(30)

  turtle.backward(30)

  turtle.color("purple")

  for i in range(72):
    turtle.forward(20)
    turtle.right(5)
    turtle.backward(20)

  turtle.backward(20)
  turtle.colormode(255)
  turtle.color((192, 192, 192))

  for i in range(72):
    turtle.forward(10)
    turtle.right(5)
    turtle.backward(10)

  turtle.backward(10)
  turtle.penup()
  turtle.right(24)
  turtle.forward(450)
  
  turtle.pendown()
