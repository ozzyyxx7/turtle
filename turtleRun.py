import turtle
import threading
import random
import time

# 랜덤 움직임을 위한 함수
def random_move(t):
    while True:
        t.forward(random.randint(1, 10))
        t.left(random.randint(-180, 180))
        time.sleep(1)


# 사용자 조작을 위한 함수
def move_turtle(event):
    if event == "Up":
        user_turtle.setheading(90)  # 위쪽 화살표 키를 누르면 위쪽으로 이동
    elif event == "Down":
        user_turtle.setheading(270)  # 아래쪽 화살표 키를 누르면 아래쪽으로 이동
    elif event == "Left":
        user_turtle.setheading(180)  # 왼쪽 화살표 키를 누르면 왼쪽으로 이동
    elif event == "Right":
        user_turtle.setheading(0)  # 오른쪽 화살표 키를 누르면 오른쪽으로 이동

# 화면 설정
screen = turtle.Screen()
screen.listen()

# 사용자가 조작하는 거북이 생성
user_turtle = turtle.Turtle()
user_turtle.speed(1)

# 랜덤 움직임을 하는 거북이 생성
random_turtle = turtle.Turtle()
random_turtle.speed(1)

# 사용자 조작 키 설정
screen.onkeypress(lambda: move_turtle("Up"), "Up")
screen.onkeypress(lambda: move_turtle("Down"), "Down")
screen.onkeypress(lambda: move_turtle("Left"), "Left")
screen.onkeypress(lambda: move_turtle("Right"), "Right")

# 스레드를 사용하여 랜덤 움직임을 하는 거북이 시작
random_thread = threading.Thread(target=random_move, args=(random_turtle,))
random_thread.start()

# 그래픽 창 유지
turtle.done()