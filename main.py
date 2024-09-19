from turtle import Turtle
import random
import time

def drawStar(t, size, op):
    ogHeading = t.heading()
    t.penup()
    t.forward(size * 144 / 100)
    t.right(90 + 72)
    t.pendown()
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.left(72)
        t.forward(size)
        t.right(72 * 2)
    t.end_fill()
    t.setheading(ogHeading)
    t.penup()
    t.backward(size * 144 / 100)
    t.pendown()


def main():
    # Init tutel
    tutel = Turtle()
    tutel.screen.title("ASRIEL HOLY CRAP")
    tutel.seth(90)
    tutel.speed(0)
    tutel.screen.colormode(255)
    tutel.hideturtle()
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    mod = [1, 1, 1]
    # tutel.fillcolor((r, g, b))
    tutel.pen(fillcolor=(r, g, b), pencolor=(r, g, b), pensize=1)
    try:
        tutel.pencolor(128, 255, 128 ,0.5)
    except:
        raise Exception("Nah NO ALPHA")
    random.seed()
    tutel.screen.delay(0)
    tutel.screen.bgcolor((0, 0, 0))
    while True:
        temphead = tutel.heading()
        for star in range(10):
            tutel.pen(fillcolor=(r, g, b, star/100), pencolor=(r, g, b), pensize=1)
            drawStar(t=tutel, size=100)
            tutel.right(1)
        tutel.seth(temphead)
        tutel.right(1)
        r += 3 * mod[0]
        g += 3 * mod[1]
        b += 3 * mod[2]
        if r > 255 or r < 0:
            mod[0] *= -1
            r += 3 * mod[0]
        if g > 255 or g < 0:
            mod[1] *= -1
            g += 3 * mod[1]
        if b > 255 or b < 0:
            mod[2] *= -1
            b += 3 * mod[2]
        tutel.pen(fillcolor=(r, g, b), pencolor=(r, g, b), pensize=1)
        time.sleep(0.01)
        

main()