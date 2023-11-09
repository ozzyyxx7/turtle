import turtle
import random

class turtleRun:
    def __init__(self):
        #Initialize Value
        self.playing = False
        self.playerSpeed = 10
        self.score = 0
        self.bananaState = 0
        self.speedProb = 0
        self.bananaProb = 0

        #Set Menu Object
        self.selectPen = turtle.Turtle(visible=False)
        self.menuPen = turtle.Turtle(visible=False)

        #Set Game Object
        self.turtle_enemy = turtle.Turtle(visible=False)
        self.score_food = turtle.Turtle(visible=False)
        self.speed_food = turtle.Turtle(visible=False)
        self.bananaItem = turtle.Turtle(visible=False)
        self.scorePen = turtle.Turtle(visible=False)
        self.speedPen = turtle.Turtle(visible=False)
        self.bananaPen = turtle.Turtle(visible=False)

    def initMenu(self):
        #Draw Menu
        self.menuPen.penup()
        self.menuPen.write("SCORE BOARD", False , 'center', ('Arial', 30))
        self.menuPen.goto(0, 60)
        self.menuPen.write("START", False , 'center', ('Arial', 30))
        self.menuPen.goto(0, -60)
        self.menuPen.write("EXIT", False , 'center', ('Arial', 30))

        #initialize Selection Icon
        self.selectPen.showturtle()
        self.selectPen.penup()
        self.selectPen.goto(-60, 75)

        #Set Key Function
        turtle.onkeypress(self.upMenu, 'Up')
        turtle.onkeypress(self.downMenu, 'Down')
        turtle.onkeypress(self.enterMenu, 'Return')

        #Wait
        turtle.listen()
        turtle.mainloop()

    # -----Function For Menu-----
    def upMenu(self):
        if self.selectPen.pos()[1] == 15:
            self.selectPen.goto(-60, 75)
        elif self.selectPen.pos()[1] == -45:
            self.selectPen.goto(-120, 15)
        
    def downMenu(self):
        if self.selectPen.pos()[1] == 75:
            self.selectPen.goto(-120, 15)
        elif self.selectPen.pos()[1] == 15:
            self.selectPen.goto(-40, -45)

    def enterMenu(self):
        if self.selectPen.pos()[1] == 75:
            self.menuPen.clear()
            self.selectPen.hideturtle()
            self.initGameEnv()
        elif self.selectPen.pos()[1] == -45:
            turtle.bye()
    #-----------------------

    # -----Initialize Game Object-----
    def initPlayerTurtle(self):
        turtle.speed(0)
        turtle.up()
        turtle.shape('turtle')
        turtle.color('black')

    def initEnemyTurtle(self):
        self.turtle_enemy.showturtle()
        self.turtle_enemy.shape('turtle')
        self.turtle_enemy.color('red')
        self.turtle_enemy.speed(0)
        self.turtle_enemy.up()
        self.turtle_enemy.goto(0, 300)

    def initScoreFood(self):
        self.score_food.showturtle()
        self.score_food.shape('circle')
        self.score_food.color('green')
        self.score_food.speed(0)
        self.score_food.up()
        self.score_food.goto(0, -300)

    def initSpeedFood(self):
        self.speed_food.showturtle()
        self.speed_food.shape('circle')
        self.speed_food.color('blue')
        self.speed_food.speed(0)
        self.speed_food.up()
        self.speed_food.goto(100, -300)

    def initBananaItem(self):
        bananaItemPosX = random.randint(-490, 490)
        bananaItemPosY = random.randint(-490, 490)

        self.bananaItem.showturtle()
        self.bananaItem.shape('circle')
        self.bananaItem.color('yellow')
        self.bananaItem.speed(0)
        self.bananaItem.up()
        self.bananaItem.goto(bananaItemPosX, bananaItemPosY)
    #-----------------------

    def rotateEnemy(self):
        for heading in range(0, 360, 60):
            self.turtle_enemy.setheading(heading)

    def defScorePen(self):
        self.scorePen.penup()
        self.scorePen.goto(-490, -490)
        self.scorePen.write("SCORE : {}".format(self.score), False , 'left', ('Arial', 30))

    def defSpeedPen(self):
        self.speedPen.penup()
        self.speedPen.goto(-490, -460)
        self.speedPen.write("SPEED : {}".format(self.playerSpeed), False , 'left', ('Arial', 30))

    def defBananaPen(self):
        self.bananaPen.penup()
        self.bananaPen.goto(-490, -430)
        self.bananaPen.write("BANANA : {}".format(self.bananaState), False , 'left', ('Arial', 30))

    def redrawScore(self):
        self.score+=100
        self.scorePen.clear()
        self.scorePen.write("SCORE : {}".format(self.score), False , 'left', ('Arial', 30))

    def redrawSpeed(self):
        self.playerSpeed+=1
        self.speedPen.clear()
        self.speedPen.write("SPEED : {}".format(self.playerSpeed), False , 'left', ('Arial', 30))
    
    def turn_right(self):
        turtle.setheading(0)
    def turn_up(self):
        turtle.setheading(90)
    def turn_left(self):
        turtle.setheading(180)
    def turn_down(self):
        turtle.setheading(270)

    def play(self):
        turtle.forward(self.playerSpeed)
        enemy_angle = self.turtle_enemy.towards(turtle.pos())
        self.turtle_enemy.setheading(enemy_angle)
        self.turtle_enemy.forward(9)

        if turtle.distance(self.score_food) < 12:
            score_foodPosX = random.randint(-490, 490)
            score_foodPosY = random.randint(-490, 490)
            self.score_food.goto(score_foodPosX, score_foodPosY)
            self.redrawScore()

        if turtle.distance(self.speed_food) < 12:
            speed_foodPosX = random.randint(-490, 490)
            speed_foodPosY = random.randint(-490, 490)
            self.speed_food.goto(speed_foodPosX, speed_foodPosY)
            self.redrawSpeed()

        if turtle.distance(self.bananaItem) < 12:
            bananaPosX = random.randint(-490, 490)
            bananaPosY = random.randint(-490, 490)
            self.bananaItem.goto(bananaPosX, bananaPosY)

        if turtle.distance(self.turtle_enemy) >= 12:
            turtle.ontimer(self.play, 100)
        else:
            self.playing = False

    def start(self):
        if self.playing == False:
            self.playing = True
            self.play()

    def initGameEnv(self):
        turtle.onkeypress(self.turn_right, 'Right')
        turtle.onkeypress(self.turn_up, 'Up')
        turtle.onkeypress(self.turn_left, 'Left')
        turtle.onkeypress(self.turn_down, 'Down')
        turtle.onkeypress(self.start, 'space')

        self.defScorePen()
        self.defSpeedPen()
        self.defBananaPen()
        self.initPlayerTurtle()
        self.initEnemyTurtle()
        self.initScoreFood()
        self.initSpeedFood()
        self.initBananaItem()

        turtle.setup(1000, 1000)
        turtle.bgcolor('white')

        turtle.listen()

        turtle.mainloop()

if __name__ == '__main__':
    game = turtleRun()
#    game.initGameEnv()
    game.initMenu()