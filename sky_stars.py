import turtle as t
from random import randint, random
def draw_star(points, size, col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180/points)
    t.color(col)
    t.begin_fill()
    for i in range (points):
        t.forward(size)
        t.right(angle)
    t.end_fill()


#mainbody
t.Screen().bgcolor('dark blue')
t.hideturtle()
t.speed(0)
while True:
    points = randint(2, 5) * 2 + 1
    size = randint(10, 50)
    x = randint(-350, 300)
    y = randint(-250, 250)
    col = (random(), random(), random())
    draw_star(points, size, col, x, y)





