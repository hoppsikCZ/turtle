import turtle as t
import random


def random_lines():
    count = t.numinput("Počet čar", "Zadej počet čar", 1, 1, 100)
    for i in range(int(count)):
        t.penup()
        t.color(random.random(), random.random(), random.random())
        t.goto(random.randint(-200, 200), random.randint(-200, 200))
        t.pendown()
        t.goto(random.randint(-200, 200), random.randint(-200, 200))


def random_spirals():
    count = t.numinput("Počet spirál", "Zadej počet spirál", 1, 1, 100)
    for i in range(int(count)):
        t.penup()
        t.color(random.random(), random.random(), random.random())
        t.goto(random.randint(-200, 200), random.randint(-200, 200))
        t.pendown()
        side_length = 10
        for a in range(random.randint(3, 7)):
            t.forward(side_length)
            t.right(90)
            side_length += 10


def square_spiral():
    side_length = 10
    for _ in range(20):
        t.forward(side_length)
        t.right(90)
        side_length += 10