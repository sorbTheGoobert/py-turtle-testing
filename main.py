from turtle import Turtle, _CFG
import random

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
    tutel.screen.tracer(0)
    tutel.screen.title("ASRIEL HOLY CRAP")
    tutel.screen.delay(0)
    tutel.speed(0)
    tutel.seth(90)
    tutel.screen.colormode(255)
    # tutel.hideturtle()
    r, g, b= random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    # r, g, b, a = 255, 255, 255, 1
    mod = [random.randint(3, 6), random.randint(3, 6), random.randint(3, 6)]
    print(mod)
    # tutel.fillcolor((r, g, b))
    tutel.pen(fillcolor=((r, g, b)), pencolor=((r, g, b)), pensize=1)
    # try:
    #     tutel.pencolor(128, 255, 128 ,0.5)
    # except:
    #     raise Exception("Nah NO ALPHA")
    random.seed()
    tutel.screen.colormode(255)
    tutel.screen.bgcolor(0, 0, 0)
    
    while True:
        tutel.right(1)
        r += mod[0]
        g += mod[1]
        b += mod[2]
        if r > 255 or r < 0:
            mod[0] *= -1
            r += mod[0]
        if g > 255 or g < 0:
            mod[1] *= -1
            g += mod[1]
        if b > 255 or b < 0:
            mod[2] *= -1
            b += mod[2]
        tutel.pen(fillcolor=((r, g, b)), pencolor=((r, g, b)), pensize=1)
        temphead = tutel.heading()
        n = 10
        delta = [int(r / n), int(g / n), int(b / n)]
        for star in range(n):
            tutel.pen(fillcolor=(delta[0] * (star + 1), delta[1] * (star + 1), delta[2] * (star + 1)), pencolor=(delta[0] * (star + 1), delta[1] * (star + 1), delta[2] * (star + 1)), pensize=1)
            drawStar(t=tutel, size=250, op=1)
            tutel.right(5)
        # drawStar(t=tutel, size=250, op=1)
        tutel.seth(temphead)
        tutel.screen.update()
        # time.sleep(0.05)
        # time.slee)
        tutel.clear()
        

main()