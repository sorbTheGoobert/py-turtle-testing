from turtle import Turtle, _CFG
import random, datetime

# def drawStar(t, size, op):
#     ogHeading = t.heading()
#     t.penup()
#     t.forward(size * 144 / 100)
#     t.right(90 + 72)
#     t.pendown()
#     t.begin_fill()
#     for i in range(5):
#         t.forward(size)
#         t.left(72)
#         t.forward(size)
#         t.right(72 * 2)
#     t.end_fill()
#     t.setheading(ogHeading)
#     t.penup()
#     t.backward(size * 144 / 100)
#     t.pendown()

class AfterImage:
    def __init__(self, pos, heading, color, colorspeed, tutel, size):
        self.artist = tutel
        self.size = size
        self.heading = heading
        self.color = {
            "current": {"r": color["r"], "g": color["g"], "b": color["b"]},
            "speed": colorspeed
        }
        self.pos = {"x": pos["x"], "y": pos["y"]}
        self.done = True
    def create(self, currentHeading, color):
        self.heading = currentHeading
        self.color["current"]["r"] = color["r"]
        self.color["current"]["g"] = color["g"]
        self.color["current"]["b"] = color["b"]
        self.done = False
        self.update()
    def draw(self):
        # Actually draw the stuff
        ogHeading = self.artist.heading()
        self.artist.penup()
        self.artist.forward(self.size * 144 / 100)
        self.artist.right(90 + 72)
        self.artist.pendown()
        self.artist.begin_fill()
        for i in range(5):
            self.artist.forward(self.size)
            self.artist.left(72)
            self.artist.forward(self.size)
            self.artist.right(72 * 2)
        self.artist.end_fill()
        self.artist.setheading(ogHeading)
        self.artist.penup()
        self.artist.backward(self.size * 144 / 100)
        self.artist.pendown()
    def update(self):
        self.draw()
        self.color["current"]["r"]+=min(self.color["current"]["r"] + self.color["speed"], 255)
        self.color["current"]["g"]+=min(self.color["current"]["g"] + self.color["speed"], 255)
        self.color["current"]["b"]+=min(self.color["current"]["b"] + self.color["speed"], 255)
        self.done = self.color["current"]["r"] == 255 and self.color["current"]["g"] == 255 and self.color["current"]["b"] == 255

class Star:
    def __init__(self, pos, size, speed, heading, tutel, colorspeed, afterimageCount):
        self.artist = tutel()
        self.rotation = {
            "speed": speed,
            "heading": heading
        }    
        self.pos = {"x": pos["x"], "y": pos["y"]}
        self.size = size
        self.color = {
            "current": {
                "r": random.randint(0, 255), "g": random.randint(0, 255), "b": random.randint(0, 255)
            },
            "mod": {
                "r": random.choice([colorspeed, -colorspeed]), "g": random.choice([colorspeed, -colorspeed]), "b": random.choice([colorspeed, -colorspeed])
            }
        }
        self.dt = 0
        self.time = {
            "before": int(datetime.datetime.now().strftime("%f")) / 1000 , 
            "after": int(datetime.datetime.now().strftime("%f")) / 1000 ,
            "lowest": 1000 / 10,
            "highest": 1000 / 60
        }
        self.done = False
        self.afterImages = []
        for _ in range(afterimageCount):
            self.afterImages.append(AfterImage(pos=pos, heading=heading, color=self.color["current"], colorspeed=colorspeed, tutel=self.artist, size=size))
    def drawAfterImages(self):
        for afterImage in self.afterImages:
            if afterImage.done:
                afterImage.create(self.rotation["heading"], self.color["current"])
            else:
                afterImage.update()
    def draw(self):
        # Actually draw the stuff
        ogHeading = self.artist.heading()
        self.artist.penup()
        self.artist.forward(self.size * 144 / 100)
        self.artist.right(90 + 72)
        self.artist.pendown()
        self.artist.begin_fill()
        for i in range(5):
            self.artist.forward(self.size)
            self.artist.left(72)
            self.artist.forward(self.size)
            self.artist.right(72 * 2)
        self.artist.end_fill()
        self.artist.setheading(ogHeading)
        self.artist.penup()
        self.artist.backward(self.size * 144 / 100)
        self.artist.pendown()
    def update(self):
        self.time["after"] = int(datetime.datetime.now().strftime("%f")) / 1000 # So the %f formatter takes date in "microseconds", or in other words 1 / 1000 of a MILLISECOND
        self.dt = abs(self.time["after"] - self.time["before"])
        self.dt = min(max(self.time["lowest"], self.dt), self.time["highest"])
        # print(self.time["before"], type(self.time["before"]))
        # print(self.time["after"], type(self.time["after"]))
        # print(self.dt)
        # print(self.rotation["speed"] * self.dt)
        # print(self.artist.heading())
        # print((self.artist.heading() + self.rotation["speed"] * self.dt) % 360)
        # print("##############################\n")
        
        # Initialize some stuff
        self.artist.screen.tracer(0)
        self.artist.screen.title("ASRIEL HOLY CRAP")
        self.artist.screen.colormode(255)
        self.artist.seth(self.rotation["heading"])
        self.artist.screen.delay(1000 / 60)
        self.artist.speed(0)
        r = self.color["current"]["r"]
        g = self.color["current"]["g"]
        b = self.color["current"]["b"]
        self.artist.setpos((self.pos["x"], self.pos["y"]))
        self.artist.pen(fillcolor=((r, g, b)), pencolor=((r, g, b)), pensize=1)

        self.drawAfterImages()
        self.draw()

        r += self.color["mod"]["r"]
        g += self.color["mod"]["g"]
        b += self.color["mod"]["b"]
        if r > 255 or r < 0:
            self.color["mod"]["r"] *= -1
            r += self.color["mod"]["r"]
        if g > 255 or g < 0:
            self.color["mod"]["g"] *= -1
            g += self.color["mod"]["g"]
        if b > 255 or b < 0:
            self.color["mod"]["b"] *= -1
            b += self.color["mod"]["b"]
        self.color["current"]["r"] = r
        self.color["current"]["g"] = g
        self.color["current"]["b"] = b

        self.time["before"] = self.time["after"]

        self.rotation["heading"] += self.rotation["speed"] * self.dt
        # self.rotation["heading"] += self.rotation["speed"]
        self.rotation["heading"] %= 360
        self.artist.screen.update()
        
        try:
            self.artist.clear()
        except:
            self.done = True
        

def main():

    # # Init tutel
    # tutel = Turtle()
    # tutel.screen.tracer(0)
    # tutel.screen.title("ASRIEL HOLY CRAP")
    # tutel.screen.delay(0)
    # tutel.speed(0)
    # tutel.seth(90)
    # tutel.screen.colormode(255)
    # r, g, b= random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    # mod = [random.randint(3, 6), random.randint(3, 6), random.randint(3, 6)]

    # newTutel = Star({"x": 100, "y": 100}, 250, 2)
    # print(newTutel.color["mod"]["r"])

    # tutel.pen(fillcolor=((r, g, b)), pencolor=((r, g, b)), pensize=1)
    # random.seed()
    # tutel.screen.colormode(255)
    # tutel.screen.bgcolor(0, 0, 0)

    # Init tutel
    tutel = Star(pos={"x": 0, "y": 0}, size=150, speed=0.05, heading=90.0, tutel=Turtle, colorspeed=1, afterimageCount=10)
    random.seed()

    while not tutel.done:
        tutel.update()


main()
