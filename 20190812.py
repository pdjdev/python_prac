#30813 박동준
import turtle, time

t = turtle.Pen()
a = turtle.Pen()
txt = turtle.Pen()
t.speed(0)
a.speed(0)
t.ht()
a.ht()
txt.ht()


def wait():
    time.sleep(3)
    penreset()
    time.sleep(0.1)

def penreset():
    t.clear()
    a.clear()
    t.color('black')
    a.color('black')
    t.penup()
    a.penup()
    t.home()
    a.home()
    t.pendown()
    a.pendown()

def writetxt(s):
    txt.clear()
    txt.penup()
    txt.goto(0,300)
    txt.pendown()
    txt.write(s, align='center', font=('돋움', 15))
    txt.pendown()

writetxt('반복 사각형')
for x in range(100):
    t.forward(x)
    t.left(90) 
wait()

writetxt('지름 10 미로')
for x in range(0,251,10):
    t.forward(x)
    t.left(90)
wait()

writetxt('비튼 반복 사각형')
for x in range(0,800,3):
    t.forward(x)
    t.left(91)
wait()

writetxt('장미모양')
t.color('red')
for x in range(6):
    t.circle(100)
    t.left(360/6)
a.color('blue')
for x in range(20):
    a.circle(20)
    a.left(360/20)
wait()

writetxt('4색 원')
colors = ['red', 'blue', 'orange', 'green']
for x in range(4):
    t.pencolor(colors[x])
    t.circle(50)
    t.left(90)
wait()    

writetxt('태양 그리기')
for i in range(15):
    t.left(180-(180/15))
    t.forward(200)
wait()

writetxt('대화 상자 출력')
n = int(turtle.numinput('입력', '원 개수?', 6))
for x in range(n):
    t.circle(100)
    t.left(360/n)
wait()

writetxt('이름 쓰기')
name = turtle.textinput('입력', '이름?')
t.penup()
t.goto(-50,20)
t.pendown()
for x in range(2):
    t.forward(100)
    t.right(90)
    t.forward(40)
    t.right(90)
t.penup()
t.home()
t.goto(0,-12)
t.write(name, align='center', font=('궁서', 20, 'bold'))
wait()

writetxt('회전 정사각형')
for i in range(100):
    for x in range(4):
        t.forward(100)
        t.left(90)
    t.left(3)
wait()

