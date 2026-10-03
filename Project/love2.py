import turtle
import math
import random

# Create Screen
screen = turtle.Screen()
screen.setup(800, 700)
screen.bgcolor("black")
screen.title("Colorful Heart")

# Create Turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

colors = [
    "red", "blue", "lime", "yellow",
    "cyan", "magenta", "orange", "pink"
]

# Draw Heart
for i in range(360):
    angle = math.radians(i)

    x = 16 * (math.sin(angle) ** 3)
    y = (13 * math.cos(angle)
         - 5 * math.cos(2 * angle)
         - 2 * math.cos(3 * angle)
         - math.cos(4 * angle))

    x *= 15
    y *= 15

    t.penup()
    t.goto(x, y)
    t.pendown()

    t.color(random.choice(colors))

    for _ in range(8):
        t.forward(6)
        t.backward(6)
        t.right(45)

screen.mainloop()