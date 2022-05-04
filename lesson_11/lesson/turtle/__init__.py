import turtle

Pencil = turtle.Turtle()
Background = turtle.Screen()
Pencil.pencolor('red')
Background.bgcolor('black')

Pencil.pensize(1)
a = 0
b = 0

Pencil.speed(0)
Pencil.penup()
Pencil.goto(0, 200)
Pencil.pendown()
       
while True:
    Pencil.forward(a)
    Pencil.right(b)
    a += 2
    b += 1
    if b == 210:
        break
    Pencil.hideturtle()

turtle.done()


























































