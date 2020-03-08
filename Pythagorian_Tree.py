import turtle
import math
# side = int(input('Введите начальную длину стороны фрактала: '))
# N = int(input("Введите уровень рекурсии: "))
Pencil = turtle.Turtle()

Pencil.penup()
Pencil.goto(-50, -200)
Pencil.pendown()

Pencil.getscreen().bgcolor('#ee9086')
Pencil.pensize(1)
Pencil.shape('classic')
Pencil.color('blue', 'orange')
Pencil.speed(5)

side = turtle.Screen().numinput("Дерево Пифагора", "Длина стороны: ", 100, minval=10, maxval=1000)
N = turtle.Screen().numinput("Дерево Пифагора", "Уровень рекурсии: ", 0, minval=0, maxval=20)
tilt = turtle.Screen().numinput("Дерево Пифагора", "Коэффициент наклона дерева: ", 0, minval=-1, maxval=1)
angle = 45*(tilt+1)


def square(drawer, size, recursion_level, p):
    if recursion_level < 1:
        return
    drawer.begin_fill()
    for i in range(4):
        if p == 0:
            drawer.forward(size)
            if i == 0:
                dir = drawer.heading()
                drawer.right(angle)
                square(drawer, size*math.cos(math.radians(angle)), recursion_level-1, 0)  # Рисуем ветку справа
                drawer.setheading(dir)
            if i == 1:
                dir = drawer.heading()
                drawer.right(90+angle)
                square(drawer, size*math.sin(math.radians(angle)), recursion_level-1, 1)  # Рисуем ветку слева
                drawer.setheading(dir)
            drawer.left(90)
        else:
            drawer.forward(size)
            if i == 1:
                dir = drawer.heading()
                drawer.right(angle)
                square(drawer, size*math.cos(math.radians(angle)), recursion_level - 1, 0)  # Рисуем ветку справа
                drawer.setheading(dir)
            if i == 2:
                dir = drawer.heading()
                drawer.right(90+angle)
                square(drawer, size*math.sin(math.radians(angle)), recursion_level - 1, 1)  # Рисуем ветку слева
                drawer.setheading(dir)
            drawer.left(90)
    drawer.end_fill()


square(Pencil, side, N, 1)

turtle.done()
