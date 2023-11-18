import turtle
import random
import threading
import time
import pygame.mixer

class turtleRun:
    def __init__(self):
        turtle.setup(1000, 1000)

        #Initialize Value
        self.playing = False
        self.playerSpeed = 10
        self.enemyTurtleSpeed = 9
        self.score = 0
        self.bananaState = 0
        self.speedProb = 0
        self.bananaProb = 0
        self.currentWindow = 0
        self.itemGetCheck = 0
        self.itemThrowCheck = 0

        self.mapSizeLLX = -450
        self.mapSizeURX = 450
        self.mapSizeLLY = -450
        self.mapSizeURY = 400
        self.mapMargin = 40

        self.availMapLLX = self.mapSizeLLX + self.mapMargin
        self.availMapURX = self.mapSizeURX - self.mapMargin
        self.availMapLLY = self.mapSizeLLY + self.mapMargin
        self.availMapURY = self.mapSizeURY - self.mapMargin


        window = turtle.Screen()
        window.bgcolor('black')
        window.title('Turtle Run')

        self.imageLogoPath = './data/image/logo.gif'
        self.imageTitlePath = './data/image/title.gif'
        self.imageStartPath = './data/image/start.gif'
        self.imageScoreBoardPath = './data/image/score_board.gif'
        self.imageExitPath = './data/image/exit.gif'
        self.imageSelectedStartPath = './data/image/selected_start.gif'
        self.imageSelectedScoreBoardPath = './data/image/selected_score_board.gif'
        self.imageSelectedExitPath = './data/image/selected_exit.gif'

        turtle.register_shape(self.imageLogoPath)
        turtle.register_shape(self.imageTitlePath)
        turtle.register_shape(self.imageStartPath)
        turtle.register_shape(self.imageScoreBoardPath)
        turtle.register_shape(self.imageExitPath)
        turtle.register_shape(self.imageSelectedStartPath)
        turtle.register_shape(self.imageSelectedScoreBoardPath)
        turtle.register_shape(self.imageSelectedExitPath)

        self.logo = turtle.Turtle(visible=False)
        self.logo.shape(self.imageLogoPath)
        self.logo.speed(0)
        self.logo.penup()

        self.title = turtle.Turtle(visible=False)
        self.title.shape(self.imageTitlePath)
        self.title.speed(0)
        self.title.penup()

        self.startButton = turtle.Turtle(visible=False)
        self.startButton.shape(self.imageSelectedStartPath)
        self.startButton.speed(0)
        self.startButton.penup()

        self.scoreBoard = turtle.Turtle(visible=False)
        self.scoreBoard.shape(self.imageScoreBoardPath)
        self.scoreBoard.speed(0)
        self.scoreBoard.penup()

        self.exit = turtle.Turtle(visible=False)
        self.exit.shape(self.imageExitPath)
        self.exit.speed(0)
        self.exit.penup()

        #Set Game Object
        self.turtle_enemy = turtle.Turtle(visible=False)
        self.score_food = turtle.Turtle(visible=False)
        self.item = turtle.Turtle(visible=False)
        self.speed_food = turtle.Turtle(visible=False)
        self.bananaItem = turtle.Turtle(visible=False)
        self.scorePen = turtle.Turtle(visible=False)
        self.speedPen = turtle.Turtle(visible=False)
        self.bananaPen = turtle.Turtle(visible=False)
        self.mapDrawingPen = turtle.Turtle(visible=False)

        pygame.init()

        self.logoSoundPath = './data/sound/logo.mp3'
        self.jumpSoundPath = './data/sound/jump.mp3'
        self.menuBgmPath = './data/sound/menu_bgm.mp3'
        self.gameBgmPath = './data/sound/game_bgm.mp3'
        self.buttonMoveSoundPath = './data/sound/button_move.mp3'

        self.logoSound = pygame.mixer.Sound(self.logoSoundPath) 
        self.jumpSound = pygame.mixer.Sound(self.jumpSoundPath) 
        self.menuBgm = pygame.mixer.Sound(self.menuBgmPath)
        self.gameBgm = pygame.mixer.Sound(self.gameBgmPath)
        self.buttonMoveSound = pygame.mixer.Sound(self.buttonMoveSoundPath)

    def initLogo(self):
        self.logo.showturtle()
        self.logoSound.play()
        time.sleep(1.5)
        self.logo.hideturtle()

    def initMenu(self):
        self.menuBgm.play(loops=-1)

        self.title.goto(0, 250)
        self.startButton.goto(0, 0)
        self.scoreBoard.goto(0, -75)
        self.exit.goto(0, -150)

        self.title.showturtle()
        self.startButton.showturtle()
        self.scoreBoard.showturtle()
        self.exit.showturtle()

        #Set Key Function
        turtle.onkeypress(self.upMenu, 'Up')
        turtle.onkeypress(self.downMenu, 'Down')
        turtle.onkeypress(self.enterMenu, 'Return')

        #Wait
        turtle.listen()

    # -----Function For Menu-----
    def upMenu(self):
        self.buttonMoveSound.play()
        if self.exit.shape() == self.imageSelectedExitPath:
            self.exit.shape(self.imageExitPath)
            self.scoreBoard.shape(self.imageSelectedScoreBoardPath)
        elif self.scoreBoard.shape() == self.imageSelectedScoreBoardPath:
            self.scoreBoard.shape(self.imageScoreBoardPath)
            self.startButton.shape(self.imageSelectedStartPath)
        
    def downMenu(self):
        self.buttonMoveSound.play()
        if self.startButton.shape() == self.imageSelectedStartPath:
            self.startButton.shape(self.imageStartPath)
            self.scoreBoard.shape(self.imageSelectedScoreBoardPath)
        elif self.scoreBoard.shape() == self.imageSelectedScoreBoardPath:
            self.scoreBoard.shape(self.imageScoreBoardPath)
            self.exit.shape(self.imageSelectedExitPath)

    def enterMenu(self):
        self.buttonMoveSound.play()
        if self.startButton.shape() == self.imageSelectedStartPath:
            self.initGameEnv()
        elif self.exit.shape() == self.imageSelectedExitPath:
            turtle.bye()
    #-----------------------

    # -----Initialize Game Object-----
    def initPlayerTurtle(self):
        turtle.speed(0)
        turtle.up()
        turtle.shape('turtle')
        turtle.color('white')

    def initEnemyTurtle(self):
        self.enemyTurtlePosX = random.randint(self.availMapLLX, self.availMapURX)
        self.enemyTurtlePosY = random.randint(self.availMapLLX, self.availMapURX)
        
        self.turtle_enemy.showturtle()
        self.turtle_enemy.shape('turtle')
        self.turtle_enemy.color('red')
        self.turtle_enemy.speed(-1)
        self.turtle_enemy.up()
        self.turtle_enemy.goto(self.enemyTurtlePosX, self.enemyTurtlePosY)

    def initScoreFood(self):
        self.scorePosX = random.randint(self.availMapLLX, self.availMapURX)
        self.scorePosY = random.randint(self.availMapLLY, self.availMapURY)

        self.score_food.showturtle()
        self.score_food.shape('circle')
        self.score_food.color('green')
        self.score_food.speed(0)
        self.score_food.up()
        self.score_food.goto(self.scorePosX, self.scorePosY)

    def initItem(self):
        self.itemPosX = 1000
        self.itemPosY = 1000

        self.item.shape('circle')
        self.item.color('blue')
        self.item.speed(0)
        self.item.up()
        self.item.goto(self.itemPosX, self.itemPosY)

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
        if turtle.distance(self.turtle_enemy) >= 12:
            turtle.ontimer(self.play, 250)
        else:
            self.playing = False

        enemy_angle = self.turtle_enemy.towards(turtle.pos())
        self.turtle_enemy.setheading(enemy_angle)
        self.turtle_enemy.forward(self.enemyTurtleSpeed)

        turtlePosX = turtle.pos()[0]
        turtlePosY = turtle.pos()[1]

        turtle.forward(self.playerSpeed)

        if turtlePosX > self.availMapURX:
            turtle.setheading(180)
        elif turtlePosX < self.availMapLLX:          
            turtle.setheading(0)
        elif turtlePosY > self.availMapURY:          
            turtle.setheading(270)
        elif turtlePosY < self.availMapLLY:          
            turtle.setheading(90)

        if self.turtle_enemy.distance(self.item) < 12 and self.itemThrowCheck == 1:
                self.enemyTurtleSpeed-=1
                self.item.setpos(1000, 1000)
                self.itemThrowCheck = 0
                self.itemGetCheck = 0
    
        if turtle.distance(self.score_food) < 12:
            self.jumpSound.play()
            score_foodPosX = random.randint(self.availMapLLX, self.availMapURX)
            score_foodPosY = random.randint(self.availMapLLY, self.availMapURY)
            self.score_food.goto(score_foodPosX, score_foodPosY)

            itemGenProb = random.randint(0, 1)

            if itemGenProb == 0 and self.itemGetCheck == 0:
                self.item.showturtle()
                itemPosX = random.randint(self.availMapLLX, self.availMapURX)
                itemPosY = random.randint(self.availMapLLY, self.availMapURY)
                self.item.goto(itemPosX, itemPosY)

        if turtle.distance(self.item) < 12 and self.itemThrowCheck == 0:
            self.jumpSound.play()
            itemTypeProb = random.randint(0, 1)

            if itemTypeProb == 0:
                #boost
                self.item.color('blue')
                self.item.goto(-450, 400)
                self.itemGetCheck = 1

            if itemTypeProb == 1:
                #banana
                self.item.color('yellow')
                self.item.goto(-450, 400)
                self.itemGetCheck = 2

    def useItem(self):
        if self.itemGetCheck == 1:
            turtlePosX = turtle.pos()[0] 
            turtlePosY = turtle.pos()[1]

            if turtle.heading() == 0:
                turtle.goto(turtlePosX+100, turtlePosY)
            elif turtle.heading() == 90:
                turtle.goto(turtlePosX, turtlePosY+100)
            elif turtle.heading() == 180:
                turtle.goto(turtlePosX-100, turtlePosY)
            elif turtle.heading() == 270:
                turtle.goto(turtlePosX, turtlePosY-100)

            self.itemGetCheck = 0
            self.item.hideturtle
            self.item.goto(1000, 1000)
        elif self.itemGetCheck == 2:
            self.itemThrowCheck = 1
            self.item.setpos(turtle.pos())

    def start(self):
        if self.playing == False:
            self.playing = True
            self.play()

    def initGameEnv(self):
        self.menuBgm.stop()
        self.gameBgm.play(loops=-1)

        self.title.hideturtle()
        self.startButton.hideturtle()
        self.scoreBoard.hideturtle()
        self.exit.hideturtle()

        turtle.onkeypress(self.turn_right, 'Right')
        turtle.onkeypress(self.turn_up, 'Up')
        turtle.onkeypress(self.turn_left, 'Left')
        turtle.onkeypress(self.turn_down, 'Down')
        turtle.onkeypress(self.start, 'space')
        turtle.onkeypress(self.useItem, 'z')

        self.mapDrawingPen.speed(0)
        self.mapDrawingPen.pensize(10)
        self.mapDrawingPen.color('white')
        self.mapDrawingPen.penup()
        self.mapDrawingPen.goto(0, self.mapSizeLLY)
        self.mapDrawingPen.pendown()
        self.mapDrawingPen.goto(self.mapSizeURX, self.mapSizeLLY)
        self.mapDrawingPen.goto(self.mapSizeURX, self.mapSizeURY)
        self.mapDrawingPen.goto(self.mapSizeLLX, self.mapSizeURY)
        self.mapDrawingPen.goto(self.mapSizeLLX, self.mapSizeLLY)
        self.mapDrawingPen.goto(0, self.mapSizeLLY)

        self.initPlayerTurtle()
        self.initEnemyTurtle()
        self.initScoreFood()
        self.initItem()

        turtle.listen()
        turtle.mainloop()

if __name__ == '__main__':
    game = turtleRun()
    game.initLogo()
    game.initMenu()

    turtle.mainloop()