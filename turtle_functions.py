import turtle as t
import random
from math import sin, cos, pi


def random_lines():
    """
    Draws a specified number of random lines.
    """
    count = t.numinput("Počet čar", "Zadej počet čar", 1, 1, 100)
    for i in range(int(count)):
        t.penup()
        t.color(random.random(), random.random(), random.random())
        t.goto(random.randint(-200, 200), random.randint(-200, 200))
        t.pendown()
        t.goto(random.randint(-200, 200), random.randint(-200, 200))


def random_spirals():
    """
    Draws a specified number of random spirals.
    """
    count = t.numinput("Počet spirál", "Zadej počet spirál", 1, 1, 100)
    for _ in range(int(count)):
        t.penup()
        t.color(random.random(), random.random(), random.random())
        t.goto(random.randint(-200, 200), random.randint(-200, 200))
        start_angle = random.randint(0, 360)
        t.pendown()

        d = random.randint(10, 50)
        cur_r = 0
        start_x, start_y = t.position()

        for _ in range(random.randint(2, 5)):
            for a in range(1, 360, 4):
                r = cur_r + d * a / 360.0
                a_rad = (a + start_angle) * pi / 180.0
                y = start_y + r * sin(a_rad)
                x = start_x + r * cos(a_rad)
                t.goto(x, y)
            cur_r += d


def square_spiral():
    """
    Draws a square spiral.
    """
    side_length = 10
    for _ in range(20):
        t.forward(side_length)
        t.right(90)
        side_length += 10


def go_to_click(x, y):
    """
    Moves the turtle to the click position.
    """
    t.color(random.random(), random.random(), random.random())
    t.goto(x, y)
