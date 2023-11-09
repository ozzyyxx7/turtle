import turtle
import threading
import random

# 거북이 생성 함수
def create_turtle(name):
    t = turtle.Turtle()
    t.speed(1)
    t.penup()
    t.color(random.random(), random.random(), random.random())  # 무작위 색상
    t.goto(random.randint(-200, 200), random.randint(-200, 200))  # 무작위 위치
    t.pendown()
    while True:
        t.forward(1)
        t.left(random.randint(0, 360))

# 거북이 스레드 생성
num_turtles = 5  # 원하는 거북이 수
threads = []
for i in range(num_turtles):
    thread = threading.Thread(target=create_turtle, args=(f"Turtle-{i+1}",))
    threads.append(thread)

# 스레드 실행
for thread in threads:
    thread.start()

# 화면 업데이트