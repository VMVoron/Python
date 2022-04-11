import turtle as t
def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.shape('turtle')
    t.begin_fill()
    for counter in range (1, 3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()
t.penup()
t.speed('slow')
print(t.window_width())
print(t.window_height())
t.bgcolor('Dodger blue')
#ступни
t.goto(-100, -150)
rectangle(50, 20, 'aquamarine')
t.goto(-30, -150)
rectangle(50, 20, 'aquamarine')
#ноги
t.goto(-25, -50)
rectangle(15, 100, 'lemon chiffon')
t.goto(-55, -50)
rectangle(-15, 100, 'lemon chiffon')
#туловище
t.goto(-90, 100)
rectangle(100, 150, 'deep pink')
#руки
t.goto(-150, 70)
rectangle(60, 15, 'misty rose')
t.goto(-150, 110)
rectangle(15, 40, 'misty rose')
t.goto(10, 70)
rectangle(60, 15, 'misty rose')
t.goto(55, 110)
rectangle(15, 40, 'misty rose')
#кисти
t.goto(-155, 130)
rectangle(25, 25, 'purple')
t.goto(-147, 130)
rectangle(10, 15, t.bgcolor())
t.goto(50, 130)
rectangle(25, 25, 'purple')
t.goto(58, 130)
rectangle(10, 15, t.bgcolor())
#шея
t.goto(-50, 120)
rectangle(15, 20, 'aquamarine')
#голова
t.goto(-85, 170)
rectangle(80, 50, 'peach puff')
#глаза
t.goto(-60, 160)
rectangle(30, 10, 'white')
t.goto(-60, 160)
rectangle(5, 5, 'black')
t.goto(-45, 155)
rectangle(5, 5, 'black')
#рот
t.goto(-65, 135)
t.right(5)
rectangle(40, 5, 'black')
t.hideturtle()