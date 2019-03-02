#!/usr/bin/python
import turtle as tu

tu.tracer(0,0)
tu.bgcolor("black")
tu.right(90)
tu.forward(450)
tu.left(5)
for i in range(15):
  tu.color("white")
  for i in range(72):
    tu.forward(90)
    tu.right(5)
    tu.backward(90)
    tu.update()
  tu.backward(90)
  tu.color("red")

  for i in range(72):
    tu.forward(80)
    tu.right(5)
    tu.backward(80)
    tu.update()
  tu.backward(80)
  tu.color("orange")

  for i in range(72):
    tu.forward(70)
    tu.right(5)
    tu.backward(70)
    tu.update()
  tu.backward(70)
  tu.color("yellow")

  for i in range(72):
    tu.forward(60)
    tu.right(5)
    tu.backward(60)
    tu.update()
  tu.backward(60)

  tu.color("green")

  for i in range(72):
    tu.forward(50)
    tu.right(5)
    tu.backward(50)
    tu.update()
  tu.backward(50)

  tu.color("blue")

  for i in range(72):
    tu.forward(40)
    tu.right(5)
    tu.backward(40)
    tu.update()
  tu.backward(40)

  tu.color("pink")

  for i in range(72):
    tu.forward(30)
    tu.right(5)
    tu.backward(30)
    tu.update()
  tu.backward(30)

  tu.color("purple")

  for i in range(72):
    tu.forward(20)
    tu.right(5)
    tu.backward(20)
    tu.update()
  tu.backward(20)
  tu.colormode(255)
  tu.color((192, 192, 192))

  for i in range(72):
    tu.forward(10)
    tu.right(5)
    tu.backward(10)
    tu.update()
  tu.backward(10)
  tu.penup()
  tu.right(24)
  tu.forward(450)

  tu.pendown()
tu.done()
